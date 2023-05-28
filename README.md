### 关键点自动标注步骤 👋
# 1.YOLO-V8安装；
-conda create -n yolo python=3.8
-conda activate yolo
-pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ultralytics
-pip install ultralytics –upgrade
-pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy opencv-python 
# 2.用YOLO-V8进行关键点检测，将检测到的关键点保存到YOLO格式txt文件；
-yolo pose predict model= yolov8x-pose-p6.pt source=images device=0 save_txt=True save=False
# 3.采用YOLO_to_Labelme_use.py脚本，修改读入YOLO格式txt文件路径、输出Labelme格式JSON格式文件路径，并运行脚本；
# 4.将labelme格式的json文件和对应的图片文件导入标注工具labelme，对关键点进行人工矫正；
# 5.把矫正后的labelme格式数据导出，转成需要的MSCOCO格式json文件。

# 补充：YOLO-V8资料
YOLOV8文档：https://docs.ultralytics.com
YOLOV8的Github主页：https://github.com/ultralytics/ultralytics
所有模型：https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models/v8
Pose预训练模型：https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models#pose
预测参数文档：https://docs.ultralytics.com/usage/cfg/#predict
