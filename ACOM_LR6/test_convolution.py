# -*- coding: cp1251 -*-
import cv2
import numpy as np
from keras.models import load_model

# загрузка модели получившейся ранее свёрточной нейронной сети
model = load_model('cnn_model.keras')

# загрузка тестируемого изображение в оттенках серого
image_path = 'img/1.jpg'
img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# изменение размера изображения на 28x28 (аналогично размеру MNIST изображений)
img_cv = cv2.resize(img_cv, (28, 28))
# печать размера изображения (должен быть (28, 28))
print('Размер тестируемого изображения:',img_cv.shape)
# нормализация изображения
image = img_cv / 255.0
# перевод изображения в формат, ожидаемый моделью (1, 28, 28, 1)
image = image.reshape(1, 28, 28, 1)

# получение предсказания модели для изображения
predictions = model.predict(image)
# вывод предсказанных вероятностей для каждого класса цифр
print(predictions)
# получение индекса с максимальной вероятностью, который представляет предсказанную цифру
predicted_class = np.argmax(predictions)

# вывод предсказанного класса(цифры)
print(f"Предсказанная цифра: {predicted_class}")