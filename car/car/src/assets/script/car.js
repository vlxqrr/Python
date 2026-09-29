export function submit(){
    let mark = document.getElementById("mark").value;
    let model = document.getElementById("model").value;
    let caryear = document.getElementById("caryear").value;
    let fuel = document.getElementById("fuel").value;
    let capacity = document.getElementById("capacity").value;
    let wear = document.getElementById("wear").value;

    const confirmedForm = document.getElementById('form');
    
    confirmedForm.style.display = 'none';

    const menu = document.querySelector(".menu");

    const createParagraph = document.createElement("p");
    const choiceInput = document.createElement("input");
    const choiceLabel = document.createElement("label");
    const submitButton = document.createElement("input");
    
    choiceLabel.innerHTML = "Ktora akcje chcesz wykonac?"
    choiceInput.setAttribute("type", "text");
    choiceInput.placeholder = "Wybierz numer (1-8)"
    submitButton.setAttribute("type", "button");
    submitButton.value = "Zatwierdz"

    createParagraph.style.whiteSpace = "pre-line";
    createParagraph.textContent = `------------------
    1) Uruchom silnik
    2) Sprawdz stan pojazdu
    3) Jedz
    4) Przyspiesz
    5) Hamuj
    6) Tankuj
    7) Wylacz silnik
    8) Zakoncz
    ------------------`;

    menu.appendChild(createParagraph);
    menu.appendChild(choiceLabel);
    menu.appendChild(choiceInput);
    menu.appendChild(submitButton);
}