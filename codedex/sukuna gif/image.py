import imageio.v3  as iio 

filenames = [r'C:\Python wth harry\codedex\gif\s1.png', r'C:\Python wth harry\codedex\gif\s2.png']

images = []
for filename in filenames:
    images.append(iio.imread(filename))
    
iio.imwrite('sakuna.gif', images, duration=500, loop=0)  # you can adjust duration as needed
print("GIF successfully created!")

