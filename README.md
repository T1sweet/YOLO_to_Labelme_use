# 关键点自动标注步骤 👋👋👋
### 如果对你的工作有所帮助，记得点上Star✨✨✨
### 1.YOLO-V8安装：
- conda create -n yolo python=3.8
- conda activate yolo
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ultralytics
- pip install ultralytics –upgrade
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy opencv-python 

### 2.用YOLO-V8进行关键点检测，将检测到的关键点保存到YOLO格式txt文件：
- yolo pose predict model= yolov8x-pose-p6.pt source=images device=0 save_txt=True save=False
![image](https://github.com/T1sweet/-/assets/96241702/5cdc6e5f-0fac-442c-bed2-86a68023ff2e)

### 3.在YOLO_to_Labelme_use.py脚本中，修改读入YOLO格式txt文件路径、输出Labelme格式JSON格式文件路径，并运行该脚本：
- yolo_txt_path = 'E:\\dataset\\set01\\runs\pose\\predict2\\labels\\'    # yolo格式txt文件路径
- labelme_json_path = 'E:\\dataset\\set01\\runs\pose\\predict2\\json\\'  # labelme格式json文件路径
![image](https://github.com/T1sweet/-/assets/96241702/48fe53c5-6e99-464f-8f43-b9073501561c)

### 4.将labelme格式的json文件和对应的图片文件导入标注工具labelme，对关键点进行人工矫正；
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple labelme
![image](https://github.com/T1sweet/YOLO_to_Labelme_use/assets/96241702/4add8405-81c1-4e61-853d-be975629c262)

### 补充：YOLO-V8资料
- YOLOV8文档：https://docs.ultralytics.com
- YOLOV8的Github主页：https://github.com/ultralytics/ultralytics
- 所有模型：https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models/v8
- Pose预训练模型：https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models#pose
- 预测参数文档：https://docs.ultralytics.com/usage/cfg/#predict
