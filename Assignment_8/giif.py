import os
import imageio
IMAGE=[]

file_list=sorted(os.listdir("Assignment_8/images"))
for file_name in file_list:
   file_path="Assignment_8/images/" + file_name
   imag=imageio.imread(file_path)
   IMAGE.append(imag)

imageio.mimsave("Assignment_8/my_out_put.gif",IMAGE)
