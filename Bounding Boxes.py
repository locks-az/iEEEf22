import cv2 as cv
path_name = "/img.jpg"

try:
    img = cv.imread("img.jpg")
except Exception:
    print("Invalid Path: {}".format(path_name))
    quit()

height = img.shape[0]
width = img.shape[1]

clickCount = 0

topLeftX = 0
topLeftY = 0
bottomRightX = 0
bottomRightY = 0

clicks = []

def click_event(event, x, y, flags, params):

    global img
    global clickCount

    if (clickCount == 2):
        clicks.sort()
        topLeftX = clicks[0][0]
        topLeftY = clicks[0][1]
        bottomRightX = clicks[1][0]
        bottomRightY = clicks[1][1]

        cv.line(img, (topLeftX,topLeftY), (bottomRightX, topLeftY), (0,0,0), 2)
        cv.line(img, (topLeftX,topLeftY), (topLeftX, bottomRightY), (0,0,0), 2)
        cv.line(img, (bottomRightX,bottomRightY), (topLeftX, bottomRightY), (0,0,0), 2)
        cv.line(img, (bottomRightX,bottomRightY), (bottomRightX, topLeftY), (0,0,0), 2)

        cv.imshow('image', img)
        cv.waitKey(5000)
        cv.destroyAllWindows()
        
    if event == cv.EVENT_LBUTTONDOWN:
        clickCount += 1
        img = cv.circle(img, (x,y), radius=7, color=(0, 0, 255), thickness=-1)
        cv.imshow('image', img)
        clicks.append([x, y])

cv.imshow('image', img)
cv.setMouseCallback('image', click_event)
cv.waitKey(0)

cropped_image = img[clicks[0][1]:clicks[1][1], clicks[0][0]:clicks[1][0]]

print(clicks)

cv.imshow("cropped", cropped_image)
cv.waitKey(5000)
cv.destroyAllWindows() 
