# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:33:37 2022

@author: anuja
"""

from django import forms



class drugForm(forms.Form):
    
    sex_list = (
    ('M','Male'),
    ('F', 'Female'),
    )
    
    bp_list = (
        ('HIGH','High'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low'),
    )
    ch_list = (
        ('HIGH','High'),
        ('NORMAL', 'Normal'),
    )

    age = forms.IntegerField(label='Age')
    sex = forms.CharField(label="Sex",widget=forms.Select(choices=sex_list))
    bp = forms.CharField(label="BP",widget=forms.Select(choices=bp_list))   
    ch = forms.CharField(label="Cholesterol",widget=forms.Select(choices=ch_list)) 
    na = forms.FloatField(label='Na_to_K:')
    
    
class medCostForm(forms.Form):
    
    smoker_list = (
    ('yes','Yes'),
    ('no', 'No'),
    )
    
    region_list = (
    ('northeast','North East'),
    ('northwest', 'North West'),
    ('southeast','South East'),
    ('southwest', 'South West'),
    )

    
    age = forms.IntegerField(label='Age')
    bmi = forms.FloatField(label="BMI")
    children = forms.IntegerField(label="Children")   
    smoker = forms.CharField(label="Smoker",widget=forms.Select(choices=smoker_list)) 
    region = forms.CharField(label='Region:',widget=forms.Select(choices=region_list))
 

class custClassForm(forms.Form):
        
    creditCard = forms.FloatField(label='Avg Credit Card Transaction Amt')
    balanceTrans = forms.FloatField(label="Avg. Balance Transfer Amt")
    lifeIns = forms.FloatField(label="Life Insurance Amt")   
    medIns = forms.FloatField(label="Medical Insurance Amt") 
    acBalance = forms.FloatField(label="Avg. A/C_Balance")
    perLoan = forms.FloatField(label='Personal Loan Amt')
    homeLoan = forms.FloatField(label="Home Loan Amt")
    onlineTrans = forms.FloatField(label="Online Purchase_Amt")   
    portBalance = forms.FloatField(label="Portfolio Balance")
    
class fpsForm(forms.Form):
    
    sex_list = (
    ('Male','Male'),
    ('Female', 'Female'),
    )
    
    travelType_list = (
    ('Personal','Personal'),
    ('Business', 'Business'),
    )
    
    
    Class_list = (
    ('Eco','Economic'),
    ('Business', 'Business'),
    ('EcoPlus','Economic Plus'),
    )

    rating_list = (
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    )


    sex = forms.CharField(label="Sex",widget=forms.Select(choices=sex_list))
    age = forms.IntegerField(label='Age')
    travelType =forms.CharField(label="Travel Type",widget=forms.Select(choices=travelType_list)) 
    flClass = forms.CharField(label="Class",widget=forms.Select(choices=Class_list))     
    flDis = forms.IntegerField(label="Flight Distance") 
    
    wifiRat = forms.CharField(label='Rating for Inflight wifi service:',widget=forms.Select(choices=rating_list))
    datRat = forms.CharField(label='Rating for Departure/Arrival time convenience:',widget=forms.Select(choices=rating_list))
    eosyBookRat = forms.CharField(label='Rating for Ease of Online booking:',widget=forms.Select(choices=rating_list))
    gateLocRat = forms.CharField(label='Rating for Gate location:',widget=forms.Select(choices=rating_list))
    foodRat = forms.CharField(label='Rating for Food and Drink:',widget=forms.Select(choices=rating_list))
    
    olBoardRat = forms.CharField(label='Rating for Online boarding:',widget=forms.Select(choices=rating_list))    
    seatComfRat = forms.CharField(label='Rating for Seat comfort:',widget=forms.Select(choices=rating_list))
    entertainRat = forms.CharField(label='Rating for Inflight Entertainment:',widget=forms.Select(choices=rating_list))
    onbrdSerRat = forms.CharField(label='Rating for On-board service:',widget=forms.Select(choices=rating_list))   
    legRmRat = forms.CharField(label='Rating for Leg room service:',widget=forms.Select(choices=rating_list))
    
    bagRat = forms.CharField(label='Rating for Baggage handling:',widget=forms.Select(choices=rating_list))
    chkinRat = forms.CharField(label='Rating for Checkin service:',widget=forms.Select(choices=rating_list))   
    inflserRat = forms.CharField(label='Rating for Inflight service:',widget=forms.Select(choices=rating_list))
    cleanRat = forms.CharField(label='Rating for Cleanliness:',widget=forms.Select(choices=rating_list))
    
    depDelay = forms.IntegerField(label='Departure Delay in min')
    arrDelay = forms.IntegerField(label='Arrival Delay in min')