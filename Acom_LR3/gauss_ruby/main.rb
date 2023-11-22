require 'rmagick'

# Загрузка изображения
input_image = Magick::Image.read('input.jpg').first

# Применение размытия Гаусса
blurred_image = input_image.gaussian_blur(0, 10)

# Сохранение размытого изображения
blurred_image.write('output.jpg')