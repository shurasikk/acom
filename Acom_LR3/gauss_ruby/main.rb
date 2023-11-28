require 'ruby-vips'

im = Vips::Image.new_from_file("C:/Users/Asus/Documents/GitHub/acom/Acom_LR3/leaf.jpg")

im = im.gaussblur(4.0)

im.write_to_file("C:/Users/Asus/Documents/GitHub/acom/Acom_LR3/blurleaf.jpg")
