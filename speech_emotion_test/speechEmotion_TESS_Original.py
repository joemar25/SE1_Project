# John Olan S. Gomez
# 12/03/2022
# Speech Emotion Recognition - TESS dataset

import librosa
import soundfile
import os, glob, pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score


#Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

#Load the data and extract features for each sound file
def load_data(test_size):
    counter= 0
    paths=[]
    x,y=[],[] #x= feature, y= emotion
    for dirname, _, filenames in os.walk(r"C:\Users\Olan\Documents\Olan\3rd_year\CS_117-Software_Engineering_1\Prototype\speechEmotion\TESS_data"):
        for filename in filenames:
            paths.append(os.path.join(dirname, filename))
            emotion = filename.split('_')[-1]
            emotion = emotion.split('.')[0]
            feature = extract_feature(paths[counter].replace("\\\\", "\\"), mfcc=True, chroma=True, mel=True)
            x.append(feature)
            y.append(str(emotion.lower()))
            counter += 1
        if len(paths) == 2800:
            break
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)

#Split the dataset
x_train,x_test,y_train,y_test=load_data(test_size=0.25)

#Get the shape of the training and testing datasets
print((x_train.shape[0], x_test.shape[0]))

#Get the number of features extracted
print(f'Features extracted: {x_train.shape[1]}')

#Initialize the Multi Layer Perceptron Classifier
model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)

#Train the model
model.fit(x_train,y_train)

#Predict for the test set
y_pred=model.predict(x_test)

#Calculate the accuracy of our model
accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)

#Print the accuracy
print("Accuracy: {:.2f}%".format(accuracy*100))

f1_score(y_test, y_pred,average=None)

df=pd.DataFrame({'Actual': y_test, 'Predicted':y_pred})
print(df.head(20))

# Writing different model files to file
with open('modelForPrediction1.sav', 'wb') as f:
    pickle.dump(model,f)

filename = 'modelForPrediction1.sav'
loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage

feature=extract_feature(r"C:\Users\Olan\Documents\Olan\3rd_year\CS_117-Software_Engineering_1\Prototype\speechEmotion\TESS_data\OAF_disgust\OAF_beg_disgust.wav", mfcc=True, chroma=True, mel=True)

feature=feature.reshape(1,-1)

prediction=loaded_model.predict(feature)
print(prediction)


