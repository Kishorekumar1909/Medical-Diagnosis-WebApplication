import pickle
from django.shortcuts import render
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from .models import patient


def predict(values, dic):
    global D_name
    if len(values) == 8:
        model = pickle.load(open('app1/models/diabetes.pkl','rb'))
        values = np.asarray(values)
        global D_name
        D_name = "Diabetes"
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('app1/models/breast_cancer.pkl','rb'))
        values = np.asarray(values)
        D_name = "Breast Cancer"
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('app1/models/heart.pkl','rb'))
        values = np.asarray(values)
        D_name = "Heart"
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('app1/models/kidney.pkl','rb'))
        values = np.asarray(values)
        D_name = "Kidney"
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('app1/models/liver.pkl','rb'))
        values = np.asarray(values)
        D_name = "Liver"
        return model.predict(values.reshape(1, -1))[0]


def index(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about-us.html')

def servicepage(request):
    return render(request, 'services.html')

def contactpage(request):
    return render(request, 'contact.html')

def iconpage(request):
    return render(request, 'index-icons.html')

def home(request):
    return render(request,'home.html')


def diabetesPage(request):
    return render(request, 'diabetes.html')


def cancerPage(request):
    return render(request,'breast_cancer.html')


def heartPage(request):
    return render(request,'heart.html')


def kidneyPage(request):
    return render(request,'kidney.html')


def liverPage(request):
    return render(request,'liver.html')


def malariaPage(request):
    return render(request,'malaria.html')


def pneumoniaPage(request):
    return render(request,'pneumonia.html')


def predictPage(request):
    try:
        if request.method == 'POST':
            #print("Post")
            to_predict_dict = request.POST.dict()
            name = to_predict_dict['PatientName']
            del to_predict_dict['csrfmiddlewaretoken']
            del to_predict_dict['PatientName']
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
            data = patient(Name = name, DiseaseName = D_name, Result = bool(pred))
            data.save()
    except Exception as error:
        context={
            "message":error
        }
        return render(request,"home.html", context)

    return render(request,'predict.html', {"pred":pred})


def malariapredictPage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                img = Image.open(request.FILES['image'])
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,3))
                img = img.astype(np.float64)
                model = load_model("app1/models/malaria.h5")
                pred = np.argmax(model.predict(img)[0])
                data = patient(Name = request.POST['PatientName'], DiseaseName = "Malaria", Result = bool(pred))
                data.save()
        except Exception as error:
            message = error
            return render(request,'malaria.html', {'message': message})
    return render(request,'malaria_predict.html', {'pred':pred})

def pneumoniapredictPage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                img = Image.open(request.FILES['image']).convert('L')
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,1))
                img = img / 255.0
                model = load_model("app1/models/pneumonia.h5")
                pred = np.argmax(model.predict(img)[0])
                data = patient(Name = request.POST['PatientName'], DiseaseName = "pneumonia", Result = bool(pred))
                data.save()
        except:
            message = "Please upload an Image"
            return render(request,'pneumonia.html', {'message': message})
    return render(request,'pneumonia_predict.html', {'pred':pred})
