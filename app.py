from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def AEKchat_response(kullanici, isim=None):
    kullanici = kullanici.lower()

    # İsim varsa kullanabiliriz
    if kullanici == "çık":
        return f"Görüşürüz {isim}, kendine iyi bak!" if isim else "Görüşürüz, kendine iyi bak!"
    
    if "mutlu" in kullanici or "iyi" in kullanici:
        return "Ne güzel, senin için sevindim!"
    elif "nasılsın" in kullanici:
        return "İyiyim, teşekkür ederim."
    elif "adın ne" in kullanici:
        return "Benim adım AEKchat. Seninle sohbet etmek çok keyifli!"
    elif "kaç yaşındasın" in kullanici:
        return "Ben bir yapay zekayım, yaşım yok ama hep buradayım :)"
    elif "üzgün" in kullanici or "kötü" in kullanici:
        return "Üzgün hissetmene üzüldüm, umarım daha iyi hissedersin."
    else:
        return "Bunu anlayamadım. Başka bir şey söylemek ister misin?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mesaj = data.get("message")
    isim = data.get("name")
    cevap = AEKchat_response(mesaj, isim)
    return jsonify({"reply": cevap})

if __name__ == "__main__":
    app.run(debug=True)
