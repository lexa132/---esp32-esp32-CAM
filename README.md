Файлы для esp32:
* main.py
* MX1508.py
* tcs34725.py
* BLEUART.py (установить своё имя)
* ble_advertising.py

esp32 управляется через приложение bluefruit

Файлы для esp32-CAM:
* CameraWebServer.ino (установить своё имя)
* camera_pins.h
* camera_index.h
* app_httpd.cpp
* ci.json

esp32-CAM создает точку доступа, к которой необходимо подключиться внешним устройством.
На внешнем устройстве изображение получается в OBS (Open Broadcaster Software) и снова отображается в виртуальной камере приложения.
Программа, для чтения аруко-кодов:
* detect_aruco_video.py
Файл запускается в среде Spyder;
Также, через conda необходимо скачать библиотеки cv2 и imutils
