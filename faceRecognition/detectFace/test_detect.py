# import the necessary packages
import requests
import cv2

# load our image and now use the face detection API to find faces in
# images by uploading an image directly

url = "http://localhost:8000/face_detection/detect/"

image = cv2.imread("test.png")
payload = {"image": open("test.png", "rb")}
r = requests.post(url, files=payload).json()
print("test.png: {}".format(r))
 
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

width, height = image.shape[:2]
image = cv2.resize(image,(int(0.5*width), int(0.4*height)), interpolation = cv2.INTER_CUBIC)
 
# show the output image
cv2.imshow("test.png", image)
cv2.waitKey(0)