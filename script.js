// Utility Functions
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
const typeText = async (elementId, text, speed = 50) => {
    const el = document.getElementById(elementId);
    if(!el) return;
    el.classList.remove('hidden');
    el.innerHTML = '';
    let isHtml = text.includes('<') && text.includes('>');
    
    if(isHtml){
        el.innerHTML = text; // Just appear immediately if it's complex HTML for brevity
        return;
    }
    
    for (let i = 0; i < text.length; i++) {
        el.innerHTML += text.charAt(i);
        await sleep(speed);
    }
};

const showEl = (id, anim = 'fade-in') => {
    const el = document.getElementById(id);
    if(el) {
        el.classList.remove('hidden');
        if(anim) el.classList.add(anim);
    }
};
const hideEl = id => {
    const el = document.getElementById(id);
    if(el) el.classList.add('hidden');
};

const switchScreen = async (newUrl) => {
    const currentScreen = document.querySelector('.screen.visible');
    if(currentScreen) currentScreen.style.opacity = '0';
    await sleep(500);
    window.location.href = newUrl;
};

function createFloatingHeart() {
    const heartsContainer = document.getElementById('hearts-container');
    if(!heartsContainer) return;
    const heart = document.createElement('div');
    heart.innerHTML = ['❤️', '💖', '✨', '💕', '🥰'][Math.floor(Math.random() * 5)];
    heart.classList.add('floating-heart');
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.animationDuration = Math.random() * 3 + 5 + 's';
    heartsContainer.appendChild(heart);
    setTimeout(() => { heart.remove(); }, 8000);
}
let heartInterval;

let waitMessagesInterval;
const waitMessages = [
    "Are you still there? 👀",
    "Don't skip ahead. 😭",
    "You're getting warmer...",
    "Okay okay, I'm getting nervous now. 🥺",
    "Patience... ❤️"
];
function triggerRandomMessage() {
    const msgEl = document.getElementById('waiting-message');
    if(!msgEl) return;
    msgEl.innerHTML = waitMessages[Math.floor(Math.random() * waitMessages.length)];
    msgEl.classList.remove('hidden');
    
    // reset animation
    msgEl.style.animation = 'none';
    msgEl.offsetHeight; 
    msgEl.style.animation = 'popup 4s ease-in-out forwards';
    
    setTimeout(() => {
        msgEl.classList.add('hidden');
    }, 4000);
}

function createConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    if(!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    // White Rose palette colors
    const colors = ['#E07090', '#FAD9E6', '#FFFFFF', '#C8476A'];
    
    for(let i=0; i<70; i++) {
        particles.push({
            x: canvas.width / 2,
            y: canvas.height / 2,
            size: Math.random() * 15 + 8,
            speedY: (Math.random() - 0.5) * 8 - 1.5, // float upwards slightly
            speedX: (Math.random() - 0.5) * 10,
            color: colors[Math.floor(Math.random() * colors.length)],
            isHeart: Math.random() > 0.4,
            opacity: 1
        });
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0,0,canvas.width, canvas.height);
        for(let i=0; i<particles.length; i++) {
            let p = particles[i];
            p.x += p.speedX;
            p.y += p.speedY;
            p.speedY -= 0.04; // float UP instead of gravity
            p.speedX *= 0.95; // air friction
            p.speedY *= 0.95;
            p.opacity -= 0.005; // slow fade
            
            if (p.opacity <= 0) continue;
            
            ctx.globalAlpha = Math.max(0, p.opacity);
            if (p.isHeart) {
                ctx.font = (p.size * 1.5) + "px Arial";
                ctx.fillText('❤️', p.x, p.y);
            } else {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size/2, 0, Math.PI*2);
                ctx.fillStyle = p.color;
                ctx.shadowBlur = 15;
                ctx.shadowColor = p.color;
                ctx.fill();
                ctx.shadowBlur = 0;
            }
        }
        ctx.globalAlpha = 1;
    }
    animate();
    setTimeout(() => { canvas.style.opacity = 0; canvas.style.transition = 'opacity 3s'; }, 4000);
}

