from PIL import Image
import os

list = os.listdir("source")

for f in list:
	im = Image.open("source/"+f)
	im.save("target/"+f, dpi=(96,96))
	
print("Converting completed")
