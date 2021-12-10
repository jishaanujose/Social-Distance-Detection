# Social-Distance-Detection

# Problem Statement
Due to an increase in the number of cases reported around the world, the World Health Organization (WHO) has declared Covid-19 a pandemic. Citizens all across the world are physically separating themselves from the Covid-19 outbreak in order to flatten the curve. To lessen the economic burden of the pandemic, various countries have allowed a restricted number of economic activities to restart after the number of new Covid-10 cases has fallen below a particular threshold. People are urged to avoid any person-to-person contact, such as shaking hands, and to maintain a distance of at least 1 metre between them to limit the risk of infection. Many people, especially when it comes to social distancing, have been seen to disregard public health precautions. Using a deep learning model, this research attempts to make the enforcement of social distancing easier by offering automated detection of social distance violations in workplaces and public spaces.

# Solution
In this study, the deep CNN approach and computer vision techniques are used. Initially, the pedestrian in the video frame was detected using an open-source object detection network based on the YOLOv5 method. Only the pedestrian class was used as a result of the detection, and other object types were ignored in this application.

# Yolov5
When it comes to deep learning-based object identification, the YOLO model is one of the state-of-the-art models that has been shown to deliver considerable speed improvements and is suited for real-time applications. The YOLO model was used to detect pedestrians in this study. The YOLO was trained on the COCO dataset, which has 80 labels, including human and pedestrian classifications.

# Methodology
The pedestrians are detected from the image/video using the pre-trained YOLOv5 model. Convert the image into the 'bird eye view' transformation using cv2 to determine the exact distance between the pedestrians. The distance between the centroids of each bounding box is determined in the transformed view, and if the distance between the centroids is less than a predetermined threshold value, those bounding boxes are colored 'red,' while others are coloured 'green.'

# Tools used
 The model is programmed using python language and uses frameworks such as pandas, numpy, and scikit learn. Pretrained model is taken from
 https://github.com/ultralytics/yolov5.git.
 
 The project is employed in Python3.6 in GoogleColab.
 
 # Output video
 
https://user-images.githubusercontent.com/91037105/145519825-85a54e73-6460-40aa-a7fb-393897a7a879.mp4

