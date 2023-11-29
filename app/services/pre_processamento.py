import cv2

def detectar_rosto(img):
    # Carregar o classificador Haarcascades para detecção de faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar faces na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Se houver faces detectadas, retorna a região da primeira face
    if len(faces) > 0:
        x, y, w, h = faces[0]
        return img[y:y+h, x:x+w]
    else:
        return None 