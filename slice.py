import cv2
extractframes = False
#extractframes
if extractframes:
    vidcap = cv2.VideoCapture('video.mp4')
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("imgdata/train_%d.png" % count, image)
        success, image = vidcap.read()
        print("saved img ", count) 
        count += 1

# take image

startframe = 100
framestep = 1
stepx = 0
stepy = 1
startx = 0
starty = 0
totalframes = 1000


bufimg = cv2.imread("imgdata/train_%d.png" % startframe, -1)

for step in range(startframe, startframe + totalframes): 
    img = cv2.imread("imgdata/train_%d.png" % step, -1)
    # print(img[starty])
    # img[starty]
    bufimg[starty] = img[starty]
    starty += 1


cv2.imshow("output", bufimg)
cv2.imwrite("output.png", bufimg)


