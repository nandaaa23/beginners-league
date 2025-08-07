const topLeft = document.querySelector('.top-left-panel');
const topRight = document.querySelector('.top-right-panel');
const bottomLeft = document.querySelector('.bottom-left-panel');
const bottomRight = document.querySelector('.bottom-right-panel');
const startBtn = document.getElementById('start-btn');

const getRandomPanel = () => {
const panels = [
    topLeft,
    topRight,
    bottomLeft,
    bottomRight
    ];
    return panels[parseInt(Math.random() * panels.length)]
};

const sequence = [getRandomPanel()];
let sequenceToGuess = [...sequence];

const flash = (panel) => {
    return new Promise((resolve,reject) => {
        panel.className += 'active';
        setTimeout(() => {
            panel.className = panel.className.replace(
                'active',
                ''
            );
            setTimeout(() => {
                resolve();
            }, 250);
        },1000);
    });
};

let canClick = false;

const panelClicked = panelClicked => {
    if (!canClick) return;
    const expectedPanel = sequenceToGuess.shift();
    if (expectedPanel === panelClicked) {
        if (sequenceToGuess.length === 0) {
            sequence.push(getRandomPanel());
            sequenceToGuess = [...sequence];
            startFlashing();
        }
    }
    else{
        alert('game over');
    }
};

startBtn.addEventListener('click', () => {
  sequence.length = 0; // clear the sequence
  sequence.push(getRandomPanel()); // start with one panel
  sequenceToGuess = [...sequence]; // reset the guess sequence
  startFlashing(); // begin the flashing sequence
});

const startFlashing = async () => {
    for (const panel of sequence){
        await flash(panel);
    }
    canClick = true;
};

startFlashing();