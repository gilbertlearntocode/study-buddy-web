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
        <h1>Welcome, Isaiah Gabriel J. Sanchez! 🌟</h1>
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
        
        <a href="/literacy/q1?lang={lang}"><button class="button">{q1_text}</button></a>
        <button class="button" disabled>Q2: School (Coming soon!)</button><br>
        <button class="button" disabled>Q3: Community (Soon!)</button><br>
        <button class="button" disabled>Q4: Environment (Soon!)</button>
        
        <div style="margin-top:40px;">
            <img src="https://cdn.pixabay.com/photo/2016/03/31/19/58/avatar-1295429_1280.png" alt="Sticker placeholder" class="sticker">
            <!-- More stickers unlock as stars add up -->
        </div>
        
        <a href="/literacy?lang={ 'Filipino' if lang=='English' else 'English' }"><button style="font-size:30px; margin:20px; padding:15px 30px; background:#4CAF50; color:white; border:none; border-radius:20px; cursor:pointer;">Switch to { 'Filipino' if lang=='English' else 'English' }</button></a>
    </body>
    </html>
    """   

@app.route('/literacy/q1')
def q1_literacy():
    lang = request.args.get('lang', 'English')
    
    if lang == 'Filipino':
       title = "1st Quarter: Sarili at Pamilya"
       instruction = "Ano ang nagsisimula sa tunog na /a/? (Tingnan ang larawan!)"
       correct_msg = "Galing mo! ⭐"
       hint_msg = "Subukan ulit – nagsisimula ito sa /a/ tulad ng mansanas!"
    else:
       title = "1st Quarter: Self & Family"
       instruction = "What starts with the /a/ sound? (Look at the picture!)"
       correct_msg = "Great job! ⭐"
       hint_msg = "Try again – it starts with /a/ like apple!"
    
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Pinoy Grade 1 Buddy - Q1 Literacy</title>
    <style>
        body {{ background: linear-gradient(to bottom, #87CEEB, #E0FFFF); text-align: center; font-family: Arial; margin:0; padding:20px; }}
        h1 {{ color: #FF4500; font-size: 50px; margin:20px; }}
        .instruction {{ font-size: 35px; color: #333; margin:30px; }}
        .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; max-width: 800px; margin: 0 auto; }}
        .card {{ background: white; border-radius: 20px; padding: 20px; box-shadow: 5px 5px 15px #888; cursor: pointer; transition: transform 0.2s; }}
        .card:hover {{ transform: scale(1.1); }}
        .letter {{ font-size: 80px; font-weight: bold; color: #FF4500; }}
        .object-img {{ width: 150px; height: 150px; object-fit: contain; }}
        #stars {{ font-size: 60px; color: gold; margin: 40px; }}
        .back-btn {{ font-size: 30px; padding: 15px 40px; background: #FFD700; border: none; border-radius: 30px; margin-top: 40px; cursor: pointer; }}
    </style>

    <style>
        #cheerPopup {{
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(255, 215, 0, 0.95); /* gold background */
            padding: 50px;
            border-radius: 40px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.6);
            text-align: center;
            z-index: 1000;
            font-size: 50px;
            color: #FF4500;
            border: 10px solid #FFD700;
            max-width: 80%;
        }}
        #cheerPopup img {{
            width: 180px;
            margin-bottom: 20px;
        }}
        #overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.4);
            z-index: 999;
        }}
        .close-btn {{
            font-size: 35px;
            padding: 20px 50px;
            background: #32CD32;
            color: white;
            border: none;
            border-radius: 30px;
            margin-top: 30px;
            cursor: pointer;
        }}
    </style>

    <script>
        let score = 0;

        function checkAnswer(letter, isCorrect) {{
            if (isCorrect) {{
                score++;
                document.getElementById('stars').innerText = '⭐'.repeat(score);
                showCheer("{correct_msg}");
                if (score >= 3) {{
                    showCheer("Unlocked sticker! 🌟 Keep going!");
                }}
            }} else {{
                alert("{hint_msg}");
            }}
        }}

        function showCheer(message) {{
            document.getElementById('cheerMessage').innerText = message;
            document.getElementById('cheerPopup').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        }}

        function closeCheer() {{
            document.getElementById('cheerPopup').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        }}
    </script>
</head>
<body>
    <h1>{title} 🌟</h1>
    <p class="instruction">{instruction}</p>
    
    <div class="grid">
        <!-- Letter A card -->
        <div class="card">
            <div class="letter">A a</div>
            <p style="font-size:35px; font-weight:bold;">{ "Ano ang nagsisimula sa /a/?" if lang=='Filipino' else "What starts with /a/?" }</p>
        </div>

        <!-- Correct: Mansanas -->
        <div class="card" onclick="checkAnswer('A', true)">
            <img class="object-img" src="https://cdn.pixabay.com/photo/2016/09/29/08/33/apple-1702316_1280.jpg" alt="Mansanas">
            <p style="font-size:28px;">Mansanas <small>(Apple)</small></p>
        </div>

        <!-- Wrong examples in Filipino -->
        <div class="card" onclick="checkAnswer('A', false)">
            <img class="object-img" src="https://cdn.pixabay.com/photo/2018/06/11/23/15/basketball-3469628_960_720.jpg" alt="Bola">
            <p style="font-size:28px;">Bola <small>(Ball)</small></p>
        </div>

        <div class="card" onclick="checkAnswer('A', false)">
            <img class="object-img" src="https://cdn.pixabay.com/photo/2024/03/07/10/38/simba-8618301_1280.jpg" alt="Pusa">
            <p style="font-size:28px;">Pusa <small>(Cat)</small></p>
        </div>
    </div>
    
    <div id="stars">⭐⭐⭐ (start with 0)</div>
    
    <a href="/literacy?lang={lang}"><button class="back-btn">Back to Literacy Menu</button></a>

    <!-- Cheer Popup -->
    <div id="overlay"></div>
    <div id="cheerPopup">
        <img src="https://cdn.pixabay.com/photo/2020/12/10/05/11/spider-man-5819368_1280.png" alt="Yay!">
        <p id="cheerMessage"></p>
        <button class="close-btn" onclick="closeCheer()">OK! 🌟</button>
    </div>
</body>
</html>
"""
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)