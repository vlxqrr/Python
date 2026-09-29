export function submit(){
    let mark = document.getElementById("mark").value;
    let model = document.getElementById("model").value;
    let caryear = document.getElementById("caryear").value;
    let fuel = document.getElementById("fuel").value;
    let capacity = document.getElementById("capacity").value;
    let wear = document.getElementById("wear").value;

    // schowanie formularza
    const confirmedForm = document.getElementById('form');
    confirmedForm.style.display = 'none';

    // pokazanie menu
    const menu = document.querySelector(".menu");
    menu.hidden = false;

    
}