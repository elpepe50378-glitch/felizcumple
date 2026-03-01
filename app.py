from flask import Flask, jsonify, render_template_string
import random
import os

app = Flask(__name__)

inicios = [
    "Desde que llegaste a mi vida",
    "No sé cómo lo hiciste pero",
    "El mundo es mejor porque",
    "Cada día agradezco que",
    "Si tuviera que describirte diría que"
]

emociones = [
    "la haces más brillante",
    "llenaste todo de alegría",
    "eres pura luz",
    "eres una bendición disfrazada de amiga",
    "eres esa paz que todos necesitan"
]

cierres = [
    "y nunca quiero perder eso 💖",
    "y eso te hace única 💫",
    "y por eso hoy celebramos tu existencia 🎉",
    "y siempre voy a estar para ti 🤍",
    "y el mundo necesita más personas como tú 🌸"
]

def generar_frase():
    return f"{random.choice(inicios)} {random.choice(emociones)} {random.choice(cierres)}"

html = """
<!DOCTYPE html>
<html>
<head>
<title>Feliz Cumpleaños 💖</title>
<style>
body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background: linear-gradient(-45deg,#ff758c,#ff7eb3,#ffb199,#ff758c);
    background-size:400% 400%;
    animation: fondo 10s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

@keyframes fondo{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.card{
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    padding:40px;
    border-radius:25px;
    text-align:center;
    color:white;
    width:90%;
    max-width:500px;
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

h1{
    margin-bottom:20px;
}

button{
    padding:12px 30px;
    font-size:18px;
    border:none;
    border-radius:30px;
    cursor:pointer;
    background:white;
    color:#ff4d6d;
    transition:0.3s;
}

button:hover{
    transform:scale(1.1);
}

#frase{
    margin-top:25px;
    font-size:20px;
    min-height:70px;
}

.marca{
    position:fixed;
    bottom:10px;
    right:15px;
    font-size:14px;
    color:white;
    opacity:0.8;
}
</style>
</head>
<body>

<div class="card">
    <h1>🎂 Feliz Cumpleaños 🎂</h1>
    <button onclick="nuevaFrase()">Presiona aquí 💖</button>
    <div id="frase"></div>
</div>

<div class="marca">✨ Hecho por José, tu mejor amigo 💙</div>

<script>
function nuevaFrase(){
    fetch("/frase")
    .then(res => res.json())
    .then(data => {
        let f = document.getElementById("frase");
        f.style.opacity = 0;
        setTimeout(()=>{
            f.innerHTML = data.frase;
            f.style.opacity = 1;
        },200);

        lanzarConfeti();
    });
}

function lanzarConfeti(){
    for(let i=0;i<30;i++){
        let c=document.createElement("div");
        c.style.position="fixed";
        c.style.width="8px";
        c.style.height="8px";
        c.style.backgroundColor=`hsl(${Math.random()*360},100%,50%)`;
        c.style.left=Math.random()*100+"vw";
        c.style.top="-10px";
        c.style.borderRadius="50%";
        c.style.animation="caer 3s linear";
        document.body.appendChild(c);
        setTimeout(()=>c.remove(),3000);
    }
}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/frase")
def frase():
    return jsonify({"frase": generar_frase()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
