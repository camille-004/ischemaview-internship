from PIL import Image

img = Image.open('/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files/106c_227_4980_mtt_1.jpg')
resized_img = img.resize((240, 470))
# resized_img.save("106c_227_4980_mtt_1_resized.jpg", "JPEG", optimize = True)
resized_img.show()