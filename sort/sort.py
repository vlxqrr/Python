class Sorting:
    def __init__(self):
        self.array = []

    def enterArray(self):
        userInput = input("Podaj tablice 6 znakow po przecinku: ")
        self.array = [int(x.strip()) for x in userInput.split(",") if x.strip()]
        self.n = len(self.array)

    def bubbleSort(self):
        for i in range(self.n - 1):
            for j in range(self.n-1-i):
                if (self.array[j] > self.array[j+1]):
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        return self.array

    def selectionSort(self):
        for i in range(self.n):
            min_index = i
            for j in range(i + 1, self.n):
                if (self.array[j] < self.array[min_index]):
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        return self.array
    
    def insertionSort(self):
        for i in range(1, self.n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j+1] = key
        return self.array

    def mergeSort(self, arr=None):
        if arr is None:
            arr = self.array

        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[0:mid]
            right = arr[mid:len(arr)]

            self.mergeSort(left)
            self.mergeSort(right)
            
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
            
        return arr

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.array[left] > self.array[largest]:
            largest = left
        
        if right < n and self.array[right] > self.array[largest]:
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]

            self.heapify(n, largest)

    def heapSort(self):
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]

            self.heapify(i, 0)
        return self.array

        
    def run(self):
        self.enterArray()
        print(f"Przed sortowaniem: {self.array}")
        self.bubbleSort()
        print(f"bubbleSort: Po sortowaniu: {self.array}")
        self.selectionSort()
        print(f"selectionSort: Po sortowaniu: {self.array}")
        self.insertionSort()
        print(f"insertionSort: Po sortowaniu: {self.array}")
        self.mergeSort()
        print(f"mergeSort: Po sortowaniu: {self.array}")
        self.heapSort()
        print(f"heapSort: Po sortowaniu: {self.array}")

if __name__ == "__main__":
    app = Sorting()
    app.run()
