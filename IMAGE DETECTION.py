import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# Read the input image
path = r'C:\Users\ALEX!\Documents\SCHOOL\ALEX.jpg'
img = cv2.imread(path)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print ("Model Found {0} faces!".format(len(faces)))
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 10)
    # Display the output
cv2.imshow('img', img)
cv2.waitKey(0)