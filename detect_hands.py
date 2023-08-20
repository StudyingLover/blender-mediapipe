import cv2
import mediapipe as mp
import json

def detect_hand_and_save_pose():
    # 打开摄像头
    cap = cv2.VideoCapture(2)

    # 初始化mediapipe
    mp_hands = mp.solutions.hands
    mp_drawing  = mp.solutions.drawing_utils
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    # 初始化pose字典
    pose = {
        '0': {'x': 0, 'y': 0, 'z': 0},
        '1': {'x': 0, 'y': 0, 'z': 0},
        '2': {'x': 0, 'y': 0, 'z': 0},
        '3': {'x': 0, 'y': 0, 'z': 0},
        '4': {'x': 0, 'y': 0, 'z': 0},
        '5': {'x': 0, 'y': 0, 'z': 0},
        '6': {'x': 0, 'y': 0, 'z': 0},
        '7': {'x': 0, 'y': 0, 'z': 0},
        '8': {'x': 0, 'y': 0, 'z': 0},
        '9': {'x': 0, 'y': 0, 'z': 0},
        '10': {'x': 0, 'y': 0, 'z': 0},
        '11': {'x': 0, 'y': 0, 'z': 0},
        '12': {'x': 0, 'y': 0, 'z': 0},
        '13': {'x': 0, 'y': 0, 'z': 0},
        '14': {'x': 0, 'y': 0, 'z': 0},
        '15': {'x': 0, 'y': 0, 'z': 0},
        '16': {'x': 0, 'y': 0, 'z': 0},
        '17': {'x': 0, 'y': 0, 'z': 0},
        '18': {'x': 0, 'y': 0, 'z': 0},
        '19': {'x': 0, 'y': 0, 'z': 0},
        '20': {'x': 0, 'y': 0, 'z': 0}
    }

    while True:
        # 读取摄像头图像
        ret, frame = cap.read()

        # 检测手部姿势
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            # 获取第一只手的关键点坐标
            hand_landmarks = results.multi_hand_landmarks[0]
            for idx, landmark in enumerate(hand_landmarks.landmark):
                # 归一化坐标到-30到30
                normalized_x = (landmark.x * 60) - 30
                normalized_y = (landmark.y * 60) - 30
                normalized_z = (landmark.z * 60) - 30

                pose[str(idx)]['x'] = normalized_x
                pose[str(idx)]['y'] = normalized_y
                pose[str(idx)]['z'] = normalized_z
            
            
            # 保存手的位置到pose.json
            with open('pose.json', 'w') as f:
                json.dump(pose, f)

        # 在图像上绘制手部姿势关键点
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # 显示图像
        cv2.imshow('Hand Pose Detection', frame)

        # 按下'q'键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头和关闭窗口
    cap.release()
    cv2.destroyAllWindows()

# 调用函数开始检测手的位置并保存到pose.json文件：

if __name__ == '__main__':
    detect_hand_and_save_pose()