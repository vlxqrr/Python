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


        
    def run(self):
        self.enterArray()
        print(f"Przed sortowaniem: {self.array}")
        self.mergeSort()
        print(f"Po sortowaniu: {self.array}")

if __name__ == "__main__":
    app = Sorting()
    app.run()
