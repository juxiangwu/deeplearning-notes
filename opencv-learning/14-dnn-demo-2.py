# -*- coding: utf-8 -*-
import cv2
import numpy as np
#from imutils.video import WebcamVideoStream
#import imutils
import time

#vs = WebcamVideoStream(src=0).start()

rows = open("../datas/model/synset_words.txt").read().strip().split("\n")
classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

#while True:

frame = cv2.imread("../datas/model/space_shuttle.jpg")#vs.read()
#frame = imutils.resize(frame, width=400)

#cv2.imshow("Frame", frame)
# send to DNN.
blob = cv2.dnn.blobFromImage(frame, 1, (224, 224), (104, 117, 123))
print("Loading model...")
net = cv2.dnn.readNetFromCaffe("../datas/model/bvlc_googlenet.prototxt", "../datas/model/bvlc_googlenet.caffemodel")
net.setInput(blob)
start = time.time()
predictions = net.forward()
end = time.time()
print("Classification took {:.5} seconds".format(end - start))
indices = np.argsort(predictions[0])[::-1][:5]

for(i, index) in enumerate(indices):

    if i == 0:
        text = "{}, {:.2f}%".format(classes[index], predictions[0][index] * 100)
        cv2.putText(frame, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        print("{}. label: {}, probability: {:.5}".format(i + 1, classes[index], predictions[0][index]))

cv2.imshow("Classification", frame)
cv2.waitKey()
cv2.destroyAllWindows()

