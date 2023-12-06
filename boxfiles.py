import os

lang = "eng"           	# Change according to the dataset
font = "ocrb" 	        # Change according to the dataset

images=[x for x in os.listdir() if x.endswith(('.jpg','.png'))]
for image in images:
    os.system(f"tesseract {image} {image[:-4]} batch.nochop makebox")
