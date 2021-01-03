from PIL import Image
import numpy as np

#data = open('lipsdata.txt','a')
ei = Image.open("lips.jpg")
eiar = np.array(ei)
eiarl = str(eiar.tolist())
#data.write(eiarl)

sa=()
face = Image.open("genny.jpg")
'''
cordinate = x, y = 150, 59
sa=sa+face.getpixel(cordinate)

cordinate = x, y = 152, 69
sa=sa+face.getpixel(cordinate)

cordinate = x, y = 151, 59
sa=sa+face.getpixel(cordinate)

print(sa)
'''
firsttime=True
for mainy in range (1,47):
	for mainx in range (1,108):
		if firsttime==True:
			cordinate = x, y = 1,1
		sa=sa+face.getpixel(cordinate)
		x+=1
		cordinate = x, y
		firsttime=False
	y+=1
	x=1
	cordinate = x, y
print(y)
print(x)
print(sa)
		