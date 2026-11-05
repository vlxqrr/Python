userInput = input("Podaj tablice: ")
array = [int(x.strip()) for x in userInput.split(",") if x.strip()]
n = len(array)

def bubbleSort():
        for i in range(n - 1):
            for j in range(n-1-i):
                if (array[j] > array[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
        print(f"{array[0]} min, {array[-1]} max")

bubbleSort()