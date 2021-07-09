from flask import Flask,render_template,url_for,request, jsonify
import re
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_md
import json 

# @TASK : Load model bahasa 
nlp = en_core_web_md.load()
# END OF TASK 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
            choice = request.form['taskoption']
            rawtext = request.form['rawtext']
            doc = nlp(rawtext)
            # menyimpan hasil nlp ke df 
            d = [(ent.label_, ent.text) for ent in doc.ents]
            df = pd.DataFrame(d, columns=['category', 'value'])

            if choice == 'organization':
                results = df[df['category'] == 'ORG']
                num_of_results = len(results)
            elif choice == 'person':
                results = df[df['category'] == 'PERSON']
                num_of_results = len(results)
            elif choice == 'geopolitical':
                results = df[df['category'] == 'GPE']
                num_of_results = len(results)
            elif choice == 'money':
                results = df[df['category'] == 'MONEY']
                num_of_results = len(results)
            elif choice == 'Select Category':
                results = pd.DataFrame()
                num_of_results = len(results)
                return render_template("index.html",results=results.iloc,num_of_results = num_of_results, original_text = rawtext)
    else:
        results = pd.DataFrame()
        num_of_results = len(results)

    return render_template("index.html",results=results.iloc[:,1],num_of_results = num_of_results, original_text = rawtext)


@app.route('/endpoint_tertentu')
def nama_fungsi_tertentu():
    # secara teknis, kita dapat melakukan apapun dalam fungsi ini 
    return ("Fungsi ini akan dijalankan saat endpoint tersebut diakses")

@app.route('/endpoint_get', methods=['GET'])
def contoh_get():
    return ("Contoh endpoint get")

@app.route('/endpoint_post', methods=['POST'])
def contoh_post():
    return ("Contoh endpoint post")

@app.route('/endpoint_multi', methods=['GET', 'POST'])
def multi_method():
    if request.method == 'POST':
        return ("Nilai ini akan dikembalikan jika endpoint ini diakses dengan method POST")
    else : 
        return ("Nilai ini akan dikembalikan jika endpoint ini diakses dengan method GET")


@app.route('/tes_send_json', methods=['POST'])
def tes_send_json():
    data = request.get_json() # proses membaca json yang dikirim 
    nama = data['nama']
    usia = data['usia']
    pekerjaan = data['pekerjaan']
    return ("Halo, {nama}. Usiamu adalah {usia} dan pekerjaanmu adalah {pekerjaan}".format(nama=nama, usia=usia, pekerjaan=pekerjaan))

@app.route('/tes_return_json', methods=['POST'])
def tes_return_json():
    data = request.get_json() # proses membaca json yang dikirim 
    df = pd.DataFrame([data]) # mengolah data menjadi dataframe

    return (df.to_json()) # mengembalikan dataframe dalam bentuk json

@app.route('/get_entities', methods=['POST'])
def get_entities():
    
    # ambil data dari json yang diterima endpoint
    data = request.get_json()
    
    # ambil nilai teks dari data
    text = data['text']
    
    # modelkan teks dengan model scipy 
    doc = nlp(text)
    
    # membuat pasangan label dan nilai entitas
    d = [(ent.label_, ent.text) for ent in doc.ents]

    # transform pasangan label menjadi dataframe 
    df = pd.DataFrame(d, columns=['category', 'value'])
    
    return (df.to_json())

    

if __name__ == '__main__':
    app.run(debug=True)