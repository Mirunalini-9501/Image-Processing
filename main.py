#import necessary packages
from skimage.feature import blob_log
import glob
from skimage.io import imread
import cv2

#image is given as input
example=glob.glob("im4.jpg")[0]

#image is converted to grey scale
img=cv2.imread(example,0)

#laplasian of gaussian algorithm is used
blobs_log=blob_log(img, max_sigma=100, num_sigma=10, threshold=.345)

#counts the objects
numrows=len(blobs_log)

#prints the counted objects
print("count of people : ", numrows)

#checks if crowd is present
if(numrows<6):
	print("No crowd!! Happy Shopping:)")
elif(numrows==6):
	print("WARNING!!! There's chance of crowding ")
else:
#prints other modes of shopping to avoid over crowding
        print("\nCrowded already!!\n\nPlease choose another way of shopping: \n\n1.Shop online and get delivered to your alloted lobby or carspace!")
	print("2.Choose a time slot! ")

	#inputs the mode of shopping
	choice=int(input("\nEnter the choice :"))

	#1st choice
	if(choice==1):
		print("\nPlease visit our online website!")

  #2nd choice
	elif(choice==2):
		print("\nAvailable time slots are: ")

	#prints available slots
		print("\n1.09:00-12:00 \n2.12:00-03:00 \n3.03:00-06:00 \n4.06:00-09:00")
		ch=int(input("\nEnter the desired time slot!!"))
		if ch==1:
			print("\nSlot successfully booked!! Please visit between 09:00-12:00")
		elif ch==2:
			print("\nSlot successfully booked!! Please visit between 12:00-03:00")
		elif ch==3:
			print("\nSlot successfully booked!! Please visit between 03:00-06:00")
		elif ch==4:
			print("\nSlot successfully booked!! Please visit between 06:00-09:00")
		else:
			print("Please enter a valid option!")
	else:
		print("Please enter a valid option!")
