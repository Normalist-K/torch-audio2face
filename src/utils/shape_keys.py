'''
- key10: neutral한 입모양이라고 생각할 수 있을 듯!! 10개의 키만으로 학습하면 기본 입모양을 잘 만들 수 있을 듯 함.
- key14: 다이나믹한 혹은 감정이 포함된 입모양의 최소기준이라고 생각할 수 있을 듯. 
- key18: 입 크기를 좀 더 신경 쓴 느낌
- key22|27: 좀 더 발화자의 개성을 포함 (ex. 한쪽 입꼬리가 자주 올라감)
'''

key2 =  [
    'jawOpen', 'mouthClose'
]
key4 =  key2 + [
    'mouthFunnel', # 'O' 입모양
    'mouthPucker' # 입술 오므리기
]
key8 =  key4 + [
    'mouthRollLower', 'mouthRollUpper', # 입술 안쪽으로 말려들어감
    'mouthShrugLower', 'mouthShrugUpper', # 입술이 바깥쪽으로 튀어나옴
]
key10 = key8 + [
    'mouthDimpleLeft', 'mouthDimpleRight', # 입꼬리 수평으로 이동
]
key14 = key10 + [
    'mouthStretchLeft', 'mouthStretchRight', # 볼 전체 수평 아랫방향으로 늘어남
    'mouthSmileLeft', 'mouthSmileRight', # 입꼬리 위쪽으로 이동
]
key18 =  key14 + [
    'mouthLowerDownLeft', 'mouthLowerDownRight', # 아랫 입술 벌어짐
    'mouthUpperUpLeft', 'mouthUpperUpRight', # 윗 입술 벌어짐
]
key22 =  key18 + [
    'mouthPressLeft', 'mouthPressRight', # 볼 전체 수평 윗방향으로 늘어남
    'mouthFrownLeft', 'mouthFrownRight', # 입꼬리 아래쪽으로 이동
]
key27 =  key22 + [
    'mouthRight', 'mouthLeft', # 전체 입 위치 이동
    'jawForward', 'jawRight', 'jawLeft', # 아래 턱 이동
]

key_dict = {
    2:key2,
    4:key4,
    8:key8,
    10:key10,
    14:key14,
    18:key18,
    22:key22,
    27:key27
}

live_link_face_columns = [
    'Timecode', 'BlendShapeCount', 'EyeBlinkLeft', 'EyeLookDownLeft',
    'EyeLookInLeft', 'EyeLookOutLeft', 'EyeLookUpLeft', 'EyeSquintLeft',
    'EyeWideLeft', 'EyeBlinkRight', 'EyeLookDownRight', 'EyeLookInRight',
    'EyeLookOutRight', 'EyeLookUpRight', 'EyeSquintRight', 'EyeWideRight',
    'JawForward', 'JawRight', 'JawLeft', 'JawOpen', 'MouthClose',
    'MouthFunnel', 'MouthPucker', 'MouthRight', 'MouthLeft',
    'MouthSmileLeft', 'MouthSmileRight', 'MouthFrownLeft',
    'MouthFrownRight', 'MouthDimpleLeft', 'MouthDimpleRight',
    'MouthStretchLeft', 'MouthStretchRight', 'MouthRollLower',
    'MouthRollUpper', 'MouthShrugLower', 'MouthShrugUpper',
    'MouthPressLeft', 'MouthPressRight', 'MouthLowerDownLeft',
    'MouthLowerDownRight', 'MouthUpperUpLeft', 'MouthUpperUpRight',
    'BrowDownLeft', 'BrowDownRight', 'BrowInnerUp', 'BrowOuterUpLeft',
    'BrowOuterUpRight', 'CheekPuff', 'CheekSquintLeft', 'CheekSquintRight',
    'NoseSneerLeft', 'NoseSneerRight', 'TongueOut', 'HeadYaw', 'HeadPitch',
    'HeadRoll', 'LeftEyeYaw', 'LeftEyePitch', 'LeftEyeRoll', 'RightEyeYaw',
    'RightEyePitch', 'RightEyeRoll'
]

columns52 = [
    "eyeBlinkLeft", "eyeLookDownLeft", "eyeLookInLeft", 
    "eyeLookOutLeft", "eyeLookUpLeft", "eyeSquintLeft", "eyeWideLeft", 
    "eyeBlinkRight", "eyeLookDownRight", "eyeLookInRight", "eyeLookOutRight", 
    "eyeLookUpRight", "eyeSquintRight", "eyeWideRight", 
    "jawForward", "jawLeft", "jawRight", "jawOpen", 
    "mouthClose", "mouthFunnel", "mouthPucker", "mouthRight", 
    "mouthLeft", "mouthSmileLeft", "mouthSmileRight", "mouthFrownLeft", "mouthFrownRight", 
    "mouthDimpleLeft", "mouthDimpleRight", "mouthStretchLeft", "mouthStretchRight", "mouthRollLower",
    "mouthRollUpper", "mouthShrugLower", "mouthShrugUpper", "mouthPressLeft", "mouthPressRight", 
    "mouthLowerDownLeft", "mouthLowerDownRight", "mouthUpperUpLeft", "mouthUpperUpRight", 
    "browDownLeft", "browDownRight", "browInnerUp", "browOuterUpLeft", "browOuterUpRight", 
    "cheekPuff", "cheekSquintLeft", "cheekSquintRight",
    "noseSneerLeft", "noseSneerRight", "tongueOut"
]

