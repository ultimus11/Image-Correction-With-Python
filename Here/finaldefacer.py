from PIL import Image
import numpy as np

lips = Image.open("lips.png")
lips_set=()
firsttime=True
for mainy in range (1,5):
	for mainx in range (1,12):
		if firsttime==True:
			cordinate = x, y = 1,1
		lips_set=lips_set+lips.getpixel(cordinate)
		x+=1
		cordinate = x, y
		firsttime=False
	y+=1
	x=1
	cordinate = x, y
print(lips_set)
print(len(lips_set))
#length of tuple is 132

face_set=()
#face = Image.open("genny.jpg")
face = Image.open("test.png")
firsttime=True
horizontal=1
vertical=1
x=0
y=0
maximum=0
getcord=0,0
def check_intersection():
	global face_set
	global lips_set
	global maximum
	global x
	global y
	global getcord
	matches=0
	for i in range (1,132):
		if lips_set[i]==face_set[i]:
			matches+=1
	if matches>maximum:
		maximum=matches
	if matches>=11:
		getcord= cordinate
		print("heres the cordinates", getcord)
	print(matches)
	face_set=()
while y<60:
	while x < 37:
		for mainy in range (1,5):
			for mainx in range (1,12):
				cordinate = mainx+x, mainy+y
				face_set=face_set+face.getpixel(cordinate)
		check_intersection()
		x+=1
	y+=1
	x=0
print(face_set)
print(maximum)
print(getcord)
x4=getcord[0]
y4=getcord[1]
x1=x4-11
y1=y4-4
pixel_position=0
print("printing pixel position")
print(lips_set[pixel_position])
def correct_img():
	global x4,y4,x1,y1
	global pixel_position
	face1 = Image.open("defaced.png")
	for mainy in range (1,5):
		for mainx in range (1,12):
			cordinate = mainx+x1, mainy+y1
			face1.putpixel((cordinate), (lips_set[pixel_position],lips_set[pixel_position+1],lips_set[pixel_position+2]))
			pixel_position+=3
	face1.save("output.png")
print(lips_set)
correct_img()
