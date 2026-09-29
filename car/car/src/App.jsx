import { useState } from 'react'
import './App.css'
import { submitForm, submitChoice } from './assets/script/car'

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

          <input id="submitForm" type="button" value="Zatwierdz" onClick={submitForm}/>
        </form>
      </section>
      <section class="menu" id="menu" hidden>
          <p id="menuList">------------------ <br/>
            1) Uruchom silnik <br/>
            2) Sprawdz stan pojazdu <br/>
            3) Jedz <br/>
            4) Przyspiesz <br/>
            5) Hamuj <br/>
            6) Tankuj <br/>
            7) Wylacz silnik <br/>
            8) Zakoncz <br/>
           ------------------</p>
           <label>Ktora akcje chcesz wykonac?</label>
           <input type="text" id='choice' placeholder='Wybierz numer (1-8)'/>
           <input type="button" id="submitAction" value="Zatwierdz" onClick={submitChoice} />
           <p id="result"></p>
        </section>
      
    </>
  )
}

export default App


