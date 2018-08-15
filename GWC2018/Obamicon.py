from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
black = (0, 0 ,0)
lightGrey = (164, 166, 168)
darkGrey = (106, 107, 109)
white = (250, 250, 250)
orange = (255, 234, 0)
pink = (255, 0, 102)

green = (25, 253, 0)

# Import image.
my_image = Image.open("Hillary.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.
recolored2 = []
recolored3 = []
#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
#makes hilary into a list of pixel values
#add up to get intensity values
def image1():
    for i in image_list:
        intensity = i[0] + i[1] + i[2]
        if(intensity <= 182):
            recolored.append(darkBlue)
        if(182 < intensity) and (intensity <= 364):
            recolored.append(red)
        if(364 < intensity) and (intensity < 546):
            recolored.append(lightBlue)
        if(intensity >= 546):
            recolored.append(yellow)
    # Create a new image using the recolored list. Display and save the image.
    new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
    new_image.putdata(recolored) #Adds the data from the recolored list to the image.
    new_image.show() #show the new image on the screen
    new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

def image2():
    for i in image_list:
        intensity = i[0] + i[1] + i[2]
        if(intensity <= 175):
            recolored2.append(black)
        if(182 < intensity) and (intensity <= 350):
            recolored2.append(darkGrey)
        if(350 < intensity) and (intensity < 500):
            recolored2.append(lightGrey)
        if(intensity >= 500):
            recolored2.append(white)
    newer_image = Image.new("RGB", my_image.size)
    newer_image.putdata(recolored2)
    newer_image.show()
    newer_image.save("recolored2.jpg", "jpeg")

def main():
    image1()
    image2()

if __name__ == "__main__":
    main()
