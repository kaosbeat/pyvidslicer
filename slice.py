import cv2
import lib.tweet as tweet

extractframes = False
# extractframes = True
tweetit = False
tweetit = True


vidname = 'mountain'
print((vidname + ".mp4"))
#extractframes
if extractframes:
    vidcap = cv2.VideoCapture(vidname + ".mp4")
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("imgdata/"+vidname+"_%d.png" % count, image)
        success, image = vidcap.read()
        print("saved img ", count) 
        count += 1

if tweetit:
    tweet.tweetimg("output.png", "experimenting with openCV and slicing")



# take image
startframe = 0
framestep = 1
stepx = 0
stepy = 1
startx = 0
starty = 100
totalframes = 640


slicewidth = 10



bufimg = cv2.imread("imgdata/"+vidname+"_%d.png" % startframe, -1)
print(bufimg.shape[0]) ## for some reason openCV reads columns after rows, so X after Y
for step in range(startframe, startframe + totalframes):
    if starty < bufimg.shape[0]:
        img = cv2.imread("imgdata/"+vidname+"_%d.png" % step, -1)
        # print(img[starty])
        # img[starty]
        bufimg[starty] = img[starty]
        starty += stepy
        if (starty%100 == 0):
            print(starty)


cv2.imshow("output", bufimg)
cv2.imwrite("output.png", bufimg)


