# USAGE
# python build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/adrian

# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os
import sqlite3
ch = "Y"
while ch == "Y" or ch == "y":
	conn = sqlite3.connect("child.db")
	c = conn.cursor()
	c.execute("SELECT rowid ,C_ID FROM details WHERE SET_EXIST = Null")
	for row in c.fetchall():
		print(row)
	val = int(intput().strip())
	for row in c.fetchall():
		if val == row[0]:
		c_id = row[1]
		break



	# load OpenCV's Haar cascade for face detection from disk
	detector = cv2.CascadeClassifier(
		"build-face-dataset\haarcascade_frontalface_default.xml")

	# initialize the video stream, allow the camera sensor to warm up,
	# and initialize the total number of example faces written to disk
	# thus far
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	# vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)
	total = 0

	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream, clone it, (just
		# in case we want to write it to disk), and then resize the frame
		# so we can apply face detection faster
		frame = vs.read()
		orig = frame.copy()
		frame = imutils.resize(frame, width=800)

		# detect faces in the grayscale frame
		rects = detector.detectMultiScale(
			cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
			minNeighbors=15, minSize=(30, 30))

		# loop over the face detections and draw them on the frame
		for (x, y, w, h) in rects:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# show the output frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
	
		# if the `k` key was pressed, write the *original* frame to disk
		# so we can later process it and use it for face recognition
		if key == ord("k"):
			p = os.path.sep.join(f"{c_id}", "{}.png".format(
				str(total).zfill(5))])
			cv2.imwrite(p, orig)
			total += 1

		# if the `q` key was pressed, break from the loop
		elif key == ord("q"):
			break

	# do a bit of cleanup
	print("[INFO] {} face images stored".format(total))
	print("[INFO] cleaning up...")
	cv2.destroyAllWindows()
	vs.stop()
	print("Wanna add more? Press Y/y. Press any other key to stop")
	ch = input().strip()
	
conn.commit()
conn.close()
