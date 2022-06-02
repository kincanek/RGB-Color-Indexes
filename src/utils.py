import cv2
import numpy as np

class index_image_RGB():
    def __init__(self,image, space = 'BGR' , gpu = False):
        """_summary_

        Args:
            image (_type_): _description_
            space (str, optional): _description_. Defaults to 'BGR'.
            gpu (bool, optional): _description_. Defaults to False.
        """
        self.img = np.array(image)
        self.norm_img = np.array(image) / 255.0
        
        if space == 'BGR':
            self.B_ = self.norm_img[:,:,0]
            self.G_ = self.norm_img[:,:,1]
            self.R_ = self.norm_img[:,:,2]
            
    def ExG(self):
        """ Exceso de verde

        Returns:
            _type_: _description_
        """
        dif = self.R_ + self.G_ + self.B_
        r = self.R_ / dif
        g = self.G_ / dif
        b = self.B_ / dif
        return 2 * g - r - b