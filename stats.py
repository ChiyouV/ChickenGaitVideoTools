#Count the number of png images in a folder
import os

def count_png(folder):
    png_count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.png'):
                png_count += 1
    return png_count

#Count the number of png images in each folder
side_count = count_png("frames/side")
back_count = count_png("frames/back")
top_count = count_png("frames/top")

#Print the number of png images in each folder
print("Side: " + str(side_count))
print("Back: " + str(back_count))
print("Top: " + str(top_count))