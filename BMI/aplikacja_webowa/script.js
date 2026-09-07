function CalculateBMI() {
  // Pobranie danych
  const height_value = document.getElementById("height").value;
  const weight_value = document.getElementById("weight").value;
  const result = document.getElementById("result");

  const height = parseInt(height_value);
  const weight = parseFloat(weight_value);

  // Walidacja czy pola nie są puste
  if (isNaN(height) || isNaN(weight) || height <= 0) {
    result.innerHTML = "Wprowadź poprawne dane!";
    result.style.color = "red";
    return;
  }

  // Obliczenie BMI
  const calculate_bmi = weight / ((height / 100) ** 2);
  const formatted_bmi = calculate_bmi.toFixed(2);

  // Zapis do historii i odświeżenie listy na ekranie
  SaveBMIResult(formatted_bmi);
  DisplayHistory();

  // Kolorystyka i komunikat
  if (calculate_bmi >= 18.5 && calculate_bmi <= 24.9) {
    result.innerHTML = "Your BMI: " + formatted_bmi;
    result.style.color = "green";
  } else if (calculate_bmi < 18.5 || (calculate_bmi >= 25.0 && calculate_bmi <= 29.9)) {
    result.innerHTML = "Your BMI: " + formatted_bmi;
    result.style.color = "yellow";
  } else {
    result.innerHTML = "Your BMI: " + formatted_bmi;
    result.style.color = "red";
  }
}

function SaveBMIResult(bmiValue) {
  const history = JSON.parse(localStorage.getItem('bmiHistory')) || [];

  history.unshift(bmiValue);

  if (history.length > 5) {
    history.length = 5;
  }

  localStorage.setItem('bmiHistory', JSON.stringify(history));
}

function DisplayHistory() {
  const historyList = document.getElementById('historyList');
  if (!historyList) return;

  const history = JSON.parse(localStorage.getItem('bmiHistory')) || [];

  historyList.innerHTML = '';

  history.forEach((bmi, index) => {
    const li = document.createElement('li');
    li.textContent = `#${index + 1}: BMI ${bmi}`;
    historyList.appendChild(li);
  });
}

window.addEventListener('DOMContentLoaded', DisplayHistory);