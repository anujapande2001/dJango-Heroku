from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd
import pickle
import sklearn
from .forms import drugForm,medCostForm,custClassForm,fpsForm


def drugPred(request):

    if request.method == 'POST':
        print("Inside drugpred")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        bp = request.POST.get("bp")
        ch = request.POST.get("ch")
        na = request.POST.get("na")
    
        sample_df=pd.DataFrame({'Age':age,'Sex':sex,'BP':bp,'Cholesterol':ch,'Na_to_K':na},index=[0])
        model = pickle.load(open(r'DrugPrediction/drug_estimator.pkl', "rb"))
        drug_pred=model.predict(sample_df)
        context ={}
        context["form"]=drugForm()
        print("After Predict")
        print(drug_pred)
        if drug_pred[0]==0:
            context['drug_pred']="Proposed Drug is Drug X"
        elif drug_pred[0]==1:
            context['drug_pred']="Proposed Drug is Drug Y"
        elif drug_pred[0]==2:
            context['drug_pred']="Proposed Drug is Drug C"
        elif drug_pred[0]==3:
            context['drug_pred']="Proposed Drug is Drug A"
        elif drug_pred[0]==4:
            context['drug_pred']="Proposed Drug is Drug B"
        return render(request,"drugpred.html",context)
    else:
        context ={}
        context["form"]=drugForm()
        return render(request,'drugpred.html',context)
 
    
 
def medcostPred(request):
    # context ={}

    if request.method == 'POST':
        print("Inside medcostPost")
        age = request.POST.get("age")
        bmi = request.POST.get("bmi")
        children = request.POST.get("children")
        smoker = request.POST.get("smoker")
        region = request.POST.get("region")
    
        sample_df=pd.DataFrame({'age':age,'bmi':bmi,'children':children,'smoker':smoker,'region':region},index=[0])
        model = pickle.load(open(r'DrugPrediction\medcost_estimator.pkl', "rb"))
        print(sample_df)
        print(type(sample_df))
        medcost_pred=model.predict(sample_df)
        print("After Predict")
        print(medcost_pred)
        context ={}
        context["form"]=medCostForm()
        context['medcost_pred']="Proposed Cost is Rs. " + str(round(medcost_pred[0],2))

        return render(request,"medcost.html",context)
    else:
        print("Inside medcostGet")
        context ={}
        context["form"]=medCostForm()
        return render(request,'medcost.html',context)
        
    
def custclassPred(request):

    if request.method == 'POST':
        print("Inside custclassPred")
        
        creditCard = request.POST.get("creditCard")
        balanceTrans = request.POST.get("balanceTrans")
        lifeIns = request.POST.get("lifeIns")
        medIns = request.POST.get("medIns")
        acBalance = request.POST.get("acBalance")
        
        perLoan = request.POST.get("perLoan")
        homeLoan = request.POST.get("homeLoan")
        onlineTrans = request.POST.get("onlineTrans")
        portBalance = request.POST.get("portBalance")

        sample_df=pd.DataFrame({'Average_Credit_Card_Transaction':creditCard,'Balance_Transfer':balanceTrans,
                                'Life_Insurance':lifeIns,'Medical_Insurance':medIns,
                                'Average_A/C_Balance':acBalance,'Personal_Loan':perLoan,'Home_Loan':homeLoan,
                                'Online_Purchase_Amount':onlineTrans,'Portfolio_Balance':portBalance},index=[0])
        print(sample_df)
        print(type(sample_df))
        model = pickle.load(open('DrugPrediction\custclass_estimator.pkl', "rb"))
        
        cust_pred=model.predict(sample_df)
        context ={}
        context["form"]=custClassForm()        
        print("After Predict")
        print(cust_pred)
        if cust_pred[0]==1:
            context['cust_pred']="This Customer is of High Net Worth "
        elif cust_pred[0]==2:
            context['cust_pred']="This Customer is of Low Net Worth"
        
        return render(request,"custclass.html",context)
    else:
        context ={}
        context["form"]=custClassForm()
        return render(request,'custclass.html',context)
    

def fpsPred(request):

    print(request.method)

    if request.method == 'POST':
        print("Inside fpsPred Post")
        print(sklearn.__version__) 
        sex = request.POST.get("sex")
        # custType=request.POST.get("custType")
        age = request.POST.get("age")

        travelType = request.POST.get("travelType")
        flClass = request.POST.get("flClass")
        flDis = request.POST.get("flDis")
        
        wifiRat = request.POST.get("wifiRat")
        datRat = request.POST.get("eosyBookRat")
        eosyBookRat=request.POST.get("eosyBookRat")
        gateLocRat = request.POST.get("gateLocRat")
        foodRat = request.POST.get("foodRat")
        olBoardRat = request.POST.get("olBoardRat")
        

        seatComfRat = request.POST.get("seatComfRat")
        entertainRat=request.POST.get("entertainRat")
        onbrdSerRat = request.POST.get("onbrdSerRat")
        legRmRat = request.POST.get("legRmRat")
        bagRat = request.POST.get("bagRat")
    
    

        chkinRat = request.POST.get("chkinRat")
        inflserRat=request.POST.get("inflserRat")
        cleanRat = request.POST.get("cleanRat")
        depDelay = request.POST.get("depDelay")
        arrDelay = request.POST.get("arrDelay")
    
    
    																	

        sample_df=pd.DataFrame({'Gender':sex,'Age':age,'Type of Travel':travelType,
                                'Class':flClass,'Flight Distance':flDis,'Inflight wifi service':wifiRat,
                                'Departure/Arrival time convenient':datRat,'Ease of Online booking':eosyBookRat,
                                'Gate location':gateLocRat,'Food and drink':foodRat,'Online boarding':olBoardRat,
                                'Seat comfort':seatComfRat,'Inflight entertainment':entertainRat,
                                'On-board service':onbrdSerRat,'Leg room service':legRmRat,
                                'Baggage handling':bagRat,'Checkin service':chkinRat,'Inflight service':inflserRat,
                                'Cleanliness':cleanRat,'Departure Delay in Minutes':depDelay,
                                'Arrival Delay in Minutes':arrDelay},index=[0])
        
        import os
        directory_path = os.getcwd()
        print("My current directory is : " + directory_path)
        model = pickle.load(open(r'DrugPrediction\fps_estimator.pkl', "rb"))
        # model = pickle.load(open('fps_ml_model.pkl', "rb"))
        print(sample_df)
        print(type(sample_df))
        fps_pred=model.predict(sample_df)
        context ={}
        context["form"]=fpsForm()
        print("After Predict")
        print(fps_pred)
        if fps_pred[0]==0:
            context['fps_pred']="Passenger is Neutral or Dissatisfied"
        elif fps_pred[0]==1:
            context['fps_pred']="Passenger is Satisfied"
  
        return render(request,"fps.html",context)
    else:     
        print("Inside get")
        context ={}
        context["form"]=fpsForm()
        return render(request,'fps.html',context)
