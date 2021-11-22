import random


class Sorts1():

    def __init__(self):
        super().__init__()

    # 버블정렬
    def bubbleSort(self, start, end):

        values = self.randomArray(start, end)

        # 화면 초기화
        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        # 정렬 시작
        for last in range(len(values), 0, -1):
            for i in range(0, last - 1):
                # 값 변경시
                if values[i] > values[i + 1]:
                    # 변경될 값 표시
                    drawList += [{'values': list(values), 'color': {i: [255, 255, 255], i + 1: [255, 255, 255]}}]
                    # 값 변경
                    values[i], values[i + 1] = values[i + 1], values[i]
                    # 변경 후 표시
                    drawList += [{'values': list(values), 'color': {}}]

        return drawList

    def randomArray(self, start, end):
        rand = [i for i in range(start, end + 1)]
        random.shuffle(rand)
        return rand
