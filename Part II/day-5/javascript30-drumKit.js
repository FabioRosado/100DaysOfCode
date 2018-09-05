// Followed the video tutorial from Wes Bos.

function playSound(e) {
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`.key[data-key="${e.keyCode}"]`)
  if(audio) {
    audio.currentTime = 0; // rewind to start
    audio.play();
    key.classList.add('playing');
  }
}

function removeTransition(e) {
  if (e.propertyName == 'transform') {
    this.classList.remove('playing');
  }
};

const keys = document.querySelectorAll('.key');
window.addEventListener('keydown', playSound);
keys.forEach(key => key.addEventListener('transitionend', removeTransition));