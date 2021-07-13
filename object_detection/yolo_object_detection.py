import cv2 as cv
import numpy as np

#loading Yolo

net = cv.dnn.readNet('yolov3.weights','yolov3.cfg')
classes = []
with open('coco.names','r') as f:
    classes = [line.strip() for line in f.readlines()]
layers_names = net.getLayerNames()
outputlayers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255, size=(len(classes),3))

#load image
img = cv.imread("bird.jpg")
img = cv.resize(img , None , fx=0.4 , fy=0.4)
height,width,channels = img.shape

#Detecting objects
blob=cv.dnn.blobFromImage(img, 0.00392,(416,416),(0,0,0), True, crop=False)
for b in blob:
    for n, img_blob in enumerate(b):
        cv.imshow(str(n),img_blob)
net.setInput(blob)  # forward the input to the algorithem
outs = net.forward(outputlayers)
#Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence >0.5:
            #object detection
            center_x = int(detection[0]*width)
            center_y = int(detection[1] * height)
            w = int(detection[0] * width)
            h = int(detection[1] * height)

            x = int(center_x-w/2)
            y = int(center_y-h/2)

            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5 , 0.4 )
print(indexes)
font = cv.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y,w,h = boxes[i]
        label =str(classes[class_ids[i]])
        color = colors[i]
        cv.rectangle(img,(x,y),(x+w, y+h),(0,255,0),2)
        cv.putText(img, label, (x, y+30),font, 1, (0,0,0),2)
        print(label)


cv.imshow("img",img)
cv.waitKey(0)



