function CalculateBMI() {
    height_value = document.getElementById("height").value;
    weight_value = document.getElementById("weight").value;
    result = document.getElementById("result");
    
    height = parseInt(height_value);
    weight = parseFloat(weight_value);

    calculate_bmi = (weight / ((height / 100)** 2));

    if (calculate_bmi >= 18.5 && calculate_bmi <= 24.9) {
        result.innerHTML = "Your BMI: " + calculate_bmi;
        result.style.color = "green";
    } else if (calculate_bmi < 18.5 || calculate_bmi >= 25.0 && calculate_bmi <= 29.9) {
        result.innerHTML = "Your BMI: " + calculate_bmi;
        result.style.color = "yellow";
    } else {
        result.innerHTML = "Your BMI: " + calculate_bmi;
        result.style.color = "red";
    }

}

CalculateBMI()