import cv2
import numpy as np
from keras.models import load_model
from gtts import gTTS
import pygame
import io

pygame.init()

# Load the saved model
model = load_model(r'C:\Users\twalunjk\Downloads\DL\save\act_model.hdf5')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Resize the image to the size the model expects
    resized = cv2.resize(gray, (128, 32))
    # Normalize the image
    normalized = resized / 255
    # Add an extra dimension
    input_data = np.expand_dims(normalized, axis=0)

    # Use the model to predict
    prediction = model.predict(input_data.reshape(1, 32, 128, 1))

    # Use CTC decoder to get the text
    out = K.get_value(K.ctc_decode(prediction, input_length=np.ones(prediction.shape[0])*prediction.shape[1],
                         greedy=True)[0][0])

    # Convert the text to speech
    for x in out:
        text = ''.join([char_list[int(p)] for p in x if int(p) != -1])
        if text:
            tts = gTTS(text=text, lang='en')
            audio_data = io.BytesIO()
            tts.write_to_fp(audio_data)
            audio_data.seek(0)
            pygame.mixer.music.load(audio_data)
            pygame.mixer.music.play()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
