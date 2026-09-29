import { useState } from 'react'
import './App.css'
import { submit } from './assets/script/car'

function App() {

  return (
    <>
      <header>
        <p>Aplikacja - Auto</p>
      </header>
      <section class="section">
        <form id="form">
          <label htmlFor="">Podaj marke auta:</label>
          <input type="text" id="mark" placeholder='Marka auta'/>

          <label htmlFor="">Podaj model auta:</label>
          <input type="text" id="model" placeholder='Model auta'/>

          <label htmlFor="">Podaj rok wyprodukowania:</label>
          <input type="number" id="caryear" placeholder='Rok wyprodukowania'/>

          <label htmlFor="">Podaj ile jest paliwa:</label>
          <input type="number" id="fuel" placeholder='Ilosc paliwa'/>

          <label htmlFor="">Podaj pojemnosc:</label>
          <input type="number" id="capacity" placeholder='Pojemnosc auta'/>

          <label htmlFor="">Podaj jakie auto ma spalanie:</label>
          <input type="number" id="wear" placeholder='Spalanie auta'/>

          <input id="submitForm" type="button" value="Zatwierdz" onClick={submit}/>
        </form>
        <section class="menu" id="menu"></section>
      </section>
      
    </>
  )
}

export default App
