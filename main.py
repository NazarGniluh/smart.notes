from PyQt5. QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(800, 500)
mainLine = QHBoxLayout()
ans = QLabel("Дякую")
hls = QLabel("Гроші в Гаманці")
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







window.setLayout(mainLine)
window.show()
app.exec()
