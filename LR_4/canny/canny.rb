require 'vips'

# Пример использования
input_image_path = 'C:/Users/Asus/Documents/GitHub/acom/LR_4/album.png'
image = Vips::Image.new_from_file(input_image_path)

canny_edges = image.canny

# Сохранение результата
canny_edges.write_to_file('canny_edges.png')

#C:/Users/Asus/Documents/GitHub/acom/LR_4/album.png