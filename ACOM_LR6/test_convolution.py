# -*- coding: cp1251 -*-
import cv2
import numpy as np
from keras.models import load_model

# �������� ������ ������������ ����� ��������� ��������� ����
model = load_model('cnn_model.keras')

# �������� ������������ ����������� � �������� ������
image_path = 'img/1.jpg'
img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# ��������� ������� ����������� �� 28x28 (���������� ������� MNIST �����������)
img_cv = cv2.resize(img_cv, (28, 28))
# ������ ������� ����������� (������ ���� (28, 28))
print('������ ������������ �����������:',img_cv.shape)
# ������������ �����������
image = img_cv / 255.0
# ������� ����������� � ������, ��������� ������� (1, 28, 28, 1)
image = image.reshape(1, 28, 28, 1)

# ��������� ������������ ������ ��� �����������
predictions = model.predict(image)
# ����� ������������� ������������ ��� ������� ������ ����
print(predictions)
# ��������� ������� � ������������ ������������, ������� ������������ ������������� �����
predicted_class = np.argmax(predictions)

# ����� �������������� ������(�����)
print(f"������������� �����: {predicted_class}")