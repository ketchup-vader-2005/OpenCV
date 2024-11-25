import cv2 as cv

def changeRes(width,heigth):
    #Live video
    capture.set(3,width)
    capture.set(4, heigth)
    
def rescaleFrame(frame, scale):
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)

    dimensions=(width,heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.75)

    cv.imshow('dog', frame)
    cv.imshow('dog_rescaled', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllwindows()