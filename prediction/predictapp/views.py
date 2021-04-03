from django.shortcuts import render
import pickle
import joblib
import openpyxl
import datetime 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
count=1

# Create your views here.

def home(request):
    return render(request,'home.html')

def form(request):
    return render(request,'form.html')

def about(request):
    return render(request,'about.html')


def getPredictions(mypreg,mygluc,mybp,mybmi,myage):
    model = joblib.load(open(r'C:\Web Programming\diab.pkl', "rb"))
    # model = joblib.load(open(r"C:\Web Programming\dms.sav", "rb"))
    prediction = model.predict([[mypreg,mygluc,mybp,mybmi,myage]])

    
    if prediction == 0:
        return "Not Diabetic"
    elif prediction == 1:
        return "Diabetic"
    else:
        return "404 errrror"
        


def result(request):
    myname = str(request.POST.get('myname'))
    myemail = str(request.POST.get('myemail'))
    mypreg = int(request.POST.get('mypreg'))
    mygluc = int(request.POST.get('mygluc'))
    myage = int(request.POST.get('myage'))
    mybp = int(request.POST.get('mybp'))
    mybmi = float(request.POST.get('mybmi'))

    print(mypreg,mygluc,mybp,mybmi,myage)

    result = getPredictions(mypreg,mygluc,mybp,mybmi,myage)

    print(result)

    wb = openpyxl.load_workbook(r"C:\Web Programming\hack\prediction\static\Book1.xlsx")
    sh = wb['Sheet1']
    sh['B4'].value = myname
    sh['E4'].value = datetime.datetime.now().strftime("%d-%m-%Y")
    sh['B5'].value = myage
    sh['E5'].value = myemail
    sh['B8'].value = mygluc
    sh['B9'].value = mypreg
    sh['E8'].value = mybp
    sh['E9'].value = mybmi
    sh['B11'].value = result
    global count
    count += 1

    wb.save(r"C:\Web Programming\hack\prediction\static\Book"+str(count)+r".xlsx")

    return render(request, 'result.html', {'result':result,'myname':myname,'mypreg':mypreg,'mygluc':mygluc,'myage':myage,'mybp':mybp,'mybmi':mybmi,})



