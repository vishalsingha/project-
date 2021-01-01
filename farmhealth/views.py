from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import preprocess_input
import os
from .models import doctor, tomato_plant
from tensorflow.keras.models import Model
from tensorflow.keras.layers import  Dropout, BatchNormalization, Dense, GlobalAveragePooling2D
#####################################################################
#base model
base_model=tf.keras.applications.MobileNet(weights='imagenet',input_shape=(128, 128, 3), include_top=False) 
x=base_model.output
x=GlobalAveragePooling2D()(x)

def  create_tomato_model(x):
    x=Dense(1024, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(1024, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.2)(x)
    x=Dense(512, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.2)(x)
    preds=Dense(10,activation='softmax')(x)
    model=Model(inputs=base_model.input,outputs=preds)
    return model

def  create_apple_model(x):
    x=Dense(512, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(128, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(64, activation = 'relu')(x)
    preds=Dense(4,activation='softmax')(x)
    model=Model(inputs=base_model.input,outputs=preds)
    return model
def create_corn_model(x):
    x=Dense(512, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(128, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(64, activation = 'relu')(x)
    preds=Dense(4,activation='softmax')(x)
    model=Model(inputs=base_model.input,outputs=preds)
    return model

def create_grapes_model(x):
    x=Dense(1024, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(1024, activation = 'relu')(x)
    x = BatchNormalization()(x)
    x=Dense(512, activation = 'relu')(x)
    preds=Dense(4,activation='softmax')(x)
    model=Model(inputs=base_model.input,outputs=preds)
    return model
    
######################################################################


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def doctor(request):
    return render(request, 'doctor.html')

def file_upload(request):
    if (request.method == 'POST')  and (request.POST["plant"]!="0"):
        if (request.FILES):
            plant = request.POST["plant"]
            if(plant=='Tomato'):
                model= create_tomato_model(x)
                file_path = os.path.join(settings.BASE_DIR, 'models/model_tomato.h5')
            elif(plant=="Apple"):
                model= create_apple_model(x)
                file_path = os.path.join(settings.BASE_DIR, 'models/model_apple.h5')
            elif(plant=="Corn"):
                model= create_corn_model(x)
                file_path = os.path.join(settings.BASE_DIR, 'models/model_corn.h5')
            elif(plant=="Grapes"):
                model= create_grapes_model(x)
                file_path = os.path.join(settings.BASE_DIR, 'models/model_grapes.h5')
            model.load_weights(file_path)
            model.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'], optimizer = 'adamax')
            img = cv2.imdecode(np.fromstring(request.FILES['myfile'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img,(128, 128))
            img = preprocess_input(np.expand_dims(img, 0))
            pred = np.argmax(model.predict(img))
            info = tomato_plant.objects.get(id = pred+1)
            return render(request, 'doctor.html', {'info': info})
    else:
        return render(request, 'doctor.html',{'massage' : "Plant category not selected"}) 
    return render(request, 'doctor.html',)








