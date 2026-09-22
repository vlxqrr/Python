export function bubbleSort() {
    let userInput = document.getElementById("userInput").value;
    const array = userInput
        .trim()
        .split(/[\s,]+/)
        .map(numStr => Number(numStr))
        .filter(num => !isNaN(num));

    if (array.length === 0) {
        document.getElementById("result").innerHTML = "Wprowadź poprawne liczby!";
        return;
    }

    let n = array.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - 1 - i; j++) {
            if (array[j] > array[j + 1]) {
                [array[j], array[j + 1]] = [array[j + 1], array[j]];
            }
        }
    }
    const result = array.join(", ");
    document.getElementById("result").innerHTML = result;
}

export function selectionSort() {
    let userInput = document.getElementById("userInput").value;
    const array = userInput
        .trim()
        .split(/[\s,]+/)
        .map(numStr => Number(numStr))
        .filter(num => !isNaN(num));

    if (array.length === 0) {
        document.getElementById("result").innerHTML = "Wprowadź poprawne liczby!";
        return;
    }
    let n = array.length;

    for (let i = 0; i < n - 1; i++) {
        let min = i;
        for (let j = i + 1; j < n; j++) {
            if (array[j] < array[min]) {
                min = j;
            }
        }
        if (min !== i) {
            [array[i], array[min]] = [array[min], array[i]];
        }
    }
    const result = array.join(", ");
    document.getElementById("result").innerHTML = result;

}

export function insertionSort() {
    let userInput = document.getElementById("userInput").value;
    const array = userInput
        .trim()
        .split(/[\s,]+/)
        .map(numStr => Number(numStr))
        .filter(num => !isNaN(num));

    if (array.length === 0) {
        document.getElementById("result").innerHTML = "Wprowadź poprawne liczby!";
        return;
    }

    let n = array.length;
    for (let i = 1; i < n; i++) {
        let key = array[i];
        let j = i - 1;
        while (j >= 0 && key < array[j]) {
            array[j + 1] = array[j];
            j -= 1;
        }
        array[j + 1] = key;
    }
    const result = array.join(", ");
    document.getElementById("result").innerHTML = result;
}

export function mergeSort(array) {
    let isInitial = false;

    if (!Array.isArray(array)) {
        isInitial = true;
        let userInput = document.getElementById("userInput").value;
        array = userInput
            .trim()
            .split(/[\s,]+/)
            .map(numStr => Number(numStr))
            .filter(num => !isNaN(num));
        if (array.length === 0) {
            document.getElementById("result").innerHTML = "Wprowadź poprawne liczby!";
            return;
        }
    }

    if (array.length > 1) {
        let mid = Math.floor(array.length / 2);
        let left = array.slice(0, mid);
        let right = array.slice(mid);

        mergeSort(left);
        mergeSort(right);
        let i = 0;
        let j = 0;
        let k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                array[k] = left[i];
                i += 1;
            } else {
                array[k] = right[j];
                j += 1;
            }
            k += 1;
        }

        while (i < left.length) {
            array[k] = left[i];
            i += 1;
            k += 1;
        }

        while (j < right.length) {
            array[k] = right[j];
            j += 1;
            k += 1;
        }
    }
    if (isInitial) {
        const result = array.join(", ");
        document.getElementById("result").innerHTML = result;
    }
}
export function heapify(array, n, i) {
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

    if (left < n && array[left] > array[largest]) {
        largest = left;
    }
    if (right < n && array[right] > array[largest]) {
        largest = right;
    }
    if (largest !== i) {
        [array[i], array[largest]] = [array[largest], array[i]];

        heapify(array, n, largest);
    }
}
export function heapSort() {
    let userInput = document.getElementById("userInput").value;
    const array = userInput
        .trim()
        .split(/[\s,]+/)
        .map(numStr => Number(numStr))
        .filter(num => !isNaN(num));

    if (array.length === 0) {
        document.getElementById("result").innerHTML = "Wprowadź poprawne liczby!";
        return;
    }
    let n = array.length;

    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(array, n, i);
    }


    for (let i = n - 1; i > 0; i--) {
        [array[0], array[i]] = [array[i], array[0]];
        heapify(array, i, 0);
    }

    const result = array.join(", ");
    document.getElementById("result").innerHTML = result;
}