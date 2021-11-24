# 环境要求

* python = 3.8.12

* opencv-python = 4.5.3.56
* onnxruntime-gpu = 2.1.3

# 如何使用

* 克隆这个项目```git clone  https://github.com/LitttleHeroZZZX/plate-ocr-based-on-paddleocr.git```
* 修改`predict_system.py`中第192行图片文件的目录，运行后控制台将会输出ocr结果。

# API接口

* `predict_system.py`文件中存在`TextSystem`类，实例化时需要指定配置文件`config.json`的路径。
* `TextSystem`这个实例化后调用自身传入`numpy`格式图片后，将返回识别结果和置信度的`list`
* `TextSystem`中`plateOCR`方法传入参数为`numpy`格式图片，返回只含字母数字的字符串。

# config.json



* 在`config.json`配置文件中可以根据需求修改自定义参数，其中`det_model_dir"`、`cls_model_dir"`、`rec_model_dir"`分别指定了文字检测、方向分类器和识别的三个模型的的位置。
