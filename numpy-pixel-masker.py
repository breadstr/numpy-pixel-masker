from PIL import Image
import os
import numpy

def changeBackroundColor(image,img_dir,trgt_clr,new_clr,out_dir):
    """
    Takes a image as input and a two colors the one to replace and the new color.

    Param:
        image (str): Name of the image to edit
        ing_dir (str): Directory of image
        trgt_clr (tuple): Backround color to replace in RGB
        new_clr (tuple): New color for the backround in RGB
        out_dir (str): Output directory for the new image

    Returns:
        None    
    """

    full_img = os.path.join(img_dir,image)

    img = Image.open(full_img)
    img_array = numpy.array(img)

    mask = numpy.all(img_array == trgt_clr, axis=-1)
    img_array[mask] = new_clr

    result_img = Image.fromarray(img_array)
    result_img.save(os.path.join(out_dir,image))

if __name__ == "__main__":
    target_image = "FULL FILE NAME HERE"
    target_image_dir = r"IMAGE DIRECTORY HERE"
    target_colour = (255,255,255) #HEX value of target coulour eg; (255,255,255) = white
    new_colour = (0,0,0) #HEX value of new colour eg; (0,0,0) = black
    output_directory = r"OUTPUT DIRECTORY HERE"


    changeBackroundColor(target_image,target_image_dir,target_colour,new_colour,output_directory)



