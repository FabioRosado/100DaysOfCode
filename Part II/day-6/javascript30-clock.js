const secondHand = document.querySelector('.second-hand');
const minuteHand = document.querySelector('.min-hand');
const hourHand = document.querySelector('.hour-hand');

function setDate(){
  const now = new Date();
  const seconds = ((now.getSeconds() / 60) * 360) + 90; 
  const minutes = ((now.getMinutes() / 60) * 360) + 90;
  const hours = ((now.getHours() /  12) * 360) + 90;


  secondHand.style.transform = `rotate(${seconds}deg)`;
  minuteHand.style.transform = `rotate(${minutes}deg)`;
  hourHand.style.transform = `rotate(${hours}deg)`;

  }

  setInterval(setDate, 1000);