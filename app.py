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
    
    
    title = "Mga Laro sa Pagbasa at Pagsulat!"
    q1_text = "1st Quarter: Sarili at Pamilya"
    
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
        
        <a href="/literacy/q1"><button class="button">{q1_text}</button></a>
        <button class="button" disabled>Q2: School (Coming soon!)</button><br>
        <button class="button" disabled>Q3: Community (Soon!)</button><br>
        <button class="button" disabled>Q4: Environment (Soon!)</button>
        
        
        
        
    </body>
    </html>
    """   

@app.route('/literacy/q1')
def q1_literacy():
    title = "1st Quarter: Sarili at Pamilya"
    instruction = "Sino 'to? Tap ang tamang sagot!"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pinoy Grade 1 Buddy - Q1 Literacy</title>
        <style>
            body {{ background: linear-gradient(to bottom, #87CEEB, #E0FFFF); text-align: center; font-family: Arial; margin:0; padding:20px; }}
            h1 {{ color: #FF4500; font-size: 50px; margin:20px; }}
            .instruction {{ font-size: 35px; color: #333; margin:30px; }}
            .family-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 30px; max-width: 90%; margin: 40px auto; padding: 20px; }}
            .family-card {{ background: white; border-radius: 25px; padding: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); text-align: center; cursor: pointer; transition: transform 0.3s ease; }}
            .family-card:hover {{ transform: scale(1.15); box-shadow: 0 15px 30px rgba(0,0,0,0.3); }}
            .family-card img {{ width: 140px; height: 140px; object-fit: contain; margin-bottom: 15px; }}
            .family-card p {{ font-size: 32px; font-weight: bold; color: #FF4500; margin: 0; }}
            #stars {{ font-size: 60px; color: gold; margin: 40px; }}
            .back-btn {{ font-size: 30px; padding: 15px 40px; background: #FFD700; border: none; border-radius: 30px; margin-top: 40px; cursor: pointer; }}
            #cheerPopup {{
                display: none;
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: rgba(255, 215, 0, 0.95);
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
            #cheerPopup img {{ width: 180px; margin-bottom: 20px; }}
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

            function showFamily(family) {{
                let questionDiv = document.getElementById('familyQuestion');
                questionDiv.style.display = 'block';

                let questionText = "";
                if (family === 'mama') questionText = "Sino 'to? Mama ko!";
                else if (family === 'papa') questionText = "Sino 'to? Papa ko!";
                else if (family === 'lola at lolo') questionText = "Sino 'to? Lola Sim at Lolo Elpeds!";
                else if (family === 'lola') questionText = "Sino 'to? Lola J!";

                questionDiv.innerHTML = questionText + '<br>' +
                    '<button class="card" onclick="checkFamily(true)">Oo! ' + questionText.split('? ')[1] + '</button>' +
                    '<button class="card" onclick="checkFamily(false)">Hindi!</button>';
            }}

            function checkFamily(isCorrect) {{
                if (isCorrect) {{
                    score++;
                    document.getElementById('stars').innerText = '⭐'.repeat(score);
                    showCheer("Galing mo! ⭐");
                }} else {{
                    alert("Subukan ulit!");
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
        
        <div class="family-grid">
            <div class="family-card" onclick="showFamily('mama')">
                <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-1/611354577_3995415380588514_2586807128409073820_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=100&ccb=1-7&_nc_sid=1d2534&_nc_eui2=AeEGbHUy7-V-LbdavGEahJEmxhitcC7GC1zGGK1wLsYLXPuItPEesDAvDSmh4C00hc74r9BtUNdYvalKqdLEgCyD&_nc_ohc=tmSq8hsDIx0Q7kNvwGG3jl2&_nc_oc=AdmKzIfkU9MkIgRKCRXB3yjsI43wbdUSoA2HOU0JMRXJ-XpglJkiHEES9Tauf5fqIU8&_nc_zt=24&_nc_ht=scontent.fmnl9-3.fna&_nc_gid=VVSmYtRTbDSerxxp9tClPQ&oh=00_AftSzcE2CxyZoRMWU5F_xqnwTyeUOo3j3lQtPY2ZRSVjAw&oe=69836E00" alt="Mama">
                <p>Mama ko</p>
            </div>
            <div class="family-card" onclick="showFamily('papa')">
                <img src="https://scontent.fmnl4-4.fna.fbcdn.net/v/t39.30808-6/490729603_2672799912890480_7292628436484835537_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeFRRmct0ACtOmOu0u3T8ggEz8wD-XR_IeDPzAP5dH8h4IVsOUZtv3jkoPbjiqTqaqTbGgVimR9o0TTyyXe1QhMC&_nc_ohc=Nfd-jZ77h6cQ7kNvwFTVF4a&_nc_oc=AdlYh91ZW441IRwRS949Ry1fVJDENJ40Xa1Xml5RPK2FrZACiUVIyFcpcE4Gl4LiX7Y&_nc_zt=23&_nc_ht=scontent.fmnl4-4.fna&_nc_gid=4CGMbduUgbVO3aRMD95z0A&oh=00_Aftyb1rQmDDJeCL8ImiOdTOllqX3ctfFPvWPg2h7kBf2fA&oe=6984487D" alt="Papa">
                <p>Papa ko</p>
            </div>
            <div class="family-card" onclick="showFamily('lola at lolo')">
                <img src="https://scontent.fmnl4-6.fna.fbcdn.net/v/t39.30808-6/498526844_3031634043658081_3409065761940624395_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=cf85f3&_nc_eui2=AeFbK8HDXqqqXA-kPWgqrVZlCQUhVQHW2yUJBSFVAdbbJecO_PvUQjVk6LA_PEX0FK56gA8HIdm-ZFv-unI9Puol&_nc_ohc=GGzsgfk5i-EQ7kNvwGQYTU7&_nc_oc=AdlEOq8hPAnJp6Sh4u4MZYZpRag9NK7L7TA6ltWk_Cv_1R8xAFrupl3eh93yETswZgg&_nc_zt=23&_nc_ht=scontent.fmnl4-6.fna&_nc_gid=Bwzdhq7uHqSlAMr_YUk3Hg&oh=00_AfvOgcY51zPhRnuvdJnWgmMPr-Q9xAS2kcIiRN8addNhaw&oe=69846A12" alt="Lola">
                <p>Lola at Lolo ko</p>
            </div>


            <div class="family-card" onclick="showFamily('lola')">
                <img src="https://scontent.fmnl4-2.fna.fbcdn.net/v/t39.30808-6/487204319_2657165571120581_8525525069188274080_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=cf85f3&_nc_eui2=AeEdJiuY270iu_9QfZ-LDwPhW6fOSYfFvGhbp85Jh8W8aCBArAJ81EZ0fLcZY6SJUhfOMNax69IT4IEBI4ijBJrR&_nc_ohc=a8R90K1MxqgQ7kNvwE1XqjU&_nc_oc=AdmKst7ORpTkxDComK9u-P_Xqrjg-W2w9h7WpVsRvA6MR4cAGAhxdQIAy3K056hGHOI&_nc_zt=23&_nc_ht=scontent.fmnl4-2.fna&_nc_gid=Xu6mDfsuQNk_U5OBfFApwQ&oh=00_Afs-dc2p1O0DrJp4jSjmWLTp1BOourU8vj7puiPTLX3jcQ&oe=69845996" alt="Lola">
                <p>Lola</p>
            </div>

            

    
        
    
            
        </div>

        <div id="familyQuestion" style="font-size:40px; margin:40px; display:none;"></div>

        <div id="stars">⭐⭐⭐ (start with 0)</div>
        
        <a href="/literacy"><button class="back-btn">Bumalik sa Literacy Menu</button></a>

        <div id="overlay"></div>
        <div id="cheerPopup">
            <img src="https://cdn.pixabay.com/animation/2022/10/27/12/57/12-57-22-874_512.gif" alt="Yay!">
            <p id="cheerMessage"></p>
            <button class="close-btn" onclick="closeCheer()">OK! 🌟</button>
        </div>
    </body>
    </html>
    """
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)