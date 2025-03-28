// wählen des Glow Kreises
const circle = document.querySelector('.glow-circle');

// Funktion für zufällige Position
function moveCircle() {
    const maxX = window.innerWidth - circle.offsetWidth;
    const maxY = window.innerHeight - circle.offsetHeight;

    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);

    circle.style.left = `${randomX}px`;
    circle.style.top = `${randomY}px`;
}

setInterval(moveCircle, 3000);

moveCircle();