columns31 = [
    'jawForward', 'jawRight', 'jawLeft', 'jawOpen', 
    'mouthClose', 'mouthFunnel', 'mouthPucker', 
    'mouthRight', 'mouthLeft', 
    'mouthSmileLeft', 'mouthSmileRight', 
    'mouthFrownLeft', 'mouthFrownRight', 
    'mouthDimpleLeft', 'mouthDimpleRight', 
    'mouthStretchLeft', 'mouthStretchRight', 
    'mouthRollLower', 'mouthRollUpper', 
    'mouthShrugLower', 'mouthShrugUpper', 
    'mouthPressLeft', 'mouthPressRight', 
    'mouthLowerDownLeft', 'mouthLowerDownRight', 
    'mouthUpperUpLeft', 'mouthUpperUpRight', 
    'cheekPuff', 'cheekSquintLeft', 'cheekSquintRight', 
    'tongueOut']

columns16 = [
    "jawForward", "jawOpen", "cheekPuff",
    "mouthClose", "mouthFunnel", "mouthPucker",
    "mouthDimpleLeft", "mouthDimpleRight",
    "mouthStretchLeft", "mouthStretchRight",
    "mouthRollLower", "mouthRollUpper",
    "mouthShrugLower", "mouthShrugUpper",
    "mouthPressLeft", "mouthPressRight",
]

columns10 = [
    "jawOpen",
    "mouthPucker", "mouthLeft", "mouthRight",
    "mouthRollUpper", "mouthRollLower",
    "mouthSmileLeft", "mouthSmileRight", 
    "mouthFrownLeft", "mouthFrownRight"
]


# columns31 = [
#     "cheekPuff","cheekSquintLeft","cheekSquintRight",
#     "jawOpen","jawForward","jawLeft","jawRight",
#     "mouthFunnel","mouthPucker","mouthLeft","mouthRight",
#     "mouthRollUpper","mouthRollLower","mouthShrugUpper","mouthShrugLower",
#     "mouthClose","mouthSmileLeft","mouthSmileRight","mouthFrownLeft","mouthFrownRight",
#     "mouthDimpleLeft","mouthDimpleRight","mouthUpperUpLeft",
#     "mouthUpperUpRight","mouthLowerDownLeft","mouthLowerDownRight",
#     "mouthPressLeft","mouthPressRight","mouthStretchLeft","mouthStretchRight","tongueOut"]

# columns16 = [
#     "JawForward",
#     "JawOpen",
#     "MouthClose",
#     "MouthFunnel",
#     "MouthPucker",
#     "MouthDimpleLeft",
#     "MouthDimpleRight",
#     "MouthStretchLeft",
#     "MouthStretchRight",
#     "MouthRollLower",
#     "MouthRollUpper",
#     "MouthShrugLower",
#     "MouthShrugUpper",
#     "MouthPressLeft",
#     "MouthPressRight",
#     "CheekPuff" 
# ]

# ignored_columns16 = [
#     "EyeBlinkLeft", 
#     "EyeBlinkRight", 
#     "EyeLookDownLeft", 
#     "EyeLookDownRight", 
#     "EyeLookInLeft", 
#     "EyeLookInRight", 
#     "EyeLookOutLeft", 
#     "EyeLookOutRight", 
#     "EyeBlinkLeft", 
#     "EyeBlinkRight", 
#     "EyeLookDownLeft", 
#     "EyeLookDownRight", 
#     "EyeLookInLeft", 
#     "EyeLookInRight", 
#     "EyeLookOutLeft", 
#     "EyeLookOutRight", 
#     "EyeLookUpLeft", 
#     "EyeLookUpRight", 
#     "EyeSquintLeft", 
#     "EyeSquintRight", 
#     "EyeWideLeft", 
#     "EyeWideRight", 
#     "BrowDownLeft", 
#     "BrowDownRight", 
#     "BrowInnerUp", 
#     "BrowOuterUpLeft", 
#     "BrowOuterUpRight", 
#     "CheekSquintLeft", 
#     "CheekSquintRight", 
#     "JawLeft", 
#     "JawRight", 
#     "MouthLeft", 
#     "MouthRight", 
#     "MouthUpperUpLeft", 
#     "MouthUpperUpRight", 
#     "MouthLowerDownLeft", 
#     "MouthLowerDownRight", 
#     "MouthSmileLeft", 
#     "MouthSmileRight", 
#     "MouthFrownLeft", 
#     "MouthFrownRight", 
#     "NoseSneerLeft", 
#     "NoseSneerRight", 
#     "HeadYaw", 
#     "HeadPitch", 
#     "HeadRoll", 
#     "TongueOut", 
#     "LeftEyeYaw", 
#     "LeftEyePitch", 
#     "LeftEyeRoll", 
#     "RightEyeYaw", 
#     "RightEyePitch", 
#     "RightEyeRoll"
# ]
