import cv2 as cv
# Reading images
# img = cv.imread('Untitled.jpg')

# cv.imshow('Cat', img)

# Reading Videos
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()

    cv.imshow('Cam', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllwindows()

# cv.waitKey(0)

