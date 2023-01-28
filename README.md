# Visual Pollution Detection
![](https://github.com/3bodymo/visual-pollution-detection/blob/main/demo.jpg)
We built a machine learning solution to detect and evaluate different types of visual pollution in street imagery taken from a moving vehicle.

## Setup

```shell
git clone https://github.com/3bodymo/visual-pollution-detection.git
cd visual-pollution-detection
```

* **Before install the modules, make sure that you have python3.9 version and run the model on it.**

* After that, you have to install some python libraries by run the following command:

```shell
pip install -r requirements.txt
```

* Now you can run YOLOv7 model successfully, but it will run over the CPU, so if you want to run it over GPU, install PyTorch by this command:

```shell
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

## Getting Started

 ```shell
python detect.py --source image.jpg --weights runs/train/yolov7-custom-100-epoch/weights/best.pt --conf 0.25
```
