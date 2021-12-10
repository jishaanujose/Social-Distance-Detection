git clone https://github.com/ultralytics/yolov5  # clone
%cd yolov5
%pip install -qr requirements.txt  # install

from yolov5 import utils
display = utils.notebook_init()  # checks

# Predict using pre-trained YOLOV5 model
python detect_cust.py --weights yolov5s.pt --img 640 --conf 0.25 --source /content/test.mp4
