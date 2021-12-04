# Drowsiness_detection
An OpenCV and CNN based script for drowsiness detection

Dataset is taken from "http://mrl.cs.vsb.cz/eyedataset" and consists of b/w images of the eyes both open and shut.  
The open cv module is used to first detect the left and right and feed it to a trained CNN on the above dataset which detects whether the person is awake or not. If the person is drowsy the timer starts and any action can be performed after some critical limit like playing an alarm in this case.  

Result from the opencv and CNN based detector:  
<img src="https://github.com/mayanksinghkgp/Drowsiness_detection/blob/main/drowsiness.gif" width="300" height="300" />

The YoloV5 based detector is trained on a custom set of images captured using OpenCV and labelled with the help of lableimg.  
The result form the model is as shown below:  
<img scr="https://github.com/mayanksinghkgp/Drowsiness_detection/blob/main/yolov5_drowsy.JPG" width="300" height="300" />
