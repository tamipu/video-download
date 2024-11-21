from PIL import Image, ImageFilter, ImageEnhance
import os

class ImageEditor:
    def __init__(self, image_path):
        """ Initialize with the image file path. """
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()  

    def show_image(self):
        """ Display the image. """
        self.image.show()

    def save_image(self, save_path):
        """ Save the current image to a file. """
        self.image.save(save_path)
        print(f"Image saved as {save_path}")

    def resize_image(self, width, height):
        """ Resize the image to given width and height. """
        self.image = self.image.resize((width, height))
        print(f"Image resized to {width}x{height}")

    def crop_image(self, left, top, right, bottom):
        """ Crop the image using the given coordinates. """
        self.image = self.image.crop((left, top, right, bottom))
        print(f"Image cropped to left={left}, top={top}, right={right}, bottom={bottom}")

    def rotate_image(self, degrees):
        """ Rotate the image by the given degrees. """
        self.image = self.image.rotate(degrees)
        print(f"Image rotated by {degrees} degrees")

    def apply_filter(self, filter_type="BLUR"):
        """ Apply a filter to the image. """
        filter_dict = {
            "BLUR": ImageFilter.BLUR,
            "CONTOUR": ImageFilter.CONTOUR,
            "DETAIL": ImageFilter.DETAIL,
            "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
        }
        
        filter_func = filter_dict.get(filter_type.upper(), ImageFilter.BLUR)
        self.image = self.image.filter(filter_func)
        print(f"Applied {filter_type} filter")

    def enhance_brightness(self, factor):
        """ Enhance the image's brightness. """
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
        print(f"Brightness enhanced by a factor of {factor}")

    def reset_image(self):
        """ Reset the image to its original state. """
        self.image = self.original_image.copy()
        print("Image reset to original state")

# Example usage:
if __name__ == "__main__":
    editor = ImageEditor("path_to_your_image.jpg")
    editor.show_image()

    # Perform image operations
    editor.resize_image(800, 600)
    editor.rotate_image(45)
    editor.apply_filter("DETAIL")
    editor.enhance_brightness(1.2)
    editor.save_image("edited_image.jpg")
    editor.reset_image()
    editor.save_image("reset_image.jpg")
