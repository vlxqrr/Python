export function submit(){
    let mark = document.getElementById("mark").value.trim();
    let model = document.getElementById("model").value.trim();
    let caryearRaw = parseFloat(document.getElementById("caryear").value.trim());
    let fuelRaw = parseFloat(document.getElementById("fuel").value.trim());
    let capacityRaw = parseFloat(document.getElementById("capacity").value.trim());
    let wearRaw = parseFloat(document.getElementById("wear").value.trim());

    
    if(!mark || !model){
        alert("Marka i model nie moga byc puste");
        return;
    }

    const caryear = Number(caryearRaw);
    const fuel = Number(fuelRaw);
    const capacity = Number(capacityRaw);
    const wear = Number(wearRaw);

    const hasInvalidNumber =
        caryearRaw === "" || isNaN(caryear) || caryear <= 0 ||
        fuelRaw === "" || isNaN(fuel) || fuel < 0 ||
        capacityRaw === "" || isNaN(capacity) || capacity <= 0 ||
        wearRaw === "" || isNaN(wear) || wear <= 0;

    if (hasInvalidNumber) {
        alert("Błąd formatu: Rok, paliwo, pojemność i spalanie muszą być poprawnymi liczbami!");
        return;
    }

    alert("Wszystkie pola zostaly poprawnie uzupelnione!");
    // schowanie formularza
    const confirmedForm = document.getElementById('form').style.display = "none";
    // pokazanie menu
    const menu = document.querySelector(".menu").hidden = false;

}