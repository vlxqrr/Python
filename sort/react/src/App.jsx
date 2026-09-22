import { useState } from 'react'
import './App.css'
import { bubbleSort } from './assets/scripts/sort.js'
import { selectionSort } from './assets/scripts/sort.js'
import { insertionSort } from './assets/scripts/sort.js'
import { mergeSort } from './assets/scripts/sort.js'
import { heapSort } from './assets/scripts/sort.js'
function App() {
  return (
    <div>
      <h2>Sorting</h2>
      <p>Tablica przed sortowaniem:</p>
      <form>
        <input type="text" id="userInput" />
        <input type="button" value="BubbleSort" onClick={bubbleSort} />
        <input type="button" value="SelectionSort" onClick={selectionSort} />
        <input type="button" value="InsertionSort" onClick={insertionSort} />
        <input type="button" value="MergeSort" onClick={mergeSort} />
        <input type="button" value="HeapSort" onClick={heapSort} />
        <p id="result"></p>
      </form>



    </div>
  )
}

export default App
