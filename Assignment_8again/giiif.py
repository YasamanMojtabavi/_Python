import os
import imageio

file_list=os.listdir("D:\python\Python\Assignment_8again\images")

IMAGES=[]
for file_name in file_list:
    file_path="D:\python\Python\Assignment_8again\images/" + file_name
    image=imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("D:\python\Python\Assignment_8again\my_output.gif",IMAGES)
