
# Скачивание статей с Habr в .docx файл.

***
### Требования
Для запуска проекта вам понадобятся следующие компоненты:

- Go 1.20
- Python 3.10.12
- Lib python-docx

***

1. Склонируйте репозиторий на вашу локальную машину:

   ```bash
   git clone https://github.com/Jhnvlglmlbrt/habr-download-articles

2. Перейдите в директорию проекта:

   ```bash
   cd habr-download-articles/cmd

3. Установите зависимости проекта:
    ```bash
    go get
    
4. Установите библиотеку docx:

    ```bash
    pip install python-docx

5. Запустите проект: 

    ```bash
    go run main.go && python3 converter/converter.py

