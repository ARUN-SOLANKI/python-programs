from PIL import Image , ImageEnhance , ImageFilter
import os
# img1 = Image.open('photo1.jpg')
# max_size = (250 , 250)
# img1.thumbnail(max_size)
# img1.save('photoeddited1.png')
# img1.show('photo1.png')

# for img in os.listdir():
#     if img.endswith('.jpg'):
#         img1 = Image.open(img)
#         filename , extention = os.path.splitext(img)
#         img1.save(f'{filename}.png')
# ---------- Image Enhance sharpness -------------
# img1 = Image.open('photo1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(50).save('eddited.jpg')

# ---------- Image Enhance color -------------
# img1 = Image.open('photo1.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save('eddited.jpg')

# ---------- Image Enhance brigtness -------------
# img1 = Image.open('photo1.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(0).save('eddited.jpg')

# ---------- Image Enhance Contrast -------------
# img1 = Image.open('photo1.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(3).save('eddited.jpg')

# ------------------ image filter blur ----------
img1 = Image.open('photo1.jpg')
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('eddited1.jpg')