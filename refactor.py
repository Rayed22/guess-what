import os

base_dir = r"C:\Users\Rayed\.gemini\antigravity\scratch\love-story"

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For You ❤️</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Playpen+Sans:wght@400;600&display=swap" rel="stylesheet">
</head>
<body data-page="{page_name}" {body_class}>
    <div id="app">
        <!-- Floating hearts container -->
        <div id="hearts-container"></div>
        {secret_heart}
        <!-- Waiting Messages UI -->
        <div id="waiting-message" class="hidden">Are you still there? 👀</div>

        {content}

    </div>
    <canvas id="confetti-canvas"></canvas>
    <script src="script.js"></script>
</body>
</html>
"""

pages = {
    "index": {
        "class": "",
        "secret": '<div id="secret-heart" class="hidden">❤️</div>',
        "content": """
        <!-- Screen 1: "Hey, guess what..." -->
        <div id="screen-1" class="screen visible fade-in">
            <h1 class="main-text suspense-text">Hey, guess what... 👀</h1>
            <div id="s1-content1" class="hidden">
                <p id="s1-p1" class="typing-text">I have something to tell you.</p>
            </div>
            <div id="s1-content2" class="hidden">
                <p id="s1-p2" class="typing-text">Actually... maybe you should guess first. 😏</p>
                <div class="buttons-container stack-buttons">
                    <button class="btn disappearing-btn" data-reply="okay">Okay, tell me 👀</button>
                    <button class="btn disappearing-btn" data-reply="guess">Hmm... let me guess 🤔</button>
                </div>
            </div>
            <div id="s1-response" class="hidden">
                <p id="s1-response-text" class="typing-text"></p>
                <div id="s1-response-continue" class="hidden mt-2">
                    <p class="typing-text hint-text">Okay, here's a hint...</p>
                    <p class="typing-text hidden" id="s1-hint1">It's something I've wanted to say to you for a while.</p>
                    <p class="typing-text hidden" id="s1-hint2">And no, it's not about pizza. 🍕</p>
                </div>
            </div>
        </div>
        """
    },
    "suspense": {
        "class": "",
        "secret": "",
        "content": """
        <!-- Screen 2: Suspense Builder -->
        <div id="screen-2" class="screen visible fade-in">
            <div id="s2-p1" class="hidden"><p class="typing-text">There is something I’ve been meaning to tell you...</p></div>
            <div id="s2-p2" class="hidden"><p class="typing-text">Something very important.</p></div>
            <div id="s2-p3" class="hidden"><p class="typing-text">Something I probably should have said a long time ago.</p></div>
            <div id="s2-p4" class="hidden"><p class="typing-text">But first...</p></div>
            <div id="s2-btn-container" class="hidden mt-2">
                <button id="s2-btn" class="btn disappearing-btn">Tell me already 😭</button>
            </div>
            <div id="s2-response" class="hidden">
                <p class="typing-text meme-text">Patience, woman 😭</p>
            </div>
        </div>
        """
    },
    "pizza": {
        "class": "",
        "secret": "",
        "content": """
        <!-- Screen 3: The Fake Confession -->
        <div id="screen-3" class="screen visible fade-in">
            <p id="s3-p1" class="typing-text hidden">Okay. I'm ready.</p>
            <p id="s3-p2" class="typing-text hidden">I have something to confess...</p>
            <p id="s3-p3" class="typing-text hidden">I...</p>
            <p id="s3-p4" class="typing-text hidden">really...</p>
            <p id="s3-p5" class="typing-text hidden">really...</p>
            
            <div id="s3-reveal" class="hidden pizza-reveal">
                <h1 class="bounce">like... pizza 🍕</h1>
                <div class="meme-card bounce mt-2" style="animation-delay: 0.5s">
                    <div class="meme-content">
                        <strong>My brain when you text me:</strong><br>
                        🧠: "Act normal."<br>
                        Me: 😭❤️😭❤️
                    </div>
                </div>
                <p class="typing-text mt-2" style="animation-duration: 0.5s">Okay okay, stop looking at me like that 😭</p>
                <div class="buttons-container pt-1">
                    <button id="s3-btn" class="btn btn-primary disappearing-btn">Seriously this time</button>
                </div>
            </div>
        </div>
        """
    },
    "confession": {
        "class": 'class="dark-mode"',
        "secret": "",
        "content": """
        <!-- Screen 4: The Actual Confession -->
        <div id="screen-4" class="screen visible fade-in dark-romantic">
            <div class="pulse-heart hidden" id="s4-heart">❤️</div>
            <p id="s4-p1" class="typing-text hidden">Okay. No more jokes.</p>
            <p id="s4-p2" class="typing-text hidden romantic-text">This one is actually for you.</p>
            
            <p id="s4-p3" class="typing-text hidden">I love...</p>
            <p id="s4-p4" class="typing-text hidden">...your smile.</p>
            <p id="s4-p5" class="typing-text hidden">...your laugh.</p>
            <p id="s4-p6" class="typing-text hidden">...the way you make ordinary days feel special.</p>
            
            <p id="s4-p7" class="typing-text hidden mt-2">And most importantly...</p>
            
            <h1 id="s4-confession" class="confession-text hidden">I LOVE YOU ❤️</h1>
        </div>
        """
    },
    "question": {
        "class": 'class="dark-mode"',
        "secret": "",
        "content": """
        <!-- Screen 5: The Question -->
        <div id="screen-5" class="screen visible fade-in dark-romantic">
            <p id="s5-p1" class="typing-text hidden">Now I have one very important question...</p>
            <h1 id="s5-q" class="question-text hidden shake">Do you love me too? 🥺👉👈</h1>
            
            <div id="s5-buttons" class="buttons-container spread-buttons hidden">
                <button id="btn-yes" class="btn btn-yes pulse-btn">I LOVE YOU TOO ❤️</button>
                <button id="btn-no" class="btn btn-no">No, I don't love you 😐</button>
            </div>
            
            <p id="s5-no-response" class="typing-text hidden mt-2 no-response-text"></p>
        </div>
        """
    },
    "end": {
        "class": 'class="dark-mode"',
        "secret": "",
        "content": """
        <!-- Screen 6: Celebration / End -->
        <div id="screen-end" class="screen visible fade-in dark-romantic">
            <h1 class="confession-text pop-in">I KNEW IT 😭❤️</h1>
            <p id="end-p1" class="typing-text hidden text-center">Come here 🫂</p>
            <div id="end-memes" class="hidden">
                <div class="meme-card bounce mt-2" style="animation-delay: 1s">
                    <div class="meme-content">
                        <strong>Me pretending I don't miss you:</strong> 🙂<br>
                        <strong>Me after 4 minutes:</strong> 🥺👉👈
                    </div>
                </div>
            </div>
            <p class="typing-text hidden pt-1" id="end-p2">More than this tiny website could ever explain.</p>
            
            <div id="end-replay-container" class="hidden mt-2">
                <button id="btn-replay" class="btn btn-secondary fade-in">Replay our little story ✨</button>
            </div>
        </div>
        """
    },
    "secret": {
        "class": 'class="dark-mode"',
        "secret": "",
        "content": """
        <!-- Secret Story Screen -->
        <div id="screen-secret" class="screen visible fade-in dark-romantic">
            <h2 class="heart-text pop-in">You found my secret ❤️</h2>
            <p id="sec-1" class="typing-text hidden mt-2">Okay... one more thing.</p>
            <p id="sec-2" class="typing-text hidden pt-1">If I could choose anyone in the world...</p>
            <h1 id="sec-3" class="confession-text hidden pt-1" style="font-size: 2rem;">I'd still choose you. ❤️</h1>
            <div id="sec-btn-container" class="hidden mt-2">
                <button id="btn-secret-return" class="btn btn-secondary">Go Back 🥺</button>
            </div>
        </div>
        """
    }
}

for name, data in pages.items():
    path = os.path.join(base_dir, f"{name}.html")
    html_content = base_html.format(
        page_name=name,
        body_class=data["class"],
        secret_heart=data["secret"],
        content=data["content"]
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)

js_content = r'''// Utility Functions
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
    
    const confettiCount = 150;
    const confettiParams = [];
    for(let i=0; i<confettiCount; i++) {
        confettiParams.push({
            x: canvas.width / 2,
            y: canvas.height / 2 + 100,
            r: Math.random() * 6 + 2,
            dx: Math.random() * 10 - 5,
            dy: Math.random() * -15 - 5,
            color: ['#E63946', '#F08080', '#FFE4E1', '#FFDAB9', '#FFF'][Math.floor(Math.random()*5)]
        });
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0,0,canvas.width, canvas.height);
        for(let i=0; i<confettiParams.length; i++) {
            let p = confettiParams[i];
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI*2, false);
            ctx.fillStyle = p.color;
            ctx.fill();
            p.x += p.dx;
            p.y += p.dy;
            p.dy += 0.3; // gravity
        }
    }
    animate();
    setTimeout(() => { canvas.style.opacity = 0; canvas.style.transition = 'opacity 2s'; }, 3000);
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

        // Start Screen 1 sequence
        await sleep(2000);
        showEl('s1-content1', 'fade-in');
        await typeText('s1-p1', "I have something to tell you.");
        await sleep(2000);
        showEl('s1-content2', 'fade-in');
        await typeText('s1-p2', "Actually... maybe you should guess first. 😏");
        
        const s1Btns = document.querySelectorAll('#s1-content2 .disappearing-btn');
        s1Btns.forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const replyType = e.target.getAttribute('data-reply');
                s1Btns.forEach(b => hideEl({id: ''} || b));
                e.target.parentElement.classList.add('hidden');
                
                showEl('s1-response', 'fade-in');
                if(replyType === 'okay') {
                    await typeText('s1-response-text', "Where's the fun in that? 😭\n\nYou have to wait a little.", 40);
                } else {
                    await typeText('s1-response-text', "Oh? You think you know me that well? 😏\n\nLet's see...", 40);
                }
                
                await sleep(1500);
                showEl('s1-response-continue', 'fade-in');
                await sleep(2000);
                showEl('s1-hint1', 'fade-in');
                await sleep(2000);
                showEl('s1-hint2', 'fade-in');
                await sleep(3000);
                
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
            switchScreen('pizza.html');
        }, {once: true});

    } else if (page === 'pizza') {
        await sleep(1000);
        showEl('s3-p1', 'fade-in');
        await sleep(2000);
        showEl('s3-p2', 'fade-in');
        await sleep(2500);
        showEl('s3-p3', 'fade-in');
        await sleep(1500);
        showEl('s3-p4', 'fade-in');
        await sleep(1500);
        showEl('s3-p5', 'fade-in');
        await sleep(2000);
        
        showEl('s3-reveal', 'fade-in');
        
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
'''

path = os.path.join(base_dir, "script.js")
with open(path, "w", encoding="utf-8") as f:
    f.write(js_content)
print("JavaScript refactored successfully.")
