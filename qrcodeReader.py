import cv2
import pyzbar.pyzbar as pyzbar
from cv2 import cv2

# reading the QR code
img = cv2.imread("QRcode.png")

# decoding the data stored in the code form of an array
decodedObjects = pyzbar.decode(img)
print(decodedObjects) 

for obj in decodedObjects:
    print("Data: ",obj.data)

# displaying the QR code
cv2.imshow("Image", img)
cv2.waitKey(0)


# # Reading using webcam 
# cap = cv2.VideoCapture(0)
# font = cv2.FONT_HERSHEY_PLAIN
# while True:
#     _,  frame = cap.read()
#     decodedObjects = pyzbar.decode(frame)
#     for obj in decodedObjects:
#         # print in terminal 
#         print("Data: ",obj.data)
#         # print on the screen
#         cv2.putText(frame, str(obj.data), (50,50), font, 2, (255,0,0), 3)
    
#     # frame settings 
#     cv2.imshow("Frame", frame)
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

