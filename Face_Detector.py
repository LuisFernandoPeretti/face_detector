import cv2

# Load some pre-trained data on face frontals from povencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect face in
img = cv2.imread('ME.jpg')

# must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#print(face_coordinates)

cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()

print("Code Completed!")