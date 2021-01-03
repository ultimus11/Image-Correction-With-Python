from PIL import Image
import numpy as np
lips = Image.open("lips.png")
lips_set=()
firsttime=True
for mainy in range (1,47):
	for mainx in range (1,108):
		if firsttime==True:
			cordinate = x, y = 1,1
		lips_set=lips_set+lips.getpixel(cordinate)
		x+=1
		cordinate = x, y
		firsttime=False
	y+=1
	x=1
	cordinate = x, y
x4=312
y4=305
x1=x4-107
y1=y4-46
pixel_position=0
def correct_img():
	global x4,y4,x1,y1
	global pixel_position
	face3 = Image.open("defaced.png")
	for mainy in range (1,47):
		for mainx in range (1,108):
			cordinate = mainx+x1, mainy+y1
			face3.putpixel((cordinate), (lips_set[pixel_position],lips_set[pixel_position+1],lips_set[pixel_position+2]))
			pixel_position+=3
	face3.save("output1.png")
correct_img()