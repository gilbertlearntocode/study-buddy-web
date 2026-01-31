from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pinoy Grade 1 Buddy</title>
        <style>
            body { 
                background: linear-gradient(to bottom, #87CEEB, #E0FFFF); 
                text-align: center; 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 20px; 
            }
            h1 { 
                color: #FF4500; 
                font-size: 60px; 
                margin: 20px; 
                text-shadow: 3px 3px 5px #000; 
            }
            .button { 
                font-size: 45px; 
                padding: 30px 60px; 
                margin: 25px; 
                background-color: #32CD32; 
                color: white; 
                border: none; 
                border-radius: 30px; 
                cursor: pointer; 
                box-shadow: 5px 5px 10px #888; 
            }
            .button:hover { background-color: #228B22; }
        </style>
    </head>
    <body>
        <h1>Welcome, Isaiah! 🌟</h1>
        <p style="font-size: 35px;">Ano ang gusto mong pag-aralan ngayon?</p>
        
        <button class="button" onclick="alert('Literacy time! Coming soon! 📖')">Literacy (Pagsulat at Pagbasa)</button><br>
        <button class="button" onclick="alert('Numeracy time! Coming soon! 🔢')">Numeracy (Bilang at Hugis)</button><br>
        <button class="button" onclick="alert('Makabansa time! Coming soon! 🇵🇭')">Makabansa</button><br>
        <button class="button" onclick="alert('GMRC time! Coming soon! ❤️')">GMRC (Mabuting Asal)</button>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)