import cv2
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model

from app.services.pre_processamento import detectar_rosto

modelo = load_model('app/model/modelo_cnn_lucas1000.h5')
# colocar aqui o path para o modelo treinado

def prever_pessoa(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = detectar_rosto(img)
      # Redimensiona para o tamanho de entrada da CNN

    img = cv2.resize(img, (640,480))

    # Previsão
    prediction = modelo.predict(np.expand_dims(img, axis=0))
    
    predicted_class = np.argmax(prediction)
    confidence = prediction[0, predicted_class]
    print(confidence)
    # a confiança é maior que o limiar?
    if confidence >= 0.8:
        pass
    else:
        predicted_class = -1
    
    if predicted_class == 0:
        return'Lucas Borges Nascimento'
    elif predicted_class == 1:
        return'Veronica Oliveira Brito'
    elif predicted_class == 2:
        return'João Fulgêncio'
    elif predicted_class == 3:
        return'Guilherme Araújo Alexandre'
    elif predicted_class == 4:
        return'Ruan Tineu Custódio'
    else:
        return'Desconhecido'
