# object_detection_nut_analysis

When you run the program, it gives you the type of the object placed in the center.

To run python file called hexagon_circle_detection.py, please use a similar format to the following one: (specify an image name after --image)
python hexagon_circle_detection.py --image 10-11-2017-9.38.49_2.bmp

I used cv2.HoughCircles to detect circles in the image.
- If the circle is detected in a specific radius range, circle as the object type is written on a text file and a circle is drawn on top of the image with a center.
- If there is no circle detected then, I found the contours of that object by using cv2.findContours. 
By looking at the area, I decided whether it a hexagon or not. Then I wrote the outcome in a text file as well as drew the contour.

Here is an example of the result of this object detection algorithm:

![hexagon_result](https://github.com/mandalinadagi/object_detection_nut_analysis/blob/master/hexagon_example.png)
![circle_result](https://github.com/mandalinadagi/object_detection_nut_analysis/blob/master/circle_example.png)

In case of any problem, please contact me via this e-mail address: mandalinadagi@gmail.com

Thank you- 

