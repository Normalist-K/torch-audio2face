import os
from tqdm.auto import tqdm
from multiprocessing import Pool

from audiolazy import lpc
import librosa
import numpy as np
import numpy.typing as npt
import pandas as pd
import scipy.signal as signal
import scipy.io.wavfile as wav


"""
- In practice, we use 520ms worth of audio as input, i.e., 260ms of past and future samples with respect to the desired output pose. 
    - We chose this value to capture relevant effects like phoneme coarticulation without providing too much data that might lead to overfitting. 
- The input audio window is divided into 64 audio frames with **2x overlap**, so that each frame corresponds to **16ms (256 samples)** and consecutive frames are located **8ms (128 samples)** apart. 
- For each audio frame, we remove the DC component and apply the standard **Hann window** to reduce temporal aliasing effects. 
    - c.f.) detrending: 선형 노이즈를 제거하고 랜덤 노이즈만 남김. 신호처리에서 보다 큰 선형성을 가지는 주파수가 있다면 그걸 제외하고 실제 신호정보만 남기는 것.
- Finally, we calculate **K = 32** autocorrelation coefficients to yield a total of 64*32 scalars for the input audio window. 
    - Although much fewer autocorrelations, e.g. K = 12, would suffice to identify individual phonemes, we choose to retain more information about the original signal to allow the subsequent layers to also detect variations in pitch.
"""


def cal_audio_sec(sig, sr=16000):
    return len(sig) / sr


def cal_bs_sec(bs, fps=60):
    return len(bs) / fps


def cal_bs_fps(bs, sec):
    return len(bs) / sec


def enframe(
    sig: npt.ArrayLike, 
    win_size: int = 8320, 
    hop_len: float = 266.6666666666667
    ) -> np.ndarray:
    """
    turn audio signal to frames.
    params:
        sig: original audio signal
        win_size: length of each frame
        hop_len: intervals of consecutive frames, 
            (normally int type, but use float for frame length correction between audio and blendshape)
    return:
        frames: framed audio signal (default size: N * 64 * 256)
    """

    sig_len = len(sig) # 1152000
    num_frames = int(np.ceil((1.0 * sig_len - win_size + hop_len) / hop_len)) # 4290
    
    # if needed, pad signal
    pad_len = int((num_frames - 1) * hop_len + win_size) # 1152053
    if pad_len - sig_len > 0:
        sig = np.pad(sig, (0, pad_len - sig_len), constant_values=0)
    
    # enframe
    indices = np.tile(np.arange(0, win_size), (num_frames, 1)) + \
              np.tile(np.trunc(np.arange(0, num_frames * hop_len, hop_len)).astype(int), (win_size, 1)).T
    frames = sig[indices]
    
    return frames


def trunc_bs(bs_csv, len_input_audios):
    """
    - 특정 길이(520ms)의 음성 신호를 넣었을 때 한 프레임의 블렌드쉐입과 매칭되도록 만들어 줌
    - 전체 음성을 특정 길이(520ms)로 enframe시키고
    - 블렌드쉐입 프레임을 truncate 시켜줌
        - 음성 길이(520ms)가 블렌드쉐입의 한 프레임(16.7ms)보다 훨씬 크기 때문에 
        - 블렌드쉐입의 처음과 끝쪽 프레임을 잘라서 음성 frames에 맞춰줌
    """
    num_trunc = len(bs_csv) - len_input_audios
    return bs_csv[num_trunc//2:-num_trunc//2]


def _lpc_K(frames, order=32):
        filt = lpc.nautocor(frames, order=order)
        return filt.numerator[1:]
    
    
def lpc_frames(
    frames: npt.ArrayLike, 
    order: int = 32, 
    num_worker: int = 8,
    detrending: bool = True, 
    hanning: bool = True
    ) -> np.ndarray:
    """
    calculate lpc features
    params:
        frames: framed audio signals (defualt size: 64 * 256)
        order: lpc order
        num_worker: for multiprocessing
        detrending: whether remove DC component
        hanning: whether apply the standard Hann windowing to reduce temporal aliasing effects
    return:
        lpc_feature: framed lpc features (defualt size: 64 * 32)
    """
    if detrending:
        frames = signal.detrend(frames, axis=-1, type='constant')
    
    if hanning:
        frames = frames * np.hanning(frames.shape[1])
    
    lpc_feature = np.zeros(shape=(len(frames), order))
    if num_worker:
        pool = Pool(num_worker)
        filt_coef = pool.map(_lpc_K, frames)
        lpc_feature[:] = filt_coef
    else:
        for i, frame in enumerate(frames):
            lpc_feature[i] = _lpc_K(frame, order=order)
    
    return lpc_feature


def lpc_input_audio(input_audio):
    frames = enframe(input_audio, win_size=256, hop_len=128)
    lpc_features = lpc_frames(frames, num_worker=0)
    return lpc_features


def main():
    pass



if __name__ == '__main__':
    main()