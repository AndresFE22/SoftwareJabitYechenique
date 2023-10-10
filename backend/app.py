from flask import Flask, render_template, request, jsonify, session
import pandas as pd
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import mysql.connector
import json


app = Flask(__name__)
CORS(app)

cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='prediccionrendimiento'
    )


@app.route('/')
def init():
    return 'escuchando'

@app.route('/prediction', methods=['GET', 'POST'])
def predecir_rtpc():
        
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='prediccionrendimiento'
    )
        input_data = request.json['field']
        name = str(input_data.pop(0))
        print(name)
        print(input_data)

        # Paso 2: Importar el conjunto de datos
        df = pd.read_csv('dataset.csv', delimiter=';', encoding='iso-8859-1')

        # Paso 3: Preprocesar los datos (si es necesario)
        X = df.iloc[:, 0:16].values
        y = df['RTPC']  # Esta es la columna que queremos predecir

        print(X, y)
        # Paso 4: Dividir el conjunto de datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Paso 5: Crear y entrenar el modelo de árbol de decisión
        tree_model = DecisionTreeClassifier(
            criterion='gini',
            max_depth=None,
            min_samples_split=500,
            min_samples_leaf=500,
            random_state=42
        )
    
        tree_model.fit(X_train, y_train)
    
        y_pred = tree_model.predict(X_test)
        precision = accuracy_score(y_test, y_pred)
        print(f'Precisión en el conjunto: {precision*100:.2f}%')


        prediction = tree_model.predict(np.array(input_data).reshape(1, -1))
        print(prediction)
    
        mensajeprediccion = ''
    
        respuestaredneuronalo = prediction[0]
        if (respuestaredneuronalo == 0):
            mensajeprediccion = "El rendimiento es ALTO"
        elif (respuestaredneuronalo == 1): 
            mensajeprediccion = "El rendimiento es MEDIO"
        elif (respuestaredneuronalo == 2): 
            mensajeprediccion = "El rendimiento es BAJO"
        
        print(mensajeprediccion)
    
        jsonFeatures = json.dumps(input_data)
        # Conectar a la base de datos

        cursor = conn.cursor()
        sql = "INSERT INTO reporteestudiantes (name, features, prediction) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, jsonFeatures, int(prediction[0])))
        new_id = cursor.lastrowid  # Obtiene el ID del nuevo registro
        cursor.close()
        conn.close()

        return jsonify({'id': new_id, 'message': mensajeprediccion})



@app.route('/prediction/<int:id>', methods=['GET', 'POST'])
def resultPrediction(id):
    
    id_student = id
    cursor = conn.cursor()
    sql = "SELECT prediction FROM reporteestudiantes WHERE id = %s"
    cursor.execute(sql, (id_student,))
    cursor.close()
    prediction = cursor.fetchone()

    
    print(id_student)
    print(prediction)

   
    
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True)



