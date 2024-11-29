import imageio.v3 as iio

filenames = [r'C:\Python wth harry\codedex\kitty frog gif\f1.png',
             r'C:\Python wth harry\codedex\kitty frog gif\f2.png',
             r'C:\Python wth harry\codedex\kitty frog gif\f3.png', 
             r'C:\Python wth harry\codedex\kitty frog gif\f4.png',
             r'C:\Python wth harry\codedex\kitty frog gif\f5.png']

images =[]
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('frog.gif', images, duration= 500, loop= 0 )
print("GIF successfully created!")