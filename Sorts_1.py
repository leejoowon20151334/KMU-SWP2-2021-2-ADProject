import random


class Sorts1():

    def __init__(self):
        super().__init__()

    def counting_sort(self, start, end):

        values = self.randomArray(start, end)

        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        size = len(values)
        counting_num = {}
        values_copy = values[:]
        answer = [0 for _ in range(size)]

        # 숫자의 등장횟수를 세서 counting_num 에 딕셔너리 형태로 저장
        for i in sorted(values):
            if i not in counting_num:
                counting_num[i] = 1
            else:
                counting_num[i] += 1

        # counting_num 의 value 를 누적합으로 변경.
        sum = 0
        for i in sorted(counting_num):
            sum += counting_num[i]
            counting_num[i] = sum

        # list의 값들을 answer에 저장.
        # 규칙1 : 카운팅 된 횟수에 대응되는 인덱스 위치에 숫자 넣기.
        # 규칙2 : 다음번에 동일한 숫자 순서가 왔을 때 이미 answer에 있는 숫자의 왼쪽에 넣어지도록 누적합값 -1 하기
        for i in values_copy:
            # 변경될 값 표시
            drawList += [{'values': list(answer), 'color': {i: [255, 255, 255]}}]
            # 값 변경
            answer[counting_num[i] - 1] = i
            counting_num[i] -= 1
            # 변경 후 표시
            drawList += [{'values': list(answer), 'color': {}}]

        return drawList

    def bogo_sort(self, start, end):

        values = self.randomArray(start, end)

        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        cnt = 0
        MAX = len(values) + 100 if len(values) + 20 < 100 else 500

        # 랜덤으로 섞고 정렬됐으면 그만. 정렬안됐으면 계속.
        while (self.is_sorted(values) == False):
            # 변경될 값 표시
            drawList += [{'values': list(values), 'color': {}}]
            # 값 변경
            self.shuffle(values)
            cnt += 1
            # 변경 후 표시
            drawList += [{'values': list(values), 'color': {}}]

            if cnt > MAX:
                drawList += [{'values': list(values), 'color': {}, }]
                drawList[-1]['error'] = "에러 : 제한된 시도횟수({}번) 이내로 정렬이 실패하여 알고리즘을 강제로 종료합니다.".format(MAX)
                return drawList

        return drawList

    def is_sorted(self, list):
        n = len(list)
        for i in range(0, n - 1):
            if (list[i] > list[i + 1]):
                return False
        return True

    def shuffle(self, list):
        n = len(list)
        for i in range(0, n):
            r = random.randint(0, n - 1)
            list[i], list[r] = list[r], list[i]

    def cocktail_sort(self, start, end):

        values = self.randomArray(start, end)

        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        a = 0
        b = len(values) - 1
        swapped = True

        # 좌->우 방향으로 붙어있는 두 수 비교하면서 위치 바꾸기
        # 무조건 맨 오른쪽 숫자는 가장 큰 수가 됨. 다음번부터는 맨 오른쪽은 제외하고 돌기 b -= 1
        # 우->좌 방향으로 붙어있는 두 수 비교하면서 위치 바꾸기
        # 무조건 맨 왼쪽 숫자는 가장 작은 수가 됨. 다음번 부터는 맨 왼쪽은 제외히고 돌기 a -= 1
        while swapped == True:
            swapped = False

            for i in range(a, b):
                if values[i] > values[i + 1]:
                    # 변경될 값 표시
                    drawList += [{'values': list(values), 'color': {i: [255, 255, 255], i+1: [255, 255, 255]}}]
                    # 값 변경
                    values[i], values[i + 1] = values[i + 1], values[i]
                    # 변경 후 표시
                    drawList += [{'values': list(values), 'color': {}}]
                    swapped = True

            if swapped == False:
                break

            swapped = False
            b -= 1

            for i in range(b - 1, a - 1, -1):
                if values[i] > values[i + 1]:
                    # 변경될 값 표시
                    drawList += [{'values': list(values), 'color': {i: [255, 255, 255], i + 1: [255, 255, 255]}}]
                    # 값 변경
                    values[i], values[i + 1] = values[i + 1], values[i]
                    # 변경 후 표시
                    drawList += [{'values': list(values), 'color': {}}]
                    swapped = True

            a += 1

        return drawList

    def selection_sort(self, start, end):

        values = self.randomArray(start, end)

        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        size = len(values)

        # 리스트의 모든 인덱스
        for i in range(0, size - 1):
            min_idx = i

            # 리스트의 끝까지 돌면서 가장 작은 값을 찾아 시작지점 인덱스에 저장.
            for j in range(i + 1, size):
                if values[j] < values[min_idx]:
                    min_idx = j
            # 변경될 값 표시
            drawList += [{'values': list(values), 'color': {i: [255, 255, 255], min_idx: [255, 255, 255]}}]
            # 값 변경
            values[i], values[min_idx] = values[min_idx], values[i]
            # 변경 후 표시
            drawList += [{'values': list(values), 'color': {}}]

        return drawList

    # Time Complexity O(n),O(n^2),O(n^2) | Space Complexity O(1) | stable
    def insertSort(self, array, begin=0, end=None):

        if end == None:
            end = len(array)
        for i in range(begin, end):
            j = i
            toChange = array[i]
            while (j != begin and array[j - 1] > toChange):
                # 변경될 값 표시
                self.intro_drawList += [{'values': list(array), 'color': {j: [255, 255, 255], j-1: [255, 255, 255]}}]
                # 값 변경
                array[j] = array[j - 1]
                j -= 1
                # 변경 후 표시
                self.intro_drawList += [{'values': list(array), 'color': {}}]
            # 변경될 값 표시
            self.intro_drawList += [{'values': list(array), 'color': {j: [255, 255, 255]}}]
            # 값 변경
            array[j] = toChange
            # 변경 후 표시
            self.intro_drawList += [{'values': list(array), 'color': {}}]
            """보여주기---------------------------------------------"""
        return self.intro_drawList

    # Time Complexity O(nlogn) | Space Complexity O(1) | not stable
    def heapify(self, arr, n, i, isIntro):  # Max Heap
        if(isIntro):
            drawList = self.intro_drawList
        else:
            drawList = self.heap_drawList

        # 부모트리와 자식트리 인덱스
        largest = i  # 트리에서 가장 큰 값 찾기
        l = 2 * i + 1  # Left Node
        r = 2 * i + 2  # Right Node

        # 힙트리 성질(부모트리는 자식트리보다 값이 크다) 만족하는지 확인하고 아니면 트리(부모+자식2)에서 최댓값 변경
        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        # root가 최대가 아니면 ( 아래 노드가 위 노드보다 크면 )
        # 최대 값과 바꾸고, 계속 heapify
        # 힙트리 성질 만족하면 끝.
        if largest != i:
            # 변경될 값 표시
            drawList += [{'values': list(arr), 'color': {i: [255, 255, 255], largest: [255, 255, 255]}}]
            # 값 변경
            arr[i], arr[largest] = arr[largest], arr[i]
            # 변경 후 표시
            drawList += [{'values': list(arr), 'color': {}}]

            self.heapify(arr, n, largest, isIntro)

    def heapSort(self, values):

        n = len(values)

        for i in range(n // 2, -1, -1):
            self.heapify(values, n, i, True)

            # 값 변경
            self.heapify(values, n, i, True)


        for i in range(n - 1, 0, -1):
            # 변경될 값 표시
            self.intro_drawList += [{'values': list(values), 'color': {i: [255, 255, 255], 0: [255, 255, 255]}}]
            values[i], values[0] = values[0], values[i]
            # 변경 후 표시
            self.intro_drawList += [{'values': list(values), 'color': {}}]

            # Heapify root element
            self.heapify(values, i, 0, True)

        return self.intro_drawList

    # quick 정렬에서 pivot 값을 선정하는 함수.
    # comparison보다 XOR을 속도면에서 선택함
    # 비교 줄이기
    def medianOf3(self, array, lowIdx, midIdx, highIdx):
        if (array[lowIdx] - array[midIdx]) * (array[highIdx] - array[lowIdx]) >= 0:
            return array[lowIdx]
        elif (array[midIdx] - array[lowIdx]) * (array[highIdx] - array[midIdx]) >= 0:
            return array[midIdx]
        else:
            return array[highIdx]

    def getPartition(self, array, low, high, pivot):

        while True:
            while (array[low] < pivot):
                low += 1
            high -= 1
            while (pivot < array[high]):
                high -= 1
            if low >= high:
                return low
            # 변경될 값 표시
            self.intro_drawList += [{'values': list(array), 'color': {high: [255, 255, 255], low:[255, 255, 255]}}]
            # 값 변경
            array[low], array[high] = array[high], array[low]
            # 변경 후 표시
            self.intro_drawList += [{'values': list(array), 'color': {}}]

            low += 1

    # Time Complexity O(nlogn) | Space Complexity O(logn) | not stable
    def intro_sort(self, start, end):

        values = self.randomArray(start, end)

        self.intro_drawList = []
        self.intro_drawList += [{'values': list(values), 'color': {}}]

        maxDepth = 2 * (len(values).bit_length() - 1)  # 2* (log2(length) - 1)
        sizeThreshold = 16
        return self.introSortHelper(values, 0, len(values), sizeThreshold, maxDepth)

    def introSortHelper(self, array, start, end, sizeThreshold, depthLimit):
        # size가 16보다 크면 heap sort or quick sort
        while (end - start > sizeThreshold):
            if (depthLimit == 0):
                return self.heapSort(array)
            depthLimit -= 1

            median = self.medianOf3(array, start, start +
                               ((end - start) // 2) + 1, end - 1)
            p = self.getPartition(array, start, end, median)
            self.introSortHelper(array, p, end, sizeThreshold, depthLimit)
            end = p
        # insert Sort로 종료
        return self.insertSort(array, start, end)

    # 내부 반복문에서는 정렬 범위에 새롭게 추가된 값과 기존 값들을 뒤에서 부터 계속해서 비교해나가면서
    # 앞의 값이 뒤의 값보다 클 경우 자리 교대(swap)를 합니다. 외부 반복문에서는 정렬 범위를 2에서 N으로 확대해 나갑니다.
    def insertion_sort(self, start, end):

        values = self.randomArray(start, end)

        # 화면 초기화
        drawList = []
        drawList += [{'values': list(values), 'color': {}}]

        for ending in range(1, len(values)):
            for i in range(ending, 0, -1):
                if values[i - 1] > values[i]:
                    # 변경될 값 표시
                    drawList += [{'values': list(values), 'color': {i: [255, 255, 255]}}]
                    # 값 변경
                    values[i - 1], values[i] = values[i], values[i - 1]
                    # 변경 후 표시
                    drawList += [{'values': list(values), 'color': {}}]

        return drawList

    def heap_sort(self, start, end):

        values = self.randomArray(start, end)

        # 화면 초기화
        self.heap_drawList = []
        self.heap_drawList += [{'values': list(values), 'color': {}}]

        n = len(values)

        # 힙 트리 구성하기
        for i in range(n // 2, -1, -1):
            self.heapify(values, n, i, False)

        for i in range(n - 1, 0, -1):
            # 변경될 값 표시
            self.heap_drawList += [{'values': list(values), 'color': {i: [255, 255, 255], 0: [255, 255, 255]}}]
            # 값 변경
            # 리스트에서 가장 큰 값 맨 오른쪽으로 이동( 힙트리의 루트 노드의 값 )
            # 동시에 가장 마지막 노드 ( 가장 아래, 가장 오른쪽 노드 ) 의 값이 힙의 루트로 이동.
            values[i], values[0] = values[0], values[i]
            # 변경 후 표시
            self.heap_drawList += [{'values': list(values), 'color': {}}]

            # 노드 하나가 빠진 상태에서( 루트 노드에 가장 마지막 노드 값이 가고 원래 루트노드의 값 없어진 상태 ) 다시 힙 트리 구성.
            self.heapify(values, i, 0, False)


        return self.heap_drawList

    def quick_sort(self, start, end):

        self.quick_values = self.randomArray(start, end)

        # 화면 초기화
        self.quick_drawList = []
        self.quick_drawList += [{'values': list(self.quick_values), 'color': {}}]

        return self.quick_sorting(0, len(self.quick_values) - 1)

    def quick_sorting(self, low, high):
        if high <= low:
            return self.quick_drawList

        mid = self.partition(low, high)
        self.quick_sorting(low, mid - 1)
        self.quick_sorting(mid, high)

        return self.quick_drawList

    def partition(self, low, high):
        pivot = self.quick_values[(low + high) // 2]
        while low <= high:
            while self.quick_values[low] < pivot:
                low += 1
            while self.quick_values[high] > pivot:
                high -= 1
            if low <= high:
                # 변경될 값 표시
                self.quick_drawList += [{'values': list(self.quick_values), 'color': {low: [255, 255, 255], high: [255, 255, 255]}}]
                # 값 변경
                self.quick_values[low], self.quick_values[high] = self.quick_values[high], self.quick_values[low]
                # 변경 후 표시
                self.quick_drawList += [{'values': list(self.quick_values), 'color': {}}]

                low, high = low + 1, high - 1
        return low

    def randomArray(self, start, end):
        rand = [i for i in range(start, end + 1)]
        random.shuffle(rand)
        return rand