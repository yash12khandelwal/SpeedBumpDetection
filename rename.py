import os
os.getcwd()
collection = "/home/yash/AGV/Data/"
count = 0
for filename in os.listdir(collection):
	os.rename(collection + filename, collection + str(count) + ".jpg")
	count += 1
