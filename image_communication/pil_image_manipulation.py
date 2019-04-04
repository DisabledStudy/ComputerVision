from PIL import Image
import imtools

working_path = 'one_session_dir\pil_image_manipulation'
imtools.clear_one_session_dir('pil_image_manipulation')

empire_path = 'data\empire.jpg'

pill_miniature = Image.open(empire_path)
pill_miniature.thumbnail((128,128))
pill_miniature.save(working_path + "\empire_min.jpg")

pill_cropped = Image.open(empire_path)
box = (100,100,100,400)
region = pill_cropped.crop(box)
region = region.transpose(Image.ROTATE_180)
pill_cropped.save(working_path + "\empire_cropped.jpg")

pill_rotated = Image.open(empire_path)
pill_rotated = pill_rotated.rotate(45)
pill_rotated.save(working_path + "\empire_rotated.jpg")

pill_resized = Image.open(empire_path)
pill_resized = pill_resized.resize((128,128))
pill_resized.save(working_path + "\empire_resized.jpg")


print("hi")