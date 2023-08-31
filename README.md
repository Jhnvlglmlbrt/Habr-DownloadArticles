
# Скачивание статей с Habr в .docx файл.

***
### Требования
Для запуска проекта вам понадобятся следующие компоненты:

- Go 1.21
- Python 3.10.12
- Библиотека Python docx

***

1. Склонируйте репозиторий на вашу локальную машину:

   ```bash
   git clone https://github.com/Jhnvlglmlbrt/Habr-DownloadArticles

2. Перейдите в директорию проекта:

   ```bash
   cd Habr-DownloadArticles/cmd

3. Установите зависимости проекта:
    ```bash
    go get
    
4. Установите библиотеку docx:

    ```bash
    pip install python-docx

5. Запустите проект: 

    ```bash
    go run main.go && python3 converter/converter.py

