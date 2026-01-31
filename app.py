from flask import Flask, request

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
        
        <a href="/literacy"><button class="button">Literacy (Pagsulat at Pagbasa)</button></a>
        <button class="button" onclick="alert('Numeracy time! Coming soon! 🔢')">Numeracy (Bilang at Hugis)</button><br>
        <button class="button" onclick="alert('Makabansa time! Coming soon! 🇵🇭')">Makabansa</button><br>
        <button class="button" onclick="alert('GMRC time! Coming soon! ❤️')">GMRC (Mabuting Asal)</button>
    </body>
    </html>
    """
@app.route('/literacy')
def literacy_hub():
    # Simple session for language (later add real toggle)
    lang = request.args.get('lang', 'English')  # ?lang=Filipino to switch
    
    if lang == 'Filipino':
        title = "Mga Laro sa Pagbasa at Pagsulat!"
        q1_text = "1st Quarter: Sarili at Pamilya"
        # Add more bilingual texts
    else:
        title = "Literacy Games!"
        q1_text = "1st Quarter: Self & Family"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pinoy Grade 1 Buddy - Literacy</title>
        <style>
            body {{ background: linear-gradient(to bottom, #87CEEB, #E0FFFF); text-align: center; font-family: Arial; margin:0; padding:20px; }}
            h1 {{ color: #FF4500; font-size: 60px; text-shadow: 3px 3px #000; }}
            .button {{ font-size: 45px; padding: 30px 60px; margin: 25px; background: #32CD32; color:white; border:none; border-radius:30px; box-shadow:5px 5px #888; cursor:pointer; }}
            .button:hover {{ background: #228B22; }}
            .sticker {{ width: 100px; opacity: 0.5; }}  /* unlocked ones full opacity later */
        </style>
    </head>
    <body>
        <h1>{title} 📖</h1>
        <p style="font-size:35px;">Pumili ng laro, Isaiah! 🌟</p>
        
        <a href="/literacy/q1"><button class="button">{q1_text}</button></a><br>
        <button class="button" disabled>Q2: School (Coming soon!)</button><br>
        <button class="button" disabled>Q3: Community (Soon!)</button><br>
        <button class="button" disabled>Q4: Environment (Soon!)</button>
        
        <div style="margin-top:40px;">
            <img src="https://cdn.pixabay.com/photo/2016/03/31/19/58/avatar-1295429_1280.png" alt="Sticker placeholder" class="sticker">
            <!-- More stickers unlock as stars add up -->
        </div>
        
        <a href="/?lang={ 'Filipino' if lang=='English' else 'English' }"><button style="font-size:30px; margin:20px;">Switch to { 'Filipino' if lang=='English' else 'English' }</button></a>
    </body>
    </html>
    """   

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)