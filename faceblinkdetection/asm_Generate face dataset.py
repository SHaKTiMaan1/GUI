#!/usr/bin/env python
# coding: utf-8

# In[1]:


# *************************************************************************************************
# Author: Andi Sama 
# Purpose: Generate face dataset through integrated camera
# Organization: Sinergi Wahana Gemilang
# Creation Date: April 13, 2020
# Changes history:
#   April 15, 2020: finalized
# *************************************************************************************************


# In[2]:


import os
from imutils.video import VideoStream
import cv2
import time


# In[3]:


# # updating count down value, shown as label on view window during recording
# import threading
# class MyThread(threading.Thread):
#     counter = 0
#     def __init__(self, name, max, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.max = max
#         self.delay = delay
#     def run(self):
#         # print('DEBUG: starting thread...%s', self.name)
#         thread_count_down(self.name, self.max, self.delay)
#         # print('DEBUG: finished thread...%s', self.name)
#     def thread_count_down(self):
#         self.counter = self.max
#         while self.counter:
#             time.sleep(self.delay)
#             print('DEBUG: Thread %s is counting down %i' % (self.name, self.counter))
#             self.counter -= 1
#     def get_count(self):
#         return self.counter 
    
# t =  MyThread("Counting down thread...", 10, 1)
# t.thread_count_down()
# t.get_count()    


# In[4]:


def generate_faces(new_path, new_face):
    video_capture = VideoStream(src=0).start()
    count=1
    while True:
        frame = video_capture.read()
        cv2.imshow("recording faces...", frame)        
        key_pressed = cv2.waitKey(500) # wait 0.5 second
        filename = new_path + '/' + new_face + str(count) + '.jpg'
        if not(key_pressed & 0xFF == ord('q')): # q=quit
            cv2.imwrite(filename, frame)
            count += 1
        else: 
            break

    cv2.destroyAllWindows()
    video_capture.stop()
    print("[LOG] recording done.")
    status=1
    return status


# In[5]:


if __name__ == "__main__":
    face_dir = 'faces/'
    new_face = 'Andi Sama'
    new_path = face_dir + new_face

    # if sub-directory with new name does not exist, then create
    cwd = os.getcwd()
    if os.path.exists(new_path):
        print('Sub directory: "', new_path + '" exists in', cwd, '- please remove it first')
    else:
        try:
            os.mkdir(new_path)
            print('Sub directory: "', new_path + '" created')
            print('LOG: Generating images of face...', new_face)
            if generate_faces(new_path, new_face):
                print("success")
            else:
                print("failed")                
        except FileExistsError:
            print('Sub directory: "', new_path + '" already exist')


# In[ ]:




