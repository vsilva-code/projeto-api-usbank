from flask import Flask, request
import pandas as pd
from flask_basicauth import BasicAuth
import pickle
import os

X = [
     "Age",
     "Job",
     "Marital",
     "Education",
     "Default",
     "Balance",
     "HHInsurance",
     "CarLoan",
     "Communication",
     "LastContactDay",
     "NoOfContacts",
     "DaysPassed",
     "PrevAttempts",
     "CarInsurance",
     "ConnectionTime",
     "DayPeriod",
     "LastContactMonthNum"]

usbank_model = pickle.load(open("../../models/usbank_model.sav", "rb"))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'fernando' #os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = 'senha' #os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)


@app.route("/")
@basic_auth.required
def home():
    mensagem = "API rodando"
    return mensagem


#endpoint retorna predição 
@app.route("/predict/", methods=["GET", "POST"])
@basic_auth.required
def predict():
    dados = request.get_json()
    dados_input = [dados[col] for col in X]
    predict = usbank_model.predict([dados_input])
    predict = predict.tolist()
    mensagem = " "
    id = str(dados['Id'] )

    if predict[0] == 1:
        mensagem = "Pode ligar!"

    else:
        mensagem = "Liga não!"

    return mensagem, id


app.run(debug=True, host='0.0.0.0')
