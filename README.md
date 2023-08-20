# blender-mediapipe
This is a project that utilizes Mediapipe to detect key points and control objects in Blender. It can serve as a foundation for creating digital humans.

## Introduction
`detect_hands.py` will detect the key points of the hand and save these points to `pose.json`. `server_hand.py` will read the key points from `pose.json` and control the hand in Blender.

## Installation
1. Install [Blender](https://www.blender.org/download/),or `yay blender` in Archlinux.
2. Run `pip install -r requirements.txt` to install the required python packages.
3. Run `pip install bpy==2.91a0 && bpy_post_install` if install `bpy` failed.

## Usage
1. Run `python detect_hands.py` to start the detection hands.
2. Run `blender hand.blend  --python server_hand.py` to start and control the hand in Blender.

**Node: The hand is only some points**

## TODO
1. Set the coordinates of the hand within a specific range.
2. Set the position of the camera.
3. Complete the modeling of the hand.
4. Develop other modules of Mediapipe.
5. More effective control ways of the hand in Blender.