from PyQt5. QtWidgets import *

import json

try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    notes = {}

app = QApplication([])
app.setStyleSheet("""
            QWidget {
                background: #FFEF00;
            }
            
            QPushButton
            {
                background-color:  #BCB008;
                border: outset;
                font: Roboto;
                min-width: 6;
                padding: 6;
            }
            
        """)


window = QWidget()
window.resize(800, 500)
mainLine = QHBoxLayout()
ans = QLabel("Мої Записи")
hls = QLabel("ПОШУК ПО ТЕГУ")
smart = QPushButton("Створити запис")
samsung = QPushButton("Видалити запис")
koold = QPushButton("Зберегти запис")
samsi = QPushButton("Відкріпити до запиту")
sims = QPushButton("Додати до запису")
poco = QPushButton("Шукати запит по тегу")
text = QTextEdit()
old = QListWidget()
hoold = QListWidget()


Onsr = QVBoxLayout()
Onsr.addWidget(text)
mainLine.addLayout(Onsr)



Amrs = QVBoxLayout()
Amrs.addWidget(ans)
Amrs.addWidget(old)

Soon = QHBoxLayout()
Soon.addWidget(smart)
Soon.addWidget(samsung)
Amrs.addLayout(Soon)

Amrs.addWidget(koold)
Amrs.addWidget(hls)
Amrs.addWidget(hoold)
Amrs.addWidget(poco)

mainLine.addLayout(Amrs)


Soon23 = QHBoxLayout()
Soon23.addWidget(samsi)
Soon23.addWidget(sims)
Amrs.addLayout(Soon23)


def del_note():
    if old.selectedItems():
        key = old.selectedItems()[0].text()
        notes.pop(key)
        hoold.clear()
        old.clear()
        text.clear()
        old.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")

samsung.clicked.connect(del_note)

def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
    key = old.selectedItems()[0].text()
    print(key)
    text.setText(notes[key]["текст"])
    hoold.clear()
    hoold.addItems(notes[key]["теги"])

old.itemClicked.connect(show_note)

def save_note():
    if old.selectedItems():
        key = old.selectedItems()[0].text()
        notes[key]["текст"] = text.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print("Замітка для збереження не вибрана!")

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати запис", "Назва запис:")
    if ok and note_name != "":
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
        old.clear()
        text.clear()
        old.addItems(notes)


        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)



koold.clicked.connect(save_note)
old.addItems(notes)
smart.clicked.connect(add_note)
window.setLayout(mainLine)
window.show()
app.exec()
