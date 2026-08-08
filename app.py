from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Özge'nin seçeceği telafi / ceza maddeleri
PENALTIES = [
    {"id": 1, "text": "Yan yana gelindiğinde en az 1 saat kesintisiz sarılma cezası."},
    {"id": 2, "text": "İlk buluşmada tüm tatlı ve yemek seçim hakkının Özge'ye devredilmesi."},
    {"id": 3, "text": "Samet'in 1 hafta boyunca her sabah ilk mesajı atma zorunluluğu."},
    {"id": 4, "text": "Özge'nin belirleyeceği bir aktiviteye sorgusuz sualsiz 'Evet' deme hakkı."},
    {"id": 5, "text": "Samet'in Özge'ye en sevdiği tatlıyı ısmarlaması."}
]

@app.route('/')
def index():
    return render_template('index.html', penalties=PENALTIES)

@app.route('/verdict', methods=['POST'])
def verdict():
    data = request.get_json()
    selected_ids = data.get('selected_penalties', [])
    
    chosen_penalties = [p['text'] for p in PENALTIES if p['id'] in selected_ids]
    
    return jsonify({
        "status": "success",
        "message": "Karar Onaylandı! Beraat Hükmü Verildi.",
        "chosen_penalties": chosen_penalties
    })

if __name__ == '__main__':
    app.run(debug=True)