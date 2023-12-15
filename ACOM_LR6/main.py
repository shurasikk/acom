# -*- coding: cp1251 -*-
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
import time

start_time = time.time()

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

x_train = x_train.astype('float32')  # из uint8
x_test = x_test.astype('float32')

x_train /= 255  # нормализация пикселей
x_test /= 255

num_classes = 10

y_train = keras.utils.to_categorical(y_train, num_classes)  # метки -> бинарные векторы
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_classes, activation='softmax'))  # вектор значений -> вероятностное распределение

model.compile(loss='categorical_crossentropy',  # Используется для задачи многоклассовой классификации, где каждый пример принадлежит к одному из нескольких классов. Эта функция минимизирует кросс-энтропию между предсказанными вероятностями и фактическими классами.
              optimizer='adam',                 # опр-т обновление весовых коэфф-ов модели в процессе обучения
              metrics=['accuracy'])             # исп-ся для оценки производительности модели

# обучение
history = model.fit(x_train, y_train,
                    batch_size=128,
                    epochs=15,
                    verbose=1,  # вывод информации о потерях, метриках и прогресс-бар
                    validation_data=(x_test, y_test))  # тестовые данные, будут использоваться для проверки производительности модели во время обучения

model.save("multilayer_perceptron.keras")

print('==============================================================')

# оценка потерь и точности модели
score = model.evaluate(x_test, y_test, verbose=0)
print('Потери на тестовых данных:', score[0])
print('Точность модели на тестовых данных:', score[1])

# подсчёт процента корректной работы на тестовой базе
accuracy = score[1]
percent_correct = accuracy * 100
print('Процент корректной работы:', percent_correct)

end_time = time.time()

print('Затраченное время:', end_time - start_time)