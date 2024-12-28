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

startframe = 0
framestep = 1
stepx = 0
stepy = 1
startx = 0
starty = 0
totalframes = 511

direc = "/home/kaos/Documents/AI/VQgancuda/VQGAN-CLIP/1steps/"


bufimg = cv2.imread(direc + "%d.png" % startframe, -1)


for step in range(startframe, startframe + totalframes): 
    img = cv2.imread(direc + "%d.png" % step, -1)
    # img[starty]
    #img.col(starty).copyTo(bufimg.col(starty))
    bufimg[:,starty] = img[:,starty] # colums
    # bufimg[starty] = img[starty] # rows
    starty += 1


cv2.imshow("output", bufimg)
cv2.imwrite("saturnslicecol.png", bufimg)


