from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tulong sa Sugal - Stop Gambling PH</title>
        <style>
            body { background: linear-gradient(to bottom, #F0F8FF, #E0FFFF); text-align: center; font-family: Arial; padding: 30px; }
            h1 { color: #228B22; font-size: 60px; margin: 40px 0; }
            p { font-size: 35px; color: #333; margin: 30px 0; }
            .big-btn { 
                display: inline-block; 
                font-size: 40px; 
                padding: 30px 60px; 
                background: #32CD32; 
                color: white; 
                text-decoration: none; 
                border-radius: 40px; 
                box-shadow: 8px 8px #888; 
                cursor: pointer; 
                margin: 30px 0; 
                width: 80%; 
                max-width: 500px; 
            }
            .big-btn:hover { background: #228B22; }
        </style>
    </head>
    <body>
        <h1>You are not alone</h1>
        <p>Kung adik ka sa online gambling, hindi ka nag-iisa. May paraan para tumigil at magsimula ulit.</p>

        <a href="/self-check" class="big-btn">Self-Check (20 Tanong)</a>
        <a href="/paano-tumigil" class="big-btn">Paano Tumigil</a>
        <a href="/mga-kwento" class="big-btn">Mga Kwento ng Iba</a>

        <!-- Scrolling Ticker -->
<div style="background: #FFD700; color: #228B22; overflow: hidden; white-space: nowrap; padding: 15px 0; font-size: 32px; font-weight: bold; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
    <div style="display: inline-block; animation: ticker 200s linear infinite;">
        &nbsp;&nbsp;&nbsp;&nbsp;
        "One day at a time lang, bro... 6 months clean na ako, wag magmayabang, lowkey lang..." &nbsp;&nbsp;&nbsp;&nbsp;
        "Nagsimula sa sabong, umabot sa utang sa lending apps... pero tumigil ako, kaya mo rin..." &nbsp;&nbsp;&nbsp;&nbsp;         
        "Hindi ko sinabi sa asawa ko noon... pero nung umamin ako, naging suporta siya..." &nbsp;&nbsp;&nbsp;&nbsp;
        "Relapse happened 3 times... pero tumayo ulit ako. Isa-isang araw lang talaga..." &nbsp;&nbsp;&nbsp;&nbsp;
        "Join GA PH, libre at walang judgment... changed my life..." &nbsp;&nbsp;&nbsp;&nbsp;
        "From negative balance to feeding my family again... salamat sa support..." &nbsp;&nbsp;&nbsp;&nbsp;
        "Wag mahiya humingi ng tulong... hotline 1553, 24/7..." &nbsp;&nbsp;&nbsp;&nbsp;
        "Kung nahihirapan ka ngayon, alam ko 'yung pakiramdam... pero may pag-asa..." &nbsp;&nbsp;&nbsp;&nbsp;
        "2 years clean na pero pag may load sa gcash parang may demonyo na nagsasabi 'one spin lang' grabe talaga...." &nbsp;&nbsp;&nbsp;&nbsp;
        "Nanalo ako 50k isang gabi sa bingo plus kinabukasan ubos na naman + utang pa sa lending 3 apps" &nbsp;&nbsp;&nbsp;&nbsp;
        "Wife ko nalaman na 200k utang ko sa online casino sabi niya 'bakit di mo sinabi?' kasi nahihiya ako sobra"    &nbsp;&nbsp;&nbsp;&nbsp;
        "From 1k bet naging 10k per game hanggang sa pawn ng motor para makapaglaro ulit tanga talaga ako nun"    &nbsp;&nbsp;&nbsp;&nbsp;
        "Every payday diretso sa sabong app. Mga anak ko baon wala na. Ngayon 3 months clean pero takot pa rin ako"    &nbsp;&nbsp;&nbsp;&nbsp;
        "Relapse ako last week after 8 months. Isang text lang ng tropa 'game tayo' tapos ubos 15k"    &nbsp;&nbsp;&nbsp;&nbsp;
        "Nagtatago ako sa CR para maglaro kasi nahihiya sa pamilya. Feeling ko demonyo na 'ko"    &nbsp;&nbsp;&nbsp;&nbsp;
        "Utang ko sa 5-6 umabot 80k dahil sa color game. bininta ko na cellphone ko para mabayaran"    &nbsp;&nbsp;&nbsp;&nbsp;
        "One day clean pa lang ako pero grabe yung panghihinayang sa pera na nasayang. Kaya ko pa ba 'to?"    &nbsp;&nbsp;&nbsp;&nbsp;
        "Sumali ako sa GA PH last month. Akala ko ako lang, pero marami pala kaming ganito. Salamat sa mga nag-share"    &nbsp;&nbsp;&nbsp;&nbsp;

    </div>
        <!-- YouTube Video in the empty space -->
    <div style="margin: 60px auto; max-width: 800px; padding: 20px; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <h2 style="color: #228B22; font-size: 40px; margin-bottom: 20px;">Pagharap sa Kamatayan</h2>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ANJ9qxx_INY?si=wsK-lB8zSxRoU4ig" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        <p style="font-size: 28px; margin-top: 20px;">(Video mula sa YouTube - safe at helpful para sa recovery journey mo)</p>
    </div>
</div>

<style>
    @keyframes ticker {
        0% { transform: translateX(0%); }
        100% { transform: translateX(-100%); }
    }
</style>
                
        
    </body>
    </html>
    """

@app.route('/paano-tumigil')
def paano_tumigil():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Paano Tumigil sa Sugal - Tulong sa Sugal PH</title>
        <style>
            body { 
                background: linear-gradient(to bottom, #F0F8FF, #E0FFFF); 
                text-align: center; 
                font-family: Arial, sans-serif; 
                margin:0; 
                padding: 30px; 
                color: #333; 
            }
            h1 { 
                color: #228B22; 
                font-size: 60px; 
                margin: 40px 0; 
            }
            h2 { 
                color: #006400; 
                font-size: 45px; 
                margin: 50px 0 20px; 
            }
            ul { 
                list-style: none; 
                padding: 0; 
                max-width: 800px; 
                margin: 0 auto 40px; 
            }
            li { 
                font-size: 32px; 
                margin: 25px 0; 
                background: white; 
                padding: 25px; 
                border-radius: 20px; 
                box-shadow: 0 5px 15px rgba(0,0,0,0.1); 
            }
            .btn { 
                font-size: 40px; 
                padding: 30px 60px; 
                background: #32CD32; 
                color: white; 
                border: none; 
                border-radius: 40px; 
                cursor: pointer; 
                margin: 40px 20px; 
            }
            .btn:hover { background: #228B22; }
            .hotline { 
                font-size: 38px; 
                color: #FF4500; 
                font-weight: bold; 
                margin: 30px 0; 
            }
        </style>
    </head>
    <body>
        <h1>Paano Tumigil sa Online Sugal</h1>
        <p style="font-size:35px;">Hindi madali, pero marami nang nakagawa nito. Kaya mo rin tumigil. Simulan natin ngayon.</p>

        <h2>Mga Unang Hakbang</h2>
        <ul>
            <h2>Mga Unang Hakbang (First 1–7 Days)</h2>
<ul>
    <li><strong>I-delete agad ang lahat ng gambling apps</strong> sa phone mo (sabong, casino, poker, slot, color game, etc.) at sa tablet/computer kung meron.</li>
    <li><strong>I-block ang websites</strong> sa browser:
        <ul style="font-size:28px; margin-left:40px;">
            <li>Gamitin ang extension na BlockSite (Chrome) o StayFocusd</li>
            <li>Sa phone: i-on ang Digital Wellbeing / Screen Time limit sa Android o Screen Time sa iPhone para sa gambling sites</li>
            <li>Pinaka-effective: bumalik sa basic phone (keypad lang) sa unang 1–3 months — walang smart apps na madaling i-download ulit</li>
        </ul>
    </li>
    <li><strong>Sabihin sa isang trusted person</strong> (asawa, magulang, kapatid, best friend):  
        "May gambling problem ako at gusto ko talagang tumigil. Tulungan mo ako."</li>
    <li><strong>Iwasan muna ang mga kaibigan/grupo</strong> na nag-e-encourage o naglalaro pa rin (kahit online chat). Sabihin mo: "Bro, pauwi na ako, may lakad ako."</li>
    <li><strong>Lagyan ng limit o i-freeze ang GCash/BPI/Maya card</strong> na ginagamit sa sugal:
        <ul style="font-size:28px; margin-left:40px;">
            <li>GCash: i-request na i-limit ang transfers or i-pause ang account temporarily</li>
            <li>Bank: tawagan ang bank para i-block ang online transactions for 30 days</li>
        </ul>
    </li>
    <li><strong>I-log out at palitan ang passwords</strong> ng lahat ng gambling accounts — gamitin ang "Forgot Password" para hindi ka makalogin ulit.</li>
</ul>

<h2>Paano Manatiling Matatag (After First Week)</h2>
<ul>
    <li><strong>Punan ang oras mo ng ibang bagay</strong>:
        <ul style="font-size:28px; margin-left:40px;">
            <li>Mag-simula ng hobby (basketball, gym, music, gardening, church, videoke with family)</li>
            <li>Mag-volunteer sa barangay o church — nakaka-busy at nakaka-give back ka pa kay Lord at sa community</li>
            <li>Mag-aral ulit ng bagong skill (YouTube tutorials: cooking, repairs, online courses)</li>
        </ul>
    </li>
    <li><strong>Mag-journal araw-araw</strong> (kahit 5 minutes lang sa phone notes or sa notebook para iwas muna sa smart phone):
        "Ngayon, ano ang naramdaman ko nang hindi ako naglaro? Ano ang pinakamahirap?"
        "Ano ang na-save ko ngayon na pera dahil hindi ako nag-sugal?"
    </li>
    <li><strong>Magtakda ng maliit na goal</strong>:
        "Ngayong linggo: walang sugal kahit piso"
        "Sa susunod na buwan: maibalik ang 50% ng utang ko sa pamilya"
    </li>
    <li><strong>Sumali sa support group</strong> (kahit online muna):
        <ul style="font-size:28px; margin-left:40px;">
            <li>Gamblers Anonymous PH (search sa Facebook or Google)</li>
            <li>Online forums like Reddit r/problemgambling or Filipino groups sa FB</li>
            <li>Kung may budget: counseling sa In Touch Community Services</li>
        </ul>
    </li>
    <li><strong>Tandaan: relapse/lapse is normal</strong> — kung madulas ka, huwag sumuko. Tumayo ulit, sabihin sa trusted person, at magsimula ulit sa Day 1.</li>
    <li><strong>Ipagdasal / magdasal</strong> kung religious ka — maraming nagsasabing malaking tulong ang faith sa pagtigil.</li>
</ul>

<p style="font-size:35px; color:#228B22; margin:50px 0;">
    <strong>One day at a time lang. Kaya mo 'yan. At wag maging mayabang kung di kana nakapagsugal sa mahabang panahon ang addiction ay nariyan lang yan, nakokontrol pero di nagagamot. Lowkey lang.</strong>
</p>

        <h2>Kung Nahihirapan Ka</h2>
        <p class="hotline">Tumawag o mag-text sa mga ito (libre at confidential):</p>
        <ul>
            <li><strong>DOH Mental Health Hotline</strong>: 1553 (nationwide, 24/7)</li>
            <li><strong>PAGCOR Helpline</strong>:  0915 938 2808 o email ResponsibleGaming@pagcor.ph</li>
            <li><strong>HopeLine PH</strong>: 0917-558-4673 (text/call, 24/7)</li>
            <li><strong>In Touch Community Services</strong>: 0917-800-1123 (counseling)</li>
        </ul>

        <h2>Paano Manatiling Matatag</h2>
        <ul>
            <li>Maglaan ng bagong hobby (laro ng basketball, gym, music, church)</li>
            <li>Mag-journal araw-araw: "Ngayon, ano ang naramdaman ko nang hindi ako naglaro?"</li>
            <li>Sumali sa support group (online o local, tulad ng Gamblers Anonymous PH)</li>
            <li>Tandaan: Isa-isang araw lang. Kung madulas ka, tumayo ulit — hindi ka nag-iisa.</li>
        </ul>
        <a href="/matagal-na-tumigil"><button class="btn">Mga Paalala Kapag Matagal Ka Nang Tumigil</button></a>
        <a href="/"><button class="btn">Bumalik sa Home</button></a>

        <h2>Magkwento Ka Rin (Anonymous OK)</h2>
<p style="font-size:30px;">Kung gusto mong ibahagi ang kwento mo para makatulong sa iba, sulat mo lang sa baba. Hindi mo kailangang maglagay ng pangalan o personal info ang mahalaga ay ang storya.</p>

<form action="https://formspree.io/f/mvzqoklw" method="POST">
    <textarea name="kwento" rows="10" placeholder="Kwento mo dito... ( anonymous)" style="width:90%; max-width:700px; font-size:28px; padding:20px; border-radius:15px; border:2px solid #32CD32; margin:20px 0;"></textarea><br>
    
    <input type="text" name="pangalan" placeholder="Pangalan (opsyonal)" style="font-size:28px; padding:15px; width:80%; max-width:500px; border-radius:15px; border:2px solid #32CD32; margin:10px 0;"><br>
    
    <input type="email" name="_replyto" placeholder="Email mo (opsyonal, para makapag-reply ako)" style="font-size:28px; padding:15px; width:80%; max-width:500px; border-radius:15px; border:2px solid #32CD32; margin:10px 0;"><br>
    
    <button type="submit" class="btn">Ipadala ang Kwento</button>
</form>

<p style="font-size:28px; margin-top:40px;">Salamat sa pagbabahagi mo. Malaking tulong 'to sa iba.</p>
        
    </body>
    </html>
   """    
@app.route('/matagal-na-tumigil')
def matagal_na_tumigil():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mga Paalala Kapag Matagal Ka Nang Tumigil - Tulong sa Sugal PH</title>
        <style>
            body { 
                background: linear-gradient(to bottom, #F0F8FF, #E0FFFF); 
                text-align: center; 
                font-family: Arial, sans-serif; 
                margin:0; 
                padding: 30px; 
                color: #333; 
            }
            h1 { 
                color: #228B22; 
                font-size: 55px; 
                margin: 40px 0; 
            }
            h2 { 
                color: #006400; 
                font-size: 40px; 
                margin: 50px 0 20px; 
            }
            ul { 
                list-style: none; 
                padding: 0; 
                max-width: 800px; 
                margin: 0 auto 40px; 
            }
            li { 
                font-size: 32px; 
                margin: 25px 0; 
                background: white; 
                padding: 25px; 
                border-radius: 20px; 
                box-shadow: 0 5px 15px rgba(0,0,0,0.1); 
            }
            .btn { 
                font-size: 40px; 
                padding: 30px 60px; 
                background: #32CD32; 
                color: white; 
                border: none; 
                border-radius: 40px; 
                cursor: pointer; 
                margin: 40px 20px; 
            }
            .btn:hover { background: #228B22; }
        </style>
    </head>
    <body>
        <h1>Mga Paalala Kapag Matagal Ka Nang Tumigil</h1>
        <p style="font-size:35px;">Isa-isang araw lang. Kaya mo 'yan. At wag maging mayabang kung di kana nakapagsugal sa mahabang panahon — ang addiction ay nariyan lang yan, nakokontrol pero di nagagamot. Lowkey lang.</p>

        <h2>Mga Bagay na Dapat Tandaan Palagi</h2>
        <ul>
            <li>One day at a time lang — wag isipin ang "forever" o "one year clean". Focus ka lang sa ngayong araw: "Ngayon, hindi ako naglaro."</li>
            <li>Wag magmalaki o mag-post sa social media na "6 months/1 year clean na ako". Minsan yung pride na 'yon mismo ang nagiging dahilan para mag-relapse.</li>
            <li>Lowkey lang ang pagpapanatili — sabihin mo lang sa sarili mo o sa trusted person. Hindi kailangan ipakita sa lahat.</li>
            <li>Ang urge ay hindi nawawala — pwede pa ring dumating kahit after years. Pero natututo kang i-manage siya (deep breath, tawag sa kaibigan, lakad, dasal, etc.).</li>
            <li>Kung madulas ka ulit — wag sumuko. Relapse is part of recovery. Tumayo ka ulit, sabihin sa trusted person, at bumalik sa Day 1. Walang "sayang" — bawat araw na clean ay panalo pa rin.</li>
            <li>Patuloy na punan ang buhay mo ng ibang bagay — hobby, pamilya, trabaho, church, exercise. Kung walang laman ang oras mo, madaling bumalik ang sugal.</li>
            <li>Tandaan: Hindi ka "mahina" o "bobo" dahil may addiction ka. Maraming matitibay, matatalino na tao ang nahulog dito. Pero mas matibay at matalino ka ngayon dahil lumalaban ka. Hangat na kokonsensya ka pa sa ginagawa mo, ikaw pa yan there is something in you na hindi lubusan nakokontrol ng addiction mo. Yan mismo ang dahilan bakit titigil ka pagsusugal. Now na!</li>
        </ul>

        <p style="font-size:38px; color:#228B22; margin:60px 0;">
            <strong>Isa-isang araw lang. Lowkey lang. Kaya mo 'yan.</strong>
        </p>
         
        <a href="/paano-tumigil"><button class="btn">Bumalik sa Paano Tumigil</button></a>
        <a href="/"><button class="btn">Bumalik sa Home</button></a>

        <h2>Magkwento Ka Rin (Anonymous OK)</h2>
<p style="font-size:30px;">Kung gusto mong ibahagi ang kwento mo para makatulong sa iba, sulat mo lang sa baba. Hindi mo kailangang maglagay ng pangalan o personal info ang mahalaga ay ang storya.</p>

<form action="https://formspree.io/f/mvzqoklw" method="POST">
    <textarea name="kwento" rows="10" placeholder="Kwento mo dito... ( anonymous)" style="width:90%; max-width:700px; font-size:28px; padding:20px; border-radius:15px; border:2px solid #32CD32; margin:20px 0;"></textarea><br>
    
    <input type="text" name="pangalan" placeholder="Pangalan (opsyonal)" style="font-size:28px; padding:15px; width:80%; max-width:500px; border-radius:15px; border:2px solid #32CD32; margin:10px 0;"><br>
    
    <input type="email" name="_replyto" placeholder="Email mo (opsyonal, para makapag-reply ako)" style="font-size:28px; padding:15px; width:80%; max-width:500px; border-radius:15px; border:2px solid #32CD32; margin:10px 0;"><br>
    
    <button type="submit" class="btn">Ipadala ang Kwento</button>
</form>

<p style="font-size:28px; margin-top:40px;">Salamat sa pagbabahagi mo. Malaking tulong 'to sa iba.</p>
        

    </body>
    </html>
    """

@app.route('/mga-kwento')
def mga_kwento():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mga Kwento ng Iba - Tulong sa Sugal PH</title>
        <style>
            body { 
                background: linear-gradient(to bottom, #F0F8FF, #E0FFFF); 
                text-align: center; 
                font-family: Arial, sans-serif; 
                margin:0; 
                padding: 30px; 
                color: #333; 
            }
            h1 { 
                color: #228B22; 
                font-size: 55px; 
                margin: 40px 0; 
            }
            .story { 
                max-width: 800px; 
                margin: 40px auto; 
                font-size: 32px; 
                line-height: 1.6; 
                text-align: left; 
                background: white; 
                padding: 40px; 
                border-radius: 25px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
            }
            .btn { 
                font-size: 40px; 
                padding: 30px 60px; 
                background: #32CD32; 
                color: white; 
                border: none; 
                border-radius: 40px; 
                cursor: pointer; 
                margin: 40px 20px; 
            }
            .btn:hover { background: #228B22; }
        </style>
    </head>
    <body>
        <h1>Mga karanasan ng iba</h1>
        <p style="font-size:35px;">Narito ang totoong kwento ng mga taong tulad natin. Hindi ka nag-iisa.</p>

        <div class="story">
            <h2>Tatay John Gereck: Isang Tatay na Nahulog sa Online Sabong</h2>
            <p>Isa akong ordinaryong Tatay. Nagsimula 'to noong pandemic — para lang magkaroon ng extra income, sabi ko. Nag-download ako ng sabong app, nanalo ng konti sa una. Masarap ang feeling. Pero unti-unti, naging "just one more bet" hanggang sa umabot sa utang sa GCash at pamilya.</p>
            
            <p>Nawala ang tiwala ng asawa ko, natakot ang mga anak ko. Nagising ako isang araw na wala na halos pera, pero patuloy pa rin ang paglalaro. Hanggang sa sinabi ko sa sarili ko: "Sapat na 'to. Para sa pamilya ko, titigil ako."</p>
            
            <p>Hindi madali. Una kong ginawa: tinanggal ko ang apps, binago ko ang passwords, sinabi ko sa misis ko ang totoo. Nahihiya ako, pero kailangan. Naghanap ako ng ibang paraan para punan ang oras — nag-gym ako, nagluto para sa pamilya, nag-volunteer sa barangay. May araw na malakas ang urge, pero tinatawagan ko ang kaibigan ko o nagdadasal lang.</p>
            
            <p>Hanggang ngayon, lowkey lang ako. Hindi ako nagpo-post na "clean na ako". Pero alam ko sa sarili ko: isa-isang araw lang. At bawat araw na hindi ako naglaro, mas malakas ako kaysa kahapon.</p>
            
            <p>Kung ikaw din ay nahuhulog ngayon — kaya mo 'yan. Hindi ka nag-iisa. Simulan mo lang ang unang hakbang.</p>
        </div>

        <div class="story">
            <h2>Story 2:  online gambling adik</h2>

            <p>Nagsimula ako sa online gambling noong 2019. Pero bago pa 'yon, simula nung nagkaroon ako ng work, gusto ko na talagang magka-account online para makataya sa NBA games. Pero mahirap pa noon maka-open ng account, kaya nalipat ang atensyon ko sa stock market. Doon ako nag-trade daily. Halata na sugal talaga ang hinahanap ko.</p>

            <p>Sa tingin ko, naka-root 'to sa pagkabata ko. Halos mga sugarol ang nakikita ko araw-araw sa community namin tuwing hapon — hindi sa family ko, pero sa paligid. Kaya hindi na bago sa'kin ang sugal. Nung teenager ako, nagsugal na rin ako, pero pinutol 'yon kasi ayaw na ayaw ng magulang ko. Nakita nila firsthand ang dulot nito: napabayaan ang pamilya, nawawalan ng pera, nagkakaproblema.</p>

            <p>Pero nung nag-pandemic, lumala ulit. Sa bahay lang lagi, kaya naging mas madali. Hanggang sa umabot na magka-utang na ako. At ang mas masama pa — **secreto ko 'to**. Hindi ko sinasabi sa asawa ko, sa parents ko, kahit kanino. Kaya lalong lumalim ang addiction ko. Hanggang ngayon, hindi ko pa rin sinasabi sa kanila na adik ako. Alam ko na may problema na, pero hindi ko matigil ang urge. Pag may pera ako, sigurado — sa online bingo plus 'to. Manalo man o matalo, hindi ako tumitigil hangga't hindi ubos lahat.</p>

            <p>May time na lahat ng sahod ko sinugal ko. Nanalo ako ng malaki, pero isang iglap lang — ubos ulit, pati sahod ko. Doon nagsimula ang pag-uutang. Minsan kahit alam ko na may mapagkakautangan ako, sinusugal ko pa rin. Pag naubos na, nanunungkulan ako sa online lending apps. Lahat ng pwede utangan, ginawa ko na. Ganun kalala.</p>

            <p>Ilang beses ko nang inamin sa sarili ko na mali 'to. Gumawa pa ako ng journal, gumawa pa ako ng self-help app katulad nito. Pero wala — nagsusugal pa rin ako hangga't may pera. Umabot na sa point na sinusuntok ko na ang ulo ko dahil sa katangahan: "Bakit ka nagsusugal? Hindi mo ba nakikita ang anak mo?" May time na hindi ko pinapansin ang anak ko dahil sa sugal — 5 years old lang siya noon. May time pa nga na pinapanood ko siya sa mga laro ko kasi feeling ko lucky charm ko siya.</p>

            <p>Alam ko sa sarili ko na kailangan ko ng tulong, pero hindi ko pa rin maamin sa asawa ko. Feeling ko kaya ko pa. Hanggang sa nag-rock bottom ako: zero, negative, wala nang mapakain sa pamilya. Utang na sa kapatid ko — paulit-ulit, walang bayad, pero those times, sinugal ko lang din. At ngayon, pagkain lang talaga ang pinag-uusapan. Yung misis ko, I think alam na niya — hindi siya tanga. Pero nag-aantay lang siguro siya ng tamang oras o sa akin na umamin. Pero hindi pa ako ready.</p>

            <p>Umabot na rin sa point na pangalan niya ginagamit ko sa online lending para makautang. Hanggang ngayon problema 'yon kasi mag-due na. God's willing, mabayaran ko rin 'yon.</p>

            <p>Ayun na nga — ito ang pinakamababa kong parte ng buhay ko. Kailangan ko i-speak out 'to kahit sa ganito lang. Thank you sa pagbabasa.</p>

            <p>Hindi ako nagsusugal for almost a month now. One day at a time. At isa na ako sa member ng GA PH. Join kayo rin dun kung nabasa niyo 'to.</p>

            <p>Salamat sa pagpapahintulot na ma-share ko 'to dito.</p>
        </div>

        <a href="/"><button class="btn">Bumalik sa Home</button></a>
        <a href="/paano-tumigil"><button class="btn">Paano Tumigil</button></a>
        
        <h2>Magkwento Ka Rin (Anonymous OK)</h2>
<p style="font-size:30px;">Kung gusto mong ibahagi ang kwento mo para makatulong sa iba, sulat mo lang sa baba. Hindi mo kailangang maglagay ng pangalan o personal info ang mahalaga ay ang storya.</p>

<form action="https://formspree.io/f/mvzqoklw" method="POST">
    <textarea name="kwento" rows="10" placeholder="Kwento mo dito... ( anonymous)" style="width:90%; max-width:700px; font-size:28px; padding:20px; border-radius:15px; border:2px solid #32CD32; margin:20px 0;"></textarea><br>
    
    <input type="text" name="pangalan" placeholder="Pangalan (opsyonal)" style="font-size:28px; padding:15px; width:80%; max-width:500px; border-radius:15px; border:2px solid #32CD32; margin:10px 0;"><br>
    
    <input type="email" name="_replyto" placeholder="Email mo (opsyonal)" style="font-size:28px; padding:15px; width:80%; max-width:500px; border-radius:15px; border:2px solid #32CD32; margin:10px 0;"><br>
    
    <button type="submit" class="btn">Ipadala ang Kwento</button>
</form>

<p style="font-size:28px; margin-top:40px;">Salamat sa pagbabahagi mo. Malaking tulong 'to sa iba.</p>
    </body>
    </html>
    """

@app.route('/self-check')
def self_check():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Self-Check: Gaano Kalala ang Problema Mo sa Sugal?</title>
        <style>
            body { background: linear-gradient(to bottom, #F0F8FF, #E0FFFF); text-align: center; font-family: Arial, sans-serif; margin:0; padding: 30px; color: #333; }
            h1 { color: #228B22; font-size: 50px; margin: 40px 0; }
            p { font-size: 32px; margin: 30px 0; }
            .question { font-size: 28px; text-align: left; max-width: 800px; margin: 25px auto; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
            label { display: block; margin: 10px 0; font-size: 28px; }
            #result { font-size: 38px; margin: 50px 0; padding: 30px; background: #FFFACD; border-radius: 20px; display: none; }
            .btn { font-size: 40px; padding: 30px 60px; background: #32CD32; color: white; border: none; border-radius: 40px; cursor: pointer; margin: 40px 20px; }
            .btn:hover { background: #228B22; }
        </style>
    </head>
    <body>
        <h1>Self-Check: Gaano Kalala ang Problema Mo sa Sugal?</h1>
        <p>Sagutan mo 'tong 20 tanong nang tapat (Oo o Hindi). Walang tamang/maling sagot — para makita mo lang kung may gambling issue ka.</p>
        <p>Score mo pagkatapos: Kung 7 o higit pa ang "Oo", baka kailangan mo ng tulong. Okay lang humingi ng tulong. Hindi ka nag-iisa.</p>

        <form id="quizForm">
            <div class="question">
                <p>1. Naglaro ka na ba ng sugal nang mas matagal kaysa sa balak mo?</p>
                <label><input type="radio" name="q1" value="yes"> Oo</label>
                <label><input type="radio" name="q1" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>2. Naglaro ka na ba ng sugal para makalimutan ang problema o mas maging masaya?</p>
                <label><input type="radio" name="q2" value="yes"> Oo</label>
                <label><input type="radio" name="q2" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>3. Naglaro ka na ba ng sugal para makabawi ng perang natalo mo sa dating laro?</p>
                <label><input type="radio" name="q3" value="yes"> Oo</label>
                <label><input type="radio" name="q3" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>4. Nag-isip ka na ba na maglaro ng mas malaki para mas maraming pera?</p>
                <label><input type="radio" name="q4" value="yes"> Oo</label>
                <label><input type="radio" name="q4" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>5. Naglaro ka na ba hanggang wala ka nang pera?</p>
                <label><input type="radio" name="q5" value="yes"> Oo</label>
                <label><input type="radio" name="q5" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>6. Nagkasakit ka na ba o nawalan ng tulog dahil sa paglalaro?</p>
                <label><input type="radio" name="q6" value="yes"> Oo</label>
                <label><input type="radio" name="q6" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>7. Nag-away kayo ng pamilya dahil sa sugal?</p>
                <label><input type="radio" name="q7" value="yes"> Oo</label>
                <label><input type="radio" name="q7" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>8. Nagpautang ka o nagutang para makapaglaro?</p>
                <label><input type="radio" name="q8" value="yes"> Oo</label>
                <label><input type="radio" name="q8" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>9. Nagbenta ka ng gamit para makapaglaro?</p>
                <label><input type="radio" name="q9" value="yes"> Oo</label>
                <label><input type="radio" name="q9" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>10. Nagkasala ka ba o nagsinungaling dahil sa sugal?</p>
                <label><input type="radio" name="q10" value="yes"> Oo</label>
                <label><input type="radio" name="q10" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>11. Naglaro ka ba para makaramdam ng "high" o excitement?</p>
                <label><input type="radio" name="q11" value="yes"> Oo</label>
                <label><input type="radio" name="q11" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>12. Naglaro ka ba kahit alam mong mali?</p>
                <label><input type="radio" name="q12" value="yes"> Oo</label>
                <label><input type="radio" name="q12" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>13. Naglaro ka ba kahit may problema ka sa pera?</p>
                <label><input type="radio" name="q13" value="yes"> Oo</label>
                <label><input type="radio" name="q13" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>14. Naglaro ka ba kahit alam mong may mas mahalaga kang dapat gawin?</p>
                <label><input type="radio" name="q14" value="yes"> Oo</label>
                <label><input type="radio" name="q14" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>15. Naglaro ka ba kahit may sakit ka o problema sa kalusugan?</p>
                <label><input type="radio" name="q15" value="yes"> Oo</label>
                <label><input type="radio" name="q15" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>16. Naglaro ka ba kahit alam mong maaaring mawala ang trabaho mo?</p>
                <label><input type="radio" name="q16" value="yes"> Oo</label>
                <label><input type="radio" name="q16" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>17. Naglaro ka ba kahit alam mong maaaring mawala ang pamilya mo?</p>
                <label><input type="radio" name="q17" value="yes"> Oo</label>
                <label><input type="radio" name="q17" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>18. Naglaro ka ba kahit alam mong maaaring makulong ka?</p>
                <label><input type="radio" name="q18" value="yes"> Oo</label>
                <label><input type="radio" name="q18" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>19. Nag-isip ka na ba ng self-harm dahil sa sugal?</p>
                <label><input type="radio" name="q19" value="yes"> Oo</label>
                <label><input type="radio" name="q19" value="no"> Hindi</label>
            </div>
            <div class="question">
                <p>20. Naglaro ka ba kahit alam mong may masamang epekto sa buhay mo?</p>
                <label><input type="radio" name="q20" value="yes"> Oo</label>
                <label><input type="radio" name="q20" value="no"> Hindi</label>
            </div>

            <button type="button" class="btn" onclick="calculateScore()">Tapos Na - Tingnan ang Resulta</button>
        </form>

        <div id="result"></div>

        <a href="/paano-tumigil"><button class="btn">Paano Tumigil</button></a>
        <a href="/"><button class="btn">Bumalik sa Home</button></a>

        <script>
            function calculateScore() {
                let score = 0;
                for (let i = 1; i <= 20; i++) {
                    let answer = document.querySelector(`input[name="q${i}"]:checked`);
                    if (answer && answer.value === "yes") {
                        score++;
                    }
                }
                let resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';

                let message = "";
                if (score === 0) {
                    message = "Mukhang kontrolado mo pa ang paglalaro mo. Good job! Mag-ingat pa rin.";
                } else if (score <= 6) {
                    message = "May kaunting senyales lang. Pero mag-ingat ka pa rin — wag hayaang lumala.";
                } else if (score <= 10) {
                    message = "May gambling problem ka na siguro. Huwag mag-alala, maraming nakakaahon dito.";
                } else {
                    message = "Malakas na senyales ng addiction. Pero kaya mo pa 'yan — may tulong na available. Tawagan mo ang hotline: 1553 (DOH) o 0917-558-4673 (HopeLine).";
                }

                resultDiv.innerHTML = `<strong>Score mo: ${score} / 20</strong><br><br>${message}<br><br>Kung 7 o higit pa ang Oo, baka kailangan mo ng tulong. Okay lang humingi ng tulong — tingnan ang <a href="/paano-tumigil">Paano Tumigil</a> page.`;
            }
        </script>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)