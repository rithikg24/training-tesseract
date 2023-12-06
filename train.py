import os
import subprocess

font_properties="font_properties.txt"
lang="eng"
font="ocrb"

# Creating font_properties.txt
fontPropFile = open(font_properties, "w")
fontPropFile.write("font 0 0 0 0 0")
fontPropFile.close()


files = os.listdir()
jpgs = [x for x in files if x.endswith('.jpg')]
boxes = [x for x in files if x.endswith('.box')]
trainfiles = list(zip(jpgs, boxes))

# Generating .tr files
for image,box in trainfiles:
    os.system(f"tesseract {image} {image[:-4]} nobatch box.train")
print("\nGenerated .tr files\n")

# Generating unicharset file
unichar="unicharset_extractor "
for image,box in trainfiles:
    unichar=unichar+box+" "

subprocess.run(unichar,shell=True)
print("\nGenerated unicharset files\n")


# Generating shapetable,pffmtable,inttemp,normproto file
trFiles = [x for x in os.listdir() if (x.endswith('.tr'))]
print(trFiles)

shapetable_command = f"shapeclustering -F {font_properties} -U unicharset -O {font}.unicharset "
pffmtable_command = f"mftraining -F {font_properties} -U unicharset -O {font}.unicharset "
np_command = f"cntraining "

for filePath in trFiles:
    shapetable_command=shapetable_command+filePath+" "
    pffmtable_command = pffmtable_command+filePath+" "
    np_command = np_command+filePath+" "

# print(shapetable_command)
subprocess.run(shapetable_command,shell=True)
print("\nGenerated shapetable file\n")

# print(pffmtable_command)
subprocess.run(pffmtable_command,shell=True)
print("\nGenerated pffmtable,inttemp file\n")

# print(np_command)
subprocess.run(np_command,shell=True)
print("\nGenerated normproto file\n")

# Renaming the generated files
os.rename("inttemp",f"{font}.inttemp")
os.rename("normproto", f"{font}.normproto")
os.rename("pffmtable", f"{font}.pffmtable")
os.rename("shapetable",f"{font}.shapetable")

subprocess.run(f"combine_tessdata {font}.",shell=True)
print(f"\nGenerated {font}.traineddata file")