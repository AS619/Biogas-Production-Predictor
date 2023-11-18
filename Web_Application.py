from flask import Flask, render_template,request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0
    if request.method == 'POST':
        Province = request.form['Province']
        Area_Rural = request.form.getlist('Area_Rural')
        Area_Urban = request.form.getlist('Area_Urban')
        Temperature = request.form['Temperature(0C)']
        Precipitation_Low= request.form.getlist('Precipitation_Low')
        Precipitation_Medium= request.form.getlist('Precipitation_Medium')
        Precipitation_High= request.form.getlist('Precipitation_High')
        Nb_of_Persons = request.form['Nb of Persons']
        Nb_of_Toilets = request.form['Nb of Toilets']
        Body_weight_ratio = request.form['Body weight ratio']
        Number_of_people_away_home = request.form['Number of people away from home']
        Are_there_Toddlers_No = request.form.getlist('Are there Toddlers_No')
        Are_there_Toddlers_Yes = request.form.getlist('Are there Toddlers_Yes')
        
        #print(Province,Area_Rural,Area_Urban,Temperature,Precipitation_Low,Precipitation_Medium,Precipitation_High,Nb_of_Persons,Nb_of_Toilets,Body_weight_ratio,Number_of_people_away_home,Are_there_Toddlers_No,Are_there_Toddlers_Yes)
      
        feature_list = []

        feature_list.append(int(Temperature))
        feature_list.append(int(Nb_of_Persons))
        feature_list.append(float(Body_weight_ratio))
        feature_list.append(int(Nb_of_Toilets))
        feature_list.append(int(Number_of_people_away_home))

        Province_list = ['Central','Eastern','North Central','North Western','Northern','Sabaragamuwa','Southern','Uwa','Western']

        for item in Province_list:
            if item == Province:
                feature_list.append(1)
            else:
                feature_list.append(0)
        
        feature_list.append(len(Area_Rural))
        feature_list.append(len(Area_Urban))

        feature_list.append(len(Precipitation_Low))
        feature_list.append(len(Precipitation_Medium))
        feature_list.append(len(Precipitation_High))

        feature_list.append(len(Are_there_Toddlers_No))
        feature_list.append(len(Are_there_Toddlers_Yes))

        pred= prediction(feature_list)
        pred= np.round(pred[0],4)
        #print(pred)
        pass
    

    return render_template("index.html",pred = pred)

if __name__ == '__main__':
    app.run(debug = True)



    #pip install scikit-learn==1.2.2
