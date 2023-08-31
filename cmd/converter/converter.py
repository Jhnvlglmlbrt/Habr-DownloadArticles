from docx import Document
from docx.shared import Pt
import re


# Открываем файл .txt и читаем его содержимое
with open('/mnt/d/ProjectsGo/WebScraper/documents/article.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

# Убираем лишние пробелы между строками (3 и более заменяем на 2)
txt_content = re.sub(r'(\n\s{3,})', '\n\n  ', txt_content)

# Создаем новый документ .docx и добавляем текст
doc = Document()
first_paragraph = doc.add_paragraph(txt_content.split('\n', 1)[0])
run = first_paragraph.runs[0]
run.font.size = Pt(18)  # 1.5rem 
run.font.name = 'Fira Sans'

# Добавляем оставшийся текст как обычно
doc.add_paragraph(txt_content[len(first_paragraph.text) + 1:])


# Сохраняем документ в файл .docx
doc.save(r'/mnt/d/ProjectsGo/WebScraper/documents/output.docx')
