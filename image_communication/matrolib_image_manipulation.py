from PIL import Image
from pylab import *
import imtools

im = array(Image.open("data\empire.jpg"))
imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x,y,'r*')
plot(x[:2],y[:2])

title('Plotting:"empire.jpg"')

working_path = 'one_session_dir\pil_image_manipulation'
imtools.clear_one_session_dir('matlib_image_manipulation')


gray()
imgrey = array(Image.open("data\empire.jpg").convert('L'))
contour(imgrey, origin='image')
axis('equal')
axis('off')

figure()
hist(imgrey.flatten(),128)

show()