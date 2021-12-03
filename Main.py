import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, \
    QLineEdit
from Sorts_1 import Sorts1 as Sort1
from Sorts_2 import Sorts2 as Sort2
from Description import description


class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.values = []
        self.colors = {}
        self.uiSize = {
            'width': 1200,
            'height': 500,
        }
        self.graphUIConfig = {
            'start': {'x': 10, 'y': 110},
            'end': {'x': self.uiSize['width'] - 310, 'y': self.uiSize['height'] - 10},
            'interval': 50,  # 막대 너비의 %단위
            'color': [70, 180, 50],
            'background': [0, 0, 0],
        }
        self.drawConfig = {
            'interval': 50,  # ui 갱신 단위, ms
        }
        self.drawList = []

        self.UI = {}

        # timer: interval 간격으로 drawUI를 호출
        self.timer = QTimer()
        self.timer.start(self.drawConfig['interval'])
        self.timer.timeout.connect(self.drawUI)

        self.sort1 = Sort1()
        self.sort2 = Sort2()

        self.initUI()
        self.setEvents()

    def initUI(self):

        self.setGeometry(300, 300, self.uiSize['width'], self.uiSize['height'])
        self.setFixedSize(self.uiSize['width'], self.uiSize['height'])
        self.setWindowTitle('ADProject - Team F')
        self.mainBox = QVBoxLayout()
        self.mainBox.addStretch(0)

        inputBox = QHBoxLayout()
        self.UI['startEdit'] = QLineEdit()
        self.UI['startEdit'].setPlaceholderText("min : 1")
        self.UI['startEdit'].setValidator(QIntValidator(1, 300, self))
        self.UI['endEdit'] = QLineEdit()
        self.UI['endEdit'].setPlaceholderText("max : 300")
        self.UI['endEdit'].setValidator(QIntValidator(1, 300, self))
        for widget in [
            QLabel('Start:', self), self.UI['startEdit'],
            QLabel('End:', self), self.UI['endEdit'],
        ]:
            inputBox.addWidget(widget)

        buttonBox1 = QHBoxLayout()
        self.UI['bubbleButton'] = QPushButton("Bubble")
        self.UI['quickButton'] = QPushButton("Quick")
        self.UI['heapButton'] = QPushButton("Heap")
        self.UI['insertionButton'] = QPushButton("Insertion")
        self.UI['mergeButton'] = QPushButton("Merge")

        buttonBox1.addWidget(self.UI['bubbleButton'])
        buttonBox1.addWidget(self.UI['quickButton'])
        buttonBox1.addWidget(self.UI['heapButton'])
        buttonBox1.addWidget(self.UI['insertionButton'])
        buttonBox1.addWidget(self.UI['mergeButton'])

        buttonBox2 = QHBoxLayout()
        self.UI['countingButton'] = QPushButton("Counting")
        self.UI['introButton'] = QPushButton("Intro")
        self.UI['cocktailButton'] = QPushButton("Cocktail")
        self.UI['selectionButton'] = QPushButton("Selection")
        self.UI['bogoButton'] = QPushButton("Bogo")

        buttonBox2.addWidget(self.UI['countingButton'])
        buttonBox2.addWidget(self.UI['introButton'])
        buttonBox2.addWidget(self.UI['cocktailButton'])
        buttonBox2.addWidget(self.UI['selectionButton'])
        buttonBox2.addWidget(self.UI['bogoButton'])

        textBoxLayout = QHBoxLayout()
        emptyBox = QWidget()

        self.UI['text'] = QTextEdit()
        self.UI['text'].setReadOnly(True)
        textBoxLayout.addWidget(emptyBox, self.graphUIConfig['end']['x'] - self.graphUIConfig['start']['x'] + 20)
        textBoxLayout.addWidget(self.UI['text'], 300)

        self.mainBox.addLayout(inputBox)
        self.mainBox.addLayout(buttonBox1)
        self.mainBox.addLayout(buttonBox2)
        self.mainBox.addLayout(textBoxLayout, 1)
        self.setLayout(self.mainBox)
        self.show()

    def setText(self, text):
        self.UI['text'].clear()
        self.UI['text'].append(text)

    def setEvents(self):
        self.UI['bubbleButton'].clicked.connect(self.bubble)
        self.UI['countingButton'].clicked.connect(self.counting)
        self.UI['bogoButton'].clicked.connect(self.bogo)
        self.UI['cocktailButton'].clicked.connect(self.cocktail)
        self.UI['selectionButton'].clicked.connect(self.selection)
        self.UI['introButton'].clicked.connect(self.intro)
        self.UI['insertionButton'].clicked.connect(self.insert)
        self.UI['heapButton'].clicked.connect(self.heap)
        self.UI['quickButton'].clicked.connect(self.quick)
        self.UI['mergeButton'].clicked.connect(self.merge)

    def getRange(self):
        start = int(self.UI['startEdit'].text().strip() if self.UI['startEdit'].text().strip()!="" else 1)
        end = int(self.UI['endEdit'].text().strip() if self.UI['endEdit'].text().strip()!="" else 300)
        if start < 1:
            start = 1
        elif start > 299:
            start = 299

        if end > 300:
            end = 300
        elif end < 1:
            end = 1

        if end < start:
            start, end = end, start

        self.UI['startEdit'].setText(str(start))
        self.UI['endEdit'].setText(str(end))

        return {'start': start, 'end': end}

    def bubble(self):
        range = self.getRange()
        self.setText(description['bubbleSort'])
        self.drawList = self.sort2.bubbleSort(range['start'], range['end'])

    def merge(self):
        range = self.getRange()
        self.setText(description['mergeSort'])
        self.drawList = self.sort2.mergeSort(range['start'], range['end'])

    def counting(self):
        range = self.getRange()
        self.setText(description['countingSort'])
        self.drawList = self.sort1.counting_sort(range['start'], range['end'])

    def bogo(self):
        range = self.getRange()
        self.setText(description['bogoSort'])
        self.drawList = self.sort1.bogo_sort(range['start'], range['end'])

    def cocktail(self):
        range = self.getRange()
        self.setText(description['cocktailSort'])
        self.drawList = self.sort1.cocktail_sort(range['start'], range['end'])

    def selection(self):
        range = self.getRange()
        self.setText(description['selectionSort'])
        self.drawList = self.sort1.selection_sort(range['start'], range['end'])

    def intro(self):
        range = self.getRange()
        self.setText(description['introSort'])
        self.drawList = self.sort1.intro_sort(range['start'], range['end'])

    def insert(self):
        range = self.getRange()
        self.setText(description['insertSort'])
        self.drawList = self.sort1.insertion_sort(range['start'], range['end'])

    def heap(self):
        range = self.getRange()
        self.setText(description['heapSort'])
        self.drawList = self.sort1.heap_sort(range['start'], range['end'])

    def quick(self):
        range = self.getRange()
        self.setText(description['quickSort'])
        self.drawList = self.sort1.quick_sort(range['start'], range['end'])

    # update시 self.values로 막대를 그림
    def paintEvent(self, event):

        graphUI = QPainter()
        graphUI.begin(self)

        graphUI.setBrush(QColor(
            self.graphUIConfig['background'][0],
            self.graphUIConfig['background'][1],
            self.graphUIConfig['background'][2],
        ))
        graphUI.drawRect(
            self.graphUIConfig['start']['x'],
            self.graphUIConfig['start']['y'],
            self.graphUIConfig['end']['x'] - self.graphUIConfig['start']['x'],
            self.graphUIConfig['end']['y'] - self.graphUIConfig['start']['y']
        )

        if len(self.values) < 1 or max(self.values) == 0:
            graphUI.end()
            return

        # 막대 색상(RGB)
        graphUI.setBrush(QColor(
            self.graphUIConfig['color'][0],
            self.graphUIConfig['color'][1],
            self.graphUIConfig['color'][2],
        ))

        # 막대 너비 - 간격과 양끝 여백을 고려하여 자동계산
        width = self.graphUIConfig['end']['x'] - self.graphUIConfig['start']['x']
        width /= len(self.values) + (len(self.values) + 1) * self.graphUIConfig['interval'] / 100

        # 막대 높이 - 최대값 = 높이 100% 가 되도록 비율 설정
        height = (self.graphUIConfig['end']['y'] - self.graphUIConfig['start']['y']) / (max(self.values) + 1)

        # 막대 배치
        for i in range(0, len(self.values)):
            # 지정된 색이 있을경우 변경
            if self.colors.get(i) is not None:
                graphUI.setBrush(QColor(self.colors[i][0], self.colors[i][1], self.colors[i][2]))
            # 막대 그리기
            graphUI.drawRect(
                round(self.graphUIConfig['start']['x'] + (width * (
                        (1 + self.graphUIConfig['interval'] / 100) * i + self.graphUIConfig['interval'] / 100))),
                self.graphUIConfig['end']['y'],
                round(width),
                - round(height * self.values[i])
            )
            # 색상 초기화
            graphUI.setBrush(QColor(
                self.graphUIConfig['color'][0],
                self.graphUIConfig['color'][1],
                self.graphUIConfig['color'][2],
            ))

        graphUI.end()

    # drawList 순서대로 막대 갱신
    def drawUI(self):
        if len(self.drawList) < 1: return
        if 'error' in self.drawList[0]:
            self.setText(self.drawList[0]['error'])
        if 'values' in self.drawList[0] and 'color' in self.drawList[0]:
            self.values = list(self.drawList[0]['values'])
            self.colors = self.drawList[0]['color']
            self.drawList.pop(0)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    # sort1 = Sort1()
    # ui.drawList = Sort1.bubbleSort(sort1, 1, 20)
    sys.exit(app.exec_())
