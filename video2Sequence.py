import os
import cv2
import numpy as np
import time

file_path = os.sys.argv[1]
if not os.path.exists(file_path):
    print("file path error")
    print("usage: <file_path>")
    exit()

videoCapture = cv2.VideoCapture(file_path)
#get fps and size
#fps = videoCapture.get(cv2.CV_CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 5
print ("Begin to generate the graphs.")
print (fps)

#read frame
if not os.path.exists('rgb/'):
    os.makedirs('rgb')
success, frame = videoCapture.read()
stamp = time.time()

nx = frame.shape[1]/2
ny = frame.shape[0]/2

stack=[]
stack_time=[]


iteration = 1

while success:
    # cv2.imshow("display", frame) #show the graph
    if (iteration % 100 == 0):
        print (str(iteration) + " graph have been generated.")

    cv2.waitKey(int(1000/fps)) #delay
    resized = cv2.resize(frame, (nx, ny))
    cv2.imwrite('rgb/'+str(stamp)+'.png',resized)
    success, frame = videoCapture.read() #read the next frame
    stack_time.append(stamp)
    stamp = time.time()
    stack.append(resized)
    iteration= iteration +1


#while not success:
   # reverse video then write
 #  print("Starting reverse.")
  # if(iteration % 10 == 0):
#	print (str(iteration) + " graph have been generated(reverse).")
 #  cv2.waitKey(int(1000/fps)) #delay
  # reverseImage = stack.pop()
   #cv2.imwrite('rgb/'+str(stamp)+'.png',reverseImage)
  # stack_time.append(stamp)
  # stamp = time.time()
  # if not stack:
#	success = 1


print("All graphs have been generated.")
print("Begin to generate index file.")

file_object = open('rgb.txt','w')
Ostr = ''
num = len(os.listdir('rgb'))
for index, timestamp in enumerate(stack_time):

    Ostr = Ostr + str(timestamp) + ' rgb/' + str(timestamp) + '.png\n'
file_object.writelines(Ostr)
file_object.close()
print("Done.")
