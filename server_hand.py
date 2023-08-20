
import sys
import bpy

sys.path.append('/home/zjh/.conda/envs/blender/lib/python3.7/site-packages')

import json

figure0 = bpy.data.objects['Figure0']
figure1 = bpy.data.objects['Figure1']
figure2 = bpy.data.objects['Figure2']
figure3 = bpy.data.objects['Figure3']
figure4 = bpy.data.objects['Figure4']
figure5 = bpy.data.objects['Figure5']
figure6 = bpy.data.objects['Figure6']
figure7 = bpy.data.objects['Figure7']
figure8 = bpy.data.objects['Figure8']
figure9 = bpy.data.objects['Figure9']
figure10 = bpy.data.objects['Figure10']
figure11 = bpy.data.objects['Figure11']
figure12 = bpy.data.objects['Figure12']
figure13 = bpy.data.objects['Figure13']
figure14 = bpy.data.objects['Figure14']
figure15 = bpy.data.objects['Figure15']
figure16 = bpy.data.objects['Figure16']
figure17 = bpy.data.objects['Figure17']
figure18 = bpy.data.objects['Figure18']
figure19 = bpy.data.objects['Figure19']
figure20 = bpy.data.objects['Figure20']

pose = {
    '0':{'x':0,'y':30,'z':0},
    '1':{'x':0,'y':0,'z':0},
    '2':{'x':0,'y':0,'z':0},
    '3':{'x':0,'y':0,'z':0},
    '4':{'x':0,'y':0,'z':0},
    '5':{'x':0,'y':0,'z':0},
    '6':{'x':0,'y':0,'z':0},
    '7':{'x':0,'y':0,'z':0},
    '8':{'x':0,'y':0,'z':0},
    '9':{'x':0,'y':0,'z':0},
    '10':{'x':0,'y':0,'z':0},
    '11':{'x':0,'y':0,'z':0},
    '12':{'x':0,'y':0,'z':0},
    '13':{'x':0,'y':0,'z':0},
    '14':{'x':0,'y':0,'z':0},
    '15':{'x':0,'y':0,'z':0},
    '16':{'x':0,'y':0,'z':0},
    '17':{'x':0,'y':0,'z':0},
    '18':{'x':0,'y':0,'z':0},
    '19':{'x':0,'y':0,'z':0},
    '20':{'x':0,'y':0,'z':0},
}


# import bpy
# import cv2

# # 设置捕获的图像尺寸
# image_width = 640
# image_height = 480

# # 创建OpenCV窗口
# cv2.namedWindow("Camera View", cv2.WINDOW_NORMAL)

# # 获取默认摄像机
# camera = bpy.context.scene.camera

# # 设置渲染参数
# render = bpy.context.scene.render
# render.use_compositing = False  # 禁用合成
# render.resolution_x = image_width
# render.resolution_y = image_height
# render.image_settings.file_format = 'PNG'

  

while True:
    # 从pose.json文件中读取关键点坐标
    try:
        with open('pose.json', 'r') as f:
            pose = json.load(f)
    except:
        pass

    figure0.location.x = pose['0']['x']
    figure0.location.y = pose['0']['y']
    figure0.location.z = pose['0']['z']
    
    figure1.location.x = pose['1']['x']
    figure1.location.y = pose['1']['y']
    figure1.location.z = pose['1']['z']
    
    figure2.location.x = pose['2']['x']
    figure2.location.y = pose['2']['y']
    figure2.location.z = pose['2']['z']
    
    figure3.location.x = pose['3']['x']
    figure3.location.y = pose['3']['y']
    figure3.location.z = pose['3']['z']
    
    figure4.location.x = pose['4']['x']
    figure4.location.y = pose['4']['y']
    figure4.location.z = pose['4']['z']
    
    figure5.location.x = pose['5']['x']
    figure5.location.y = pose['5']['y']
    figure5.location.z = pose['5']['z']
    
    figure6.location.x = pose['6']['x']
    figure6.location.y = pose['6']['y']
    figure6.location.z = pose['6']['z']
    
    figure7.location.x = pose['7']['x']
    figure7.location.y = pose['7']['y']
    figure7.location.z = pose['7']['z']
    
    figure8.location.x = pose['8']['x']
    figure8.location.y = pose['8']['y']
    figure8.location.z = pose['8']['z']
    
    figure9.location.x = pose['9']['x']
    figure9.location.y = pose['9']['y']
    figure9.location.z = pose['9']['z']
    
    figure10.location.x = pose['10']['x']
    figure10.location.y = pose['10']['y']
    figure10.location.z = pose['10']['z']
    
    figure11.location.x = pose['11']['x']
    figure11.location.y = pose['11']['y']
    figure11.location.z = pose['11']['z']
    
    figure12.location.x = pose['12']['x']
    figure12.location.y = pose['12']['y']
    figure12.location.z = pose['12']['z']
    
    figure13.location.x = pose['13']['x']
    figure13.location.y = pose['13']['y']
    figure13.location.z = pose['13']['z']
    
    figure14.location.x = pose['14']['x']
    figure14.location.y = pose['14']['y']
    figure14.location.z = pose['14']['z']
    
    figure15.location.x = pose['15']['x']
    figure15.location.y = pose['15']['y']
    figure15.location.z = pose['15']['z']
    
    figure16.location.x = pose['16']['x']
    figure16.location.y = pose['16']['y']
    figure16.location.z = pose['16']['z']
    
    figure17.location.x = pose['17']['x']
    figure17.location.y = pose['17']['y']
    figure17.location.z = pose['17']['z']
    
    figure18.location.x = pose['18']['x']
    figure18.location.y = pose['18']['y']
    figure18.location.z = pose['18']['z']
    
    figure19.location.x = pose['19']['x']
    figure19.location.y = pose['19']['y']
    figure19.location.z = pose['19']['z']
    
    figure20.location.x = pose['20']['x']
    figure20.location.y = pose['20']['y']
    figure20.location.z = pose['20']['z']
    
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    # capture_camera_frame()