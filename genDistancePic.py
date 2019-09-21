from PIL import Image
from resizeimage import resizeimage
img = Image.open('sample.jpg', 'r')
img.show()
img_w, img_h = img.size
#img = img.resize((20,20))
img = resizeimage.resize_contain(img, [20,20])
background = Image.new('RGBA', (img_w, img_h), (48,48,48))
bg_w, bg_h = background.size
offset = (50, 50)
background.paste(img, offset)
background.show()
#background.save('sample_dist.png')
