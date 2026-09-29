// STAN SAMOCHODU (dostępny dla wszystkich funkcji w pliku)
let car = {
  mark: "",
  model: "",
  caryear: 0,
  fuel: 0.0,
  capacity: 0.0,
  wear: 0.0,
  speed: 0.0,
  engine_on: false,
  mileage: 0.0
};

export function submitForm() {
  const mark = document.getElementById("mark").value.trim();
  const model = document.getElementById("model").value.trim();
  const caryearRaw = document.getElementById("caryear").value.trim();
  const fuelRaw = document.getElementById("fuel").value.trim();
  const capacityRaw = document.getElementById("capacity").value.trim();
  const wearRaw = document.getElementById("wear").value.trim();

  if (!mark || !model) {
    alert("Marka i model nie moga byc puste");
    return;
  }

  const caryearValue = Number(caryearRaw);
  const fuelValue = Number(fuelRaw);
  const capacityValue = Number(capacityRaw);
  const wearValue = Number(wearRaw);

  const hasInvalidNumber =
    caryearRaw === "" || isNaN(caryearValue) || caryearValue <= 0 ||
    fuelRaw === "" || isNaN(fuelValue) || fuelValue < 0 ||
    capacityRaw === "" || isNaN(capacityValue) || capacityValue <= 0 ||
    wearRaw === "" || isNaN(wearValue) || wearValue <= 0;

  if (hasInvalidNumber) {
    alert("Błąd formatu: Rok, paliwo, pojemność i spalanie muszą być poprawnymi liczbami!");
    return;
  }

  car.mark = mark;
  car.model = model;
  car.caryear = caryearValue;
  car.fuel = fuelValue;
  car.capacity = capacityValue;
  car.wear = wearValue;
  car.speed = 0.0;
  car.engine_on = false;
  car.mileage = 0.0;

  alert("Wszystkie pola zostaly poprawnie uzupelnione!");
  document.getElementById('form').style.display = "none";
  document.querySelector(".menu").hidden = false;
}

export function submitChoice() {
  const submitAction = document.getElementById("choice").value.trim();

  if (submitAction === "1") {
    startEngine();
  } else if (submitAction === "2") {
    showState();
  } else if (submitAction === "3") {
    drive();
  } else if (submitAction === "4") {
    acceleration();
  } else if (submitAction === "5") {
    slowingDown();
  } else if (submitAction === "6") {
    refuel();
  } else if (submitAction === "7") {
    stopEngine();
  } else if (submitAction === "8") {
    alert("Dziekujemy za skorzystanie o/");
    document.getElementById("menu").hidden = true;
    const form = document.getElementById('form');
    form.style.display = "";
    form.reset();
  } else {
    alert("Podaj poprawny numer akcji (1-8)!");
  }
}

export function startEngine() {
  if (car.fuel > 0) {
    car.engine_on = true;
    document.getElementById('result').innerHTML = "Auto wlaczone";
  } else {
    document.getElementById('result').innerHTML = "Nie ma paliwa";
  }
}


export function showState() {
    const engineStatus = "";
    if (car.engine_on) {
        engineStatus = "Wlaczony";
    } else {
        "wylaczony";
    }

    const state = `
    Mark: ${car.mark}<br>
    Model: ${car.model}<br>
    Rok producji: ${car.caryear}<br>
    Paliwo: ${car.fuel} / ${car.capacity} L<br>
    Spalanie: ${car.wear} L/km<br>
    Aktualna predkosc: ${car.speed}<br>
    Przebieg: ${car.mileage}<br> km
    Stan silnika: ${car.engine_on ? "Wlaczony" : "Wylaczony"}
    `;
    document.getElementById('result').innerHTML = state;
}
export function drive() {
    if (!car.engine_on){
        document.getElementById('result').innerHTML = "Auto jest wylaczone";
        return;
    }

    const result = document.getElementById('result');
    const distanceLabel = document.createElement("label");
    distanceLabel.innerHTML = "Ile kilometrow chcesz przejechac?";
    const distanceInput = document.createElement("input");
    distanceInput.setAttribute("type", "number");
    distanceInput.placeholder = "Podaj ilosc kilometrow";
    const distanceButton = document.createElement("input");
    distanceButton.setAttribute("type", "button");
    distanceButton.value = "Zatwierdz";

    result.appendChild(distanceLabel);
    result.appendChild(distanceInput);
    result.appendChild(distanceButton);
}   
export function acceleration() {}
export function slowingDown() {}
export function refuel() {}

export function stopEngine() {
    if (!car.engine_on){
        document.getElementById('result').innerHTML = "Auto jest wylaczone";
        return;
    }

    if (car.speed > 0){
        document.getElementById('result').innerHTML = "Pierw zahamuj do 0, aktualna predkosc" + car.speed + "km/h";
        return;
    } 

    car.engine_on = false;
    document.getElementById('result').innerHTML = "Auto zostalo wylaczone";

}