// ---------------------------------------------------------------- //
// Logic Execution based on page
// ---------------------------------------------------------------- //
document.addEventListener("DOMContentLoaded", async () => {
    const page = document.body.getAttribute('data-page');
    heartInterval = setInterval(createFloatingHeart, page === 'confession' || page === 'question' ? 300 : (page === 'end' || page === 'secret' ? 150 : 800));

    if (page === 'index') {
        // Secret Heart Logic
        setTimeout(()=> { showEl('secret-heart'); }, 5000);
        document.getElementById('secret-heart').addEventListener('click', async () => {
            clearInterval(waitMessagesInterval);
            switchScreen('secret.html');
        });

        // Start Screen 1 sequence — two opening lines first
        await sleep(1500);
        showEl('s1-open2', 'fade-in');    // "shuno na...." fades in under "Ei....."
        await sleep(2000);
        showEl('s1-content1', 'fade-in');
        await typeText('s1-p1', "Stop whatever you're doing.");
        await sleep(2000);
        showEl('s1-content2', 'fade-in');
        await typeText('s1-p2', "I made this random little website just for you. 😏");
        
        const s1Btns = document.querySelectorAll('#s1-content2 .disappearing-btn');
        s1Btns.forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const replyType = e.target.getAttribute('data-reply');
                s1Btns.forEach(b => hideEl({id: ''} || b));
                e.target.parentElement.classList.add('hidden');
                
                showEl('s1-response', 'fade-in');
                if(replyType === 'really') {
                    await typeText('s1-response-text', "Yes really! And you have to click through it now.", 40);
                } else {
                    await typeText('s1-response-text', "Wow, the lack of trust. 😭\n\nIt's a cute virus though.", 40);
                }
                
                await sleep(1500);
                showEl('s1-response-continue', 'fade-in');
                await sleep(2000);
                showEl('s1-hint1', 'fade-in');
                await sleep(2000);
                
                switchScreen('suspense.html');
            }, {once: true});
        });

    } else if (page === 'suspense') {
        waitMessagesInterval = setInterval(() => {
            if(Math.random() > 0.6) triggerRandomMessage();
        }, 7000);

        await sleep(1000);
        showEl('s2-p1', 'fade-in');
        await sleep(2000);
        showEl('s2-p2', 'fade-in');
        await sleep(2000);
        showEl('s2-p3', 'fade-in');
        await sleep(3500); 
        showEl('s2-p4', 'fade-in');
        await sleep(1000);
        showEl('s2-btn-container', 'fade-in');
        
        document.getElementById('s2-btn').addEventListener('click', async (e) => {
            e.target.classList.add('hidden');
            showEl('s2-response', 'fade-in');
            await sleep(3000);
            switchScreen('movie.html');
        }, {once: true});

    } else if (page === 'movie') {
        await sleep(1000);
        showEl('s3-p1', 'fade-in');       // "I..."
        await sleep(2200);
        showEl('s3-p2', 'fade-in');       // "love..."
        await sleep(2200);
        showEl('s3-p3', 'fade-in');       // "you"  ← heart stops here
        await sleep(1800);

        // The twist: hide "you", show the reveal which starts with "your"
        hideEl('s3-p3');
        showEl('s3-reveal', 'fade-in');   // "your" + meme card drops in

        document.getElementById('s3-btn').addEventListener('click', async (e) => {
            e.target.classList.add('hidden');
            switchScreen('confession.html');
        });

    } else if (page === 'confession') {
        showEl('s4-heart');
        await sleep(1500);
        showEl('s4-p1', 'fade-in');
        await sleep(2500);
        showEl('s4-p2', 'fade-in');
        await sleep(2500);
        
        showEl('s4-p3', 'fade-in');
        await sleep(1500);
        showEl('s4-p4', 'fade-in');
        await sleep(1500);
        showEl('s4-p5', 'fade-in');
        await sleep(2000);
        showEl('s4-p6', 'fade-in');
        await sleep(3500);
        showEl('s4-p7', 'fade-in');
        
        await sleep(3500); // Dramatic pause
        
        const confession = document.getElementById('s4-confession');
        confession.classList.remove('hidden');
        confession.classList.add('pop-in');
        
        createConfetti();
        
        await sleep(6000);
        switchScreen('question.html');

    } else if (page === 'question') {
        await sleep(1000);
        showEl('s5-p1', 'fade-in');
        await sleep(2000);
        showEl('s5-q', 'fade-in');
        await sleep(1000);
        showEl('s5-extra', 'fade-in');   // "I love you moreeeeeee ❤️"
        await sleep(1500);
        showEl('s5-buttons', 'fade-in');
        
        // Handle No Button
        const btnNo = document.getElementById('btn-no');
        const msgEl = document.getElementById('s5-no-response');
        let noAttempts = 0;
        
        const noMessages = [
            "Are you sure? 🥺",
            "Think carefully... 😭",
            "That button seems to be malfunctioning. 🤨",
            "Interesting... because I don't believe you. 😭",
            "Okay, clearly you're just pressing the wrong button."
        ];
        
        btnNo.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            triggerNoBehavior();
        });

        btnNo.addEventListener('mouseenter', () => {
            if (window.innerWidth > 768) {
                 triggerNoBehavior(true);
            }
        });
        
        function triggerNoBehavior(isHover) {
            if(noAttempts >= noMessages.length) return;
            msgEl.innerHTML = noMessages[noAttempts];
            msgEl.classList.remove('hidden');
            msgEl.style.animation = 'none';
            msgEl.offsetHeight; 
            msgEl.style.animation = 'shake 0.5s';
            
            const container = document.getElementById('s5-buttons');
            const rangeX = container.offsetWidth - btnNo.offsetWidth;
            const rangeY = 200; 
            const randX = (Math.random() - 0.5) * rangeX;
            const randY = (Math.random() - 0) * rangeY;
            
            btnNo.style.position = 'absolute';
            btnNo.style.transform = `translate(${randX}px, ${randY}px)`;
            btnNo.style.transition = 'all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            noAttempts++;
            
            if(noAttempts >= 5) {
                btnNo.style.transform = 'scale(0)';
                setTimeout(()=> { btnNo.classList.add('hidden'); }, 300);
                setTimeout(() => {
                    msgEl.innerHTML = "You really thought I would let you click that? 😭";
                }, 1000);
            }
        }
        
        document.getElementById('btn-yes').addEventListener('click', () => {
            switchScreen('end.html');
        });

    } else if (page === 'end') {
        await sleep(2000);
        showEl('end-p1', 'fade-in');
        await sleep(1500);
        showEl('end-memes', 'fade-in');
        await sleep(3500);
        showEl('end-p2', 'fade-in');
        await sleep(2000);
        showEl('end-replay-container', 'fade-in');
        
        document.getElementById('btn-replay').addEventListener('click', () => {
            switchScreen('index.html');
        });

    } else if (page === 'secret') {
        await sleep(1500);
        await typeText('sec-1', "Okay... one more thing.");
        await sleep(1500);
        await typeText('sec-2', "If I could choose anyone in the world...");
        await sleep(2000);
        showEl('sec-3', 'pop-in');
        await sleep(1500);
        showEl('sec-btn-container', 'fade-in');
        
        document.getElementById('btn-secret-return').addEventListener('click', () => {
            switchScreen('index.html');
        });
    }
});
