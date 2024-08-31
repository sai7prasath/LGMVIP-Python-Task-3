# Import the imageio library for image processing (version 3)
import imageio.v3 as iio

# Define separate lists to store filenames for different themes (more organized)
example_images = [
    'Gif Images/team-pic1.png',
    'Gif Images/team-pic2.png'
]
brawl_stars_images = [
    'Gif Images/FernierBuzz.jpeg',
    'Gif Images/BibiThor.jpeg',
    'Gif Images/CordilieusOdin.jpeg'
]
nature_images = [
    'Gif Images/Sakura.png',
    'Gif Images/SakuraDay.png',
    'Gif Images/SakuraNight.png'
]

# Create empty lists to store loaded images for each theme
e_images = []  # List for example images
bs_images = []  # List for Brawl Stars images
n_images = []  # List for nature images

# Get user input for theme selection
choice = int(input("""
Get the gif, by selecting the theme (^=^)
>> Try the below themes!
    - 1 (Brawl Stars theme✨ Gif)
    - 2 (Nature Gif)
Enter your choice (1/2/Anything): 
"""))

# Save the list of images as a GIF using imageio.imwrite
#  - 'Generated Gifs/filename.gif': Output filename with theme in folder
#  - image_list: List of images to be saved in the GIF (specific to choice)
#  - duration=500: Duration of each frame in milliseconds (controls speed)
#  - loop=0: Number of times the GIF loops (0 for infinite)
if choice == 1:
    for bs_image in brawl_stars_images:  # Use descriptive variable names
        image = iio.imread(bs_image)
        bs_images.append(image)
    iio.imwrite('Generated Gifs/brawlStars.gif', bs_images, duration=500, loop=0)
    print("Check out the brawlStars.gif file - that's just created!")
elif choice == 2:
    for n_image in nature_images:
        image = iio.imread(n_image)
        n_images.append(image)
    iio.imwrite('Generated Gifs/nature.gif', n_images, duration=500, loop=0)
    print("Check out the nature.gif file - that's just created!")
else:
    for filename in example_images:
        image = iio.imread(filename)
        e_images.append(image)
    iio.imwrite('Generated Gifs/team.gif', e_images, duration=500, loop=0)
    print("Check out the exampleImages.gif file - that's just created!")
    print("Try the other themes too!")
