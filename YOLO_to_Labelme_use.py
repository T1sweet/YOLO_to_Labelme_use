import os
import json
import shutil
import numpy as np
from tqdm import tqdm
import copy

#########################################################
# 多个文件：yolo格式 转 labelme格式
#########################################################
yolo_dict_format = {   # 初始化labelme格式
    "version": "5.1.1",                 # labelme版本
    "flags": {},
    "shapes": [{                 # 标注
        "label": "people",              # 类别：如关键点类别left_eye
        "points": [[0, 0], [0, 0]],     # 关键点坐标
        "group_id": 0,                  # 组的id
        "shape_type": "rectangle",      # 标注类别：如point，rectangle
        "flags": {}
    }],
    "imagePath": "00004.png",
    "imageData": None,
    "imageHeight": 1080,
    "imageWidth": 1920
}
keypoints = ['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear',
                  'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist',
                  'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
                  'left_ankle', 'right_ankle']

yolo_txt_path = 'E:\\dataset\\set01\\runs\pose\\predict2\\labels\\'    # yolo格式txt文件路径
labelme_json_path = 'E:\\dataset\\set01\\runs\pose\\predict2\\json\\'  # labelme格式json文件路径

extension = '.txt'      # 文件后缀
files = [file for file in os.listdir(yolo_txt_path) if file.endswith(extension)]    # 查看指定目录下指定后缀的列表
for file in tqdm(files):
    print(file)
    yolo_txt = yolo_txt_path + file
    with open(yolo_txt, 'r', encoding='utf-8') as f:
        lines = f.readlines()       # 按行读取
        print(lines)
        yolo_dict = copy.deepcopy(yolo_dict_format)    # 一张图片一个字典
        yolo_dict["imagePath"] = str(int(file.split('.')[0].split('_')[-1]) - 0).zfill(5) + '.png'
        people_id = 0
        for line in lines:          # 遍历每一行
            line = line.replace("\n", "")
            line_list = line.split(' ')
            print(line_list)
            for i in range(len(line_list)):
                if i == 0:
                    yolo_dict["shapes"][-1]["label"] = "people"
                    yolo_dict["shapes"][-1]["shape_type"] = "rectangle"
                    yolo_dict["shapes"][-1]["group_id"] = people_id
                elif i == 1:
                    center_x = float(line_list[i]) * yolo_dict["imageWidth"]
                elif i == 2:
                    center_y = float(line_list[i]) * yolo_dict["imageHeight"]
                elif i == 3:
                    yolo_dict["shapes"][-1]["points"] = [[0, 0], [0, 0]]
                    bbox_width = float(line_list[i]) * yolo_dict["imageWidth"]
                    yolo_dict["shapes"][-1]["points"][0][0] = center_x - bbox_width / 2
                    yolo_dict["shapes"][-1]["points"][1][0] = center_x + bbox_width / 2
                elif i == 4:
                    bbox_height = float(line_list[i]) * yolo_dict["imageHeight"]
                    yolo_dict["shapes"][-1]["points"][0][1] = center_y - bbox_height / 2
                    yolo_dict["shapes"][-1]["points"][1][1] = center_y + bbox_height / 2
                elif i % 2 == 1:
                    yolo_dict["shapes"].append(dict())
                    yolo_dict["shapes"][-1]["group_id"] = people_id
                    yolo_dict["shapes"][-1]["flags"] = {}
                    yolo_dict["shapes"][-1]["label"] = keypoints[int(i/2-2.5)]
                    yolo_dict["shapes"][-1]["shape_type"] = "point"
                    yolo_dict["shapes"][-1]["points"] = [[0, 0]]
                    yolo_dict["shapes"][-1]["points"][0][0] = float(line_list[i]) * yolo_dict["imageWidth"]
                elif i % 2 == 0:
                    yolo_dict["shapes"][-1]["points"][0][1] = float(line_list[i]) * yolo_dict["imageHeight"]
            people_id += 1
    print(yolo_dict)
    labelme_json = labelme_json_path + yolo_dict["imagePath"].split('.')[-2] + '.json'
    with open(labelme_json, "w", encoding='utf-8') as f:
        json.dump(yolo_dict, f)

