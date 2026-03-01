from flask import Flask, jsonify, render_template_string
import random

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
<title>Para Mi Mejor Amiga 💖</title>
<style>
body{
    margin:0;
    text-align:center;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#ff758c,#ff7eb3);
    color:white;
}
h1{
    margin-top:80px;
    font-size:45px;
}
button{
    padding:15px 35px;
    font-size:20px;
    border:none;
    border-radius:30px;
    cursor:pointer;
    background:white;
    color:#ff4d6d;
    transition:0.3s;
}
button:hover{
    transform:scale(1.1);
    background:#ff4d6d;
    color:white;
}
#frase{
    margin-top:40px;
    font-size:24px;
    min-height:80px;
    padding:20px;
}

/* Marca de agua personalizada */
.marca{
    position:fixed;
    bottom:15px;
    right:20px;
    font-size:15px;
    opacity:0.7;
    font-style:italic;
}
</style>
</head>
<body>

<h1>🎂 Feliz Cumpleaños Mejor Amiga 🎂</h1>

<button onclick="nuevaFrase()">Presiona aquí 💖</button>

<div id="frase"></div>

<div class="marca">✨ Hecho por José, tu mejor amigo 💙</div>

<script>
function nuevaFrase(){
    fetch("/frase")
    .then(response => response.json())
    .then(data => {
        let contenedor = document.getElementById("frase");
        contenedor.style.opacity = 0;
        setTimeout(()=>{
            contenedor.innerHTML = data.frase;
            contenedor.style.opacity = 1;
        },200);
    });
}
</script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(html)

@app.route("/frase")
def frase():
    return jsonify({"frase": generar_frase()})

if __name__ == "__main__":
    app.run(debug=True)