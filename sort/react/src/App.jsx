import { useState } from 'react'
import './App.css'
import { bubbleSort } from './assets/scripts/sort.js'
function App() {
  return (
    <div>
      <h2>Sorting</h2>
      <p>Tablica przed sortowaniem:</p>
      <input type="text" id="userInput" />
      <input type="button" value="BubbleSort" />
      <input type="button" value="SelectionSort" />
      <input type="button" value="InsertionSort" />
      <input type="button" value="MergeSort" />
      <input type="button" value="HeapSort" />
      <p id="result"></p>


    </div>
  )
}

export default App
