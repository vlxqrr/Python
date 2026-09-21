import tkinter as tk

class Sorting:
    def __init__(self, userInput):
        self.root = root
        self.array = []
        tk.Label(self.root, text=f"Przed sortowaniem {self.array}").pack()
        self.userInput = tk.Entry()
        self.userInput.pack()
        self.result = ""

        self.choose()

    def enterArray(self):
        text = self.userInput.get()
        if not text.strip():
            self.array = []
            return False
        try:
            self.array = [int(x.strip()) for x in text.split(",") if x.strip()]
            return True
        except ValueError:
            self.result.config(text="Błąd: wpisz tylko liczby oddzielone przecinkami!")
            return False

    def bubbleSort(self):
        if not self.enterArray(): 
            return
            
        n = len(self.array)
        for i in range(n - 1):
            for j in range(n-1-i):
                if (self.array[j] > self.array[j+1]):
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        self.result.config(text=f"bubbleSort: {self.array}")

    def selectionSort(self):
        if not self.enterArray():
            return
            
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if (self.array[j] < self.array[min_index]):
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        self.result.config(text=f"selectionSort: {self.array}")
    
    def insertionSort(self):
        if not self.enterArray():
            return
            
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j+1] = key
        self.result.config(text=f"insertionSort: {self.array}")

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
            
        self.result.config(text=f"mergeSort: {self.array}")

    def heapify(self, i):
        if not self.enterArray():
            return
            
        n = len(self.array)
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
        if not self.enterArray():
            return
            
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]

            self.heapify(i, 0)

        self.result.config(text=f"heapSort: {self.array}")
        
    def choose(self):
        bubblehBtn = tk.Button(self.root, text="bubbleSort", command=self.bubbleSort)
        bubblehBtn.pack()

        selectionBtn = tk.Button(self.root, text="selectionSort", command=self.selectionSort)
        selectionBtn.pack()

        insertionBtn = tk.Button(self.root, text="insertionSort", command=self.insertionSort)
        insertionBtn.pack()

        mergeBtn = tk.Button(self.root, text="mergeSort", command=self.mergeSort)
        mergeBtn.pack()

        heapBtn = tk.Button(self.root, text="heapSort", command=self.heapSort)
        heapBtn.pack()

        self.result = tk.Label(self.root, text="")
        self.result.pack()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1920x1080")
    root.title("Sort")
    app = Sorting("")
    app.run()
