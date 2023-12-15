from keras.models import load_model
import cv2
import numpy as np

# загрузка модели получившегося ранее персептрона
model = load_model("multilayer_perceptron.keras")

# загрузка тестируемого изображение в оттенках серого
image_path = "img/2.jpg"
img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# изменение размера изображения на 28x28 (аналогично размеру MNIST изображений)
img_cv = cv2.resize(img_cv, (28, 28))
# печать размера изображения (должен быть (28, 28))
print('Размер тестируемого изображения:',img_cv.shape)
# нормализация изображения
image = img_cv / 255.0
# перевод изображения в одномерный вектор
image = image.reshape(1, 784)

# получение предсказания модели для изображения
predictions = model.predict(image)
# вывод предсказанных вероятностей для каждого класса цифр
print(predictions)
# получение индекса класса с наибольшей вероятностью
predicted_class = np.argmax(predictions)

# вывод предсказанного класса(цифры)
print(f"Предсказанная цифра: {predicted_class}")