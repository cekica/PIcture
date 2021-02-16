# Picture generator library :
#
# Module dedicated to the generation of pictures adapted for the pi computation.
# Dependance : numpy, scipy
# Import package :
import numpy as np
import scipy.misc as smp
from PIL import Image

""" Generator Engin :
    Class will manage the picture generation

"""
class GeneratorEngine:

    """ Initialisation of the generator.
        Width : width of the generated pictures.
        height : height of the generated pictures.
        tips : number of generated pictures will be int(len(source)/(width*height))
    """

    def __init__(self, width, height, sourcefile):
        self.width = width
        self.height = height
        tmp = self.read_pi_file(sourcefile)
        tmp = tmp.replace("3.", "")
        self.source = tmp
        self.encoded_source = tmp

    def read_pi_file(self, file):
        res =""
        f = open(file,"r")
        res = f.read()
        return res
    """ This method allow to convert pi decimal string source to the binaries string.
        This allow to artificially increase the length of the source string and generate more picture.
        
    """
    def encode_binaries(self):
        res = ""
        for digit in self.source:
            if digit.isnumeric():
                d = int(digit)
                b = bin(d)
                res =  res + str(b)
        self.encoded_source = res

    """ Set the picture output directory 
    """
    def set_output_dir(self, output):
        self.out_file = output

    """ Set the file name template without png extension. Free text variable
        Example : image-of-pi or picture
    """
    def set_output_name_format(self, template):
        self.template_name = template


    """ Run the engine one time in black and white mode
    """
    def run_one_shot_bw(self):
        img = PI_image(self.out_file+"/"+self.template_name+"-bw.png", self.encoded_source)
        img.setSize(self.width, self.height)
        if img.have_Enough_fdta_for_BW_mode() :
            img.save_picture_BW()

class PI_image:

    # Initialisation of the PI_Image
    def __init__(self, output, source):
        self.output = output
        self.source = source
        self.width = 0
        self.height = 0

    # Set size of the picture
    def setSize(self, width, height):
        self.width = width
        self.height = height

    """ Method to check if enough data is available to generate the picture in Black and white mode. 
    """
    def have_Enough_fdta_for_BW_mode(self):
        source = str(self.source)

        if self.width != 0 and self.height != 0:
            tot = self.width * self.height
            if len(source) > tot:
                return True
        return False

    """ Method to check if enough data is available to generate the picture in Color mode.
        This method request 3 time more data than black and white mode.
    """
    def have_Enough_Data_for_color_mode(self):
        source = str(self.source)
        if self.width != 0 and self.height != 0:
            tot = self.width * self.height
            if len(source) > tot:
                return True
        return False

    """ Methode to create a picture pixel by pixel and save it in output folder.
        This methode is perfect for binaries input source and generate bacl and white picture.
    """
    def save_picture_BW(self):

        pixel= 0
        data = np.zeros( (self.width, self.height, 3), dtype=np.uint8)
        print(self.source)
        for y in range(0, self.height):
            for x in range(0, self.width):
                pixel = self.source[x+y]
                if pixel.isnumeric():
                    pixel = int(pixel)
                else:
                    pixel = 0

                color = (1 - pixel)*255
                data[x, y] = [color, color, color]

        export = Image.fromarray(data)
        export.save(self.output)


    """ Methode to create a picture pixel by pixel and save it in output folder.
        This methode is perfect for binaries input source and generate bacl and white picture.
    """
    def save_picture(self):

        pixel= 0
        data = np.zeros( (self.width, self.height, 3), dtype=np.uint8)
        print(self.source)
        for y in range(0, self.height):
            for x in range(0, self.width) :
                color = (1 - int(self.source[pixel]))*255
                data[x , y] = [color, color, color]

        export = Image.fromarray(data)
        export.save(self.output)