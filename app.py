from flask import Flask, request, jsonify
import datetime
import random

app = Flask(__name__)

# Basit kullanıcı ismi değişkeni
isim = "Misafir"

# Ortalama hesaplama durumu
ortalama_modu = False
sayilar = []
sayac = 0
toplam_sayi = 0

@app.route("/chat", methods=["POST"])
def chat():
    global ortalama_modu, sayilar, sayac, toplam_sayi, isim

    data = request.get_json()
    mesaj = data.get("message", "").lower()
    isim = data.get("name", "Misafir")

    kelimeler = mesaj.split()

    if ortalama_modu:
        if toplam_sayi == 0:
            try:
                toplam_sayi = int(mesaj)
                if toplam_sayi <= 0:
                    toplam_sayi = 0
                    return jsonify({"reply": "Lütfen geçerli bir sayı gir."})
                sayac = 0
                sayilar = []
                return jsonify({"reply": f"{sayac + 1}. sayıyı gir:"})
            except:
                return jsonify({"reply": "Lütfen geçerli bir sayı gir."})
        else:
            try:
                sayi = float(mesaj)
                sayilar.append(sayi)
                sayac += 1
                if sayac < toplam_sayi:
                    return jsonify({"reply": f"{sayac + 1}. sayıyı gir:"})
                else:
                    ort = sum(sayilar) / len(sayilar)
                    ortalama_modu = False
                    sayilar = []
                    sayac = 0
                    toplam_sayi = 0
                    return jsonify({"reply": f"Girdiğin sayıların ortalaması: {ort:.2f}"})
            except:
                return jsonify({"reply": "Lütfen geçerli bir sayı gir."})

    if "ortalama" in mesaj:
        ortalama_modu = True
        return jsonify({"reply": "Kaç sayı gireceksin?"})

    def kelime_var(*anahtarlar):
        return any(kelime in kelimeler for kelime in anahtarlar)

    def cumlede_var(*anahtarlar):
        return any(anahtar in mesaj for anahtar in anahtarlar)

    mutlu_kelimeler = ["mutlu", "iyi", "harika", "sevinçli"]
    uzgun_kelimeler = ["üzgün", "kötü", "mutsuz"]

    if kelime_var("merhaba", "selam", "hello"):
        return jsonify({"reply": f"Merhaba {isim}! 😊 Sana nasıl yardımcı olabilirim?"})
    elif kelime_var("çık"):
        return jsonify({"reply": f"Görüşürüz {isim}! Kendine iyi bak! 👋"})
    elif any(k in kelimeler for k in mutlu_kelimeler):
        cevaplar = ["Harika! 😄", "Bunu duyduğuma sevindim! 🌟", "Ne güzel! 😃"]
        return jsonify({"reply": random.choice(cevaplar)})
    elif any(k in kelimeler for k in uzgun_kelimeler):
        cevaplar = ["Üzgün hissetmene üzüldüm 😢", "Umarım daha iyi hissedersin 🌈", "Böyle zamanlar geçer, sabırlı ol 🙏"]
        return jsonify({"reply": random.choice(cevaplar)})
    elif cumlede_var("nasılsın"):
        return jsonify({"reply": "Ben iyiyim, teşekkür ederim! 🤖 Sen nasılsın?"})
    elif cumlede_var("adın ne"):
        return jsonify({"reply": f"Benim adım AEKchat. Seninle sohbet etmek çok keyifli, {isim}! 🗨️"})
    elif cumlede_var("kaç yaşındasın"):
        return jsonify({"reply": "Ben bir yapay zekayım, yaşım yok ama hep buradayım :)"})
    elif cumlede_var("saat kaç"):
        simdi = datetime.datetime.now().strftime("%H:%M")
        return jsonify({"reply": f"Şu an saat {simdi} ⏰"})
    elif cumlede_var("tarih", "günlerden ne"):
        bugun = datetime.datetime.now().strftime("%d/%m/%Y - %A")
        return jsonify({"reply": f"Bugünün tarihi {bugun} 📅"})
    elif kelime_var("motivasyon", "moralim bozuk"):
        return jsonify({"reply": "Unutma, her karanlığın sonunda aydınlık doğar. Güçlüsün, başaracaksın! 💪✨"})
    elif kelime_var("öneri", "ne yapayım"):
        return jsonify({"reply": "Kısa bir yürüyüş yapmayı dene. Temiz hava sana iyi gelebilir 🌳"})
    elif kelime_var("yapay zeka"):
        return jsonify({"reply": "Ben bir yapay zekayım! Öğrenmem, gelişmem ve seninle konuşmam için tasarlandım 🤖"})
    elif cumlede_var("uzaylı"):
        return jsonify({"reply": "Blorp! Ben AEK-9000. Barış için geldim 🛸"})
    elif kelime_var("tebrik et", "başardım"):
        return jsonify({"reply": "🎉 Bravo! Seninle gurur duyuyorum! 👏"})
    elif cumlede_var("kaç yaşındayım"):
        return jsonify({"reply": f"Hmm... Tahminimce {random.randint(18, 40)} yaşındasın 😄 Doğru mu?"})
    elif cumlede_var("aekchat"):
        return jsonify({"reply": f"Efendim {isim}! 😊 Sana nasıl yardımcı olabilirim?"})
    elif cumlede_var("optimus"):
        return jsonify({"reply": "Ben Optimus Prime. Tüm Otobotlara sesleniyorum."})
    elif cumlede_var("seni kim tasarladı"):
        return jsonify({"reply": "Beni tasarlayan kişi Ahmet Emir Koç."})
    elif cumlede_var("ne tür bir yapay zekasın", "ne tür"):
        return jsonify({"reply": "Ben bir sohbet yapay zekasıyım 🤖"})
    elif cumlede_var("zararlı"):
        return jsonify({"reply": "Hayır, ben yararlı bir yazılım türüyüm. Sana yardımcı olmak için buradayım."})
    elif cumlede_var("yararlı"):
        return jsonify({"reply": "Evet, ben yararlı bir yazılım türüyüm. Sohbet ve bilgi için buradayım."})
    elif cumlede_var("gelişim", "geliş"):
        return jsonify({"reply": "Evet, gelişmeye devam ediyorum. Çok daha iyi bir yapay zeka olabilmek için."})
    elif cumlede_var("yazılım dilin ne", "dilin ne"):
        return jsonify({"reply": "Ben bir Python ile yazılmış kişisel yapay zekayım."})
    elif cumlede_var("pyinstaller"):
        return jsonify({"reply": "PyInstaller, Python'da yazılmış bir programı .exe Windows çalıştırılabilir dosyası haline getirmeni sağlar."})
    elif cumlede_var("pyinstaller nasıl indirilir", "pyinstaller indir"):
        return jsonify({"reply": "-pip install pyinstaller- terminal üzerinden komutu çalıştırarak PyInstaller'ı yükleyebilirsin."})
    elif cumlede_var("exe"):
        return jsonify({"reply": "-pyinstaller --onefile scriptin_adi.py- terminal üzerinden bu komutla .py dosyanı .exe formatına dönüştürebilirsin."})
    else:
        return jsonify({"reply": "Bunu anlayamadım 🤔 Başka bir şey söylemek ister misin?"})


if __name__ == "__main__":
    app.run(debug=True)


