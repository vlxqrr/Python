userInput = input("Podaj tablice: ")
array = [int(x.strip()) for x in userInput.split(",") if x.strip()]
n = len(array)

def bubbleSort():
        for i in range(n - 1):
            for j in range(n-1-i):
                if (array[j] > array[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
        
        if array[-1] == array[-2]:
            print(None)
        elif array[-1] > array[-2]:
             print(f"{array[-2]} jest 2 najwieksza")
        else:
             print(f"{array[-1]} jest 2 najwieksza")
            
             

bubbleSort()