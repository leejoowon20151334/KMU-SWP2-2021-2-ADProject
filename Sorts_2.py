import random


class Sorts2():

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

    def mergeSort(self, start, end):

        values = self.randomArray(start, end)

        # 화면 초기화
        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        # 분해
        divide = [{'color': self.randomColor(), 'values': list(values)}]
        while len(divide) < len(values):
            newDivide = []
            for i in range(0, len(divide)):
                newDivide += [
                    {'color': divide[i]['color'], 'values': divide[i]['values'][:len(divide[i]['values']) // 2]}]
                newDivide += [
                    {'color': self.randomColor(), 'values': divide[i]['values'][len(divide[i]['values']) // 2:]}]
                drawDivide = list(newDivide)
                drawDivide += [divide[i] for i in range(i + 1, len(divide))]
                drawList += [self.divDrawFormat(drawDivide)]
            divide = list(newDivide)

        # 병합
        while len(divide) > 1:
            newDivide = []
            while len(divide) > 1 != None:
                new = {'color': self.randomColor(), 'values': []}
                divide1 = dict(divide[0])
                divide2 = dict(divide[1])
                for j in range(0, len(divide1['values']) + len(divide2['values'])):
                    if len(divide1['values']) < 1:
                        new['values'] += [divide2['values'].pop(0)]
                    elif len(divide2['values']) < 1:
                        new['values'] += [divide1['values'].pop(0)]
                    elif divide1['values'][0] < divide2['values'][0]:
                        new['values'] += [divide1['values'].pop(0)]
                    else:
                        new['values'] += [divide2['values'].pop(0)]
                    drawList += [self.divDrawFormat(newDivide + [new] + [divide1] + [divide2] + divide[2:])]
                newDivide += [new]
                divide.pop(1)
                divide.pop(0)
            newDivide += list(divide)
            divide = list(newDivide)

        return drawList

    def randomArray(self, start, end):
        rand = [i for i in range(start, end + 1)]
        random.shuffle(rand)
        return rand

    def randomColor(self):
        return [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]

    def divDrawFormat(self, drawDivide):
        drawList = {
            'values': [],
            'color': {}
        }
        j = 0
        for i in range(0, len(drawDivide)):
            drawList['values'] += list(drawDivide[i]['values'])
            for k in range(0, len(drawDivide[i]['values'])):
                drawList['color'][j] = drawDivide[i]['color']
                j += 1
        return drawList
