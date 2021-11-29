import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QTextEdit, \
    QGridLayout, QLineEdit
from Sorts_1 import Sorts1 as Sort1


class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.values = []
        self.colors = {}
        self.graphUIConfig = {
            'start': {'x': 10, 'y': 110},
            'end': {'x': 790, 'y': 490},
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

        self.initUI()
        self.setEvents()

    def initUI(self):

        self.setGeometry(300, 300, 800, 500)
        self.setFixedSize(800,500)
        self.setWindowTitle('ADProject - Team F(20151334,')
        self.mainBox = QVBoxLayout()
        self.mainBox.addStretch(0)

        inputBox = QHBoxLayout()
        self.UI['startEdit'] = QLineEdit()
        self.UI['endEdit'] = QLineEdit()
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

        # 임시 비활성화
        self.UI['quickButton'].setDisabled(True)
        self.UI['heapButton'].setDisabled(True)
        self.UI['insertionButton'].setDisabled(True)
        self.UI['mergeButton'].setDisabled(True)

        self.mainBox.addLayout(inputBox)
        self.mainBox.addLayout(buttonBox1)
        self.mainBox.addLayout(buttonBox2)
        self.mainBox.addStretch(1)
        self.setLayout(self.mainBox)
        self.show()

    def setEvents(self):
        self.UI['bubbleButton'].clicked.connect(self.bubble)
        self.UI['countingButton'].clicked.connect(self.counting)
        self.UI['bogoButton'].clicked.connect(self.bogo)
        self.UI['cocktailButton'].clicked.connect(self.cocktail)
        self.UI['selectionButton'].clicked.connect(self.selection)
        self.UI['introButton'].clicked.connect(self.intro)

    def bubble(self):
        start = int(self.UI['startEdit'].text().strip())
        end = int(self.UI['endEdit'].text().strip())
        self.drawList = self.sort1.bubbleSort(start, end)

    def counting(self):
        start = int(self.UI['startEdit'].text().strip())
        end = int(self.UI['endEdit'].text().strip())
        self.drawList = self.sort1.counting_sort_2(start, end)

    def bogo(self):
        start = int(self.UI['startEdit'].text().strip())
        end = int(self.UI['endEdit'].text().strip())
        self.drawList = self.sort1.bogo_sort(start, end)

    def cocktail(self):
        start = int(self.UI['startEdit'].text().strip())
        end = int(self.UI['endEdit'].text().strip())
        self.drawList = self.sort1.cocktail_sort(start, end)

    def selection(self):
        start = int(self.UI['startEdit'].text().strip())
        end = int(self.UI['endEdit'].text().strip())
        self.drawList = self.sort1.selection_sort(start, end)

    def intro(self):
        start = int(self.UI['startEdit'].text().strip())
        end = int(self.UI['endEdit'].text().strip())
        self.drawList = self.sort1.intro_sort(start, end)

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