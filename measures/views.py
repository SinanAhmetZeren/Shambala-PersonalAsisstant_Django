import os
from django.shortcuts import render,redirect
from .forms import measure_values_Form, measure_names_Form
from .models import measure_values, measure_names
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import seaborn as sns; sns.set_theme()


@login_required(login_url = "user:login")
def set_measure_names(request):
    form = measure_names_Form(request.POST or None)

    if request.user.is_authenticated and measure_names.objects.filter(author = request.user):
        measure_names1 = measure_names.objects.filter(author = request.user)[0]
    else:
        measure_names1 = None

    if form.is_valid():
        measure_names2 = form.save(commit=False)
        if request.user.is_authenticated:
            measure_names2.author = request.user
        else:
            messages.success(request,"Please login first")
            return render(request,"setmeasures.html",{"form":form})
        """setmeasures.author = request.user"""
        measure_names2.save()
        messages.success(request,"Measures saved successfully")
    return render(request,"setmeasures.html",{"form":form,"measure_names1": measure_names1})





def index(request): 
    # GET --> kullanıcının (measure_names)i ve boş form ile render edicez
    # POST --> forma girilen değerlerini (measure_values) post edicez 
    form = measure_values_Form(request.POST or None)
    
    # ------- GET ------ #
    if request.user.is_authenticated and measure_names.objects.filter(author = request.user):
        measure_names1 = measure_names.objects.filter(author = request.user)[0]
    else:
        measure_names1 = None
    # ------- POST ----- #
    if form.is_valid():
        measures = form.save(commit=False)
        #if request.user.is_authenticated:
        measures.author = request.user
        #else:
        #messages.success(request,"Please login first")
        #return render(request,"index.html",{"form":form})
        measures.save()
        messages.success(request,"Measures saved successfully")
    return render(request,"index.html",{"form":form, "measure_names1": measure_names1})

    #örnek kod:  articles = Article.objects.filter(author = request.user)

    #else:
    #    measure_names1 = measure_names(request.user, datetime.date.today() ,"measure1","measure2","measure3","measure4","measure5","measure6",)
  

@login_required(login_url = "user:login")
def analyze(request):
    if request.user.is_authenticated and measure_names.objects.filter(author = request.user):
        measure_names1 = measure_names.objects.filter(author = request.user)[0]
    else:
        measure_names1 = [" "," "," "," "," "," "]  #author, name1, name2, name3..., name6
    measure_values1 = measure_values.objects.filter(author = request.user)
    datelist, measure1list,measure2list,measure3list,measure4list,measure5list,measure6list = ([] for i in range(7))
    j = 1
    for values in measure_values1:
        measure1list.append(values.measure_1)
        measure2list.append(values.measure_2)
        measure3list.append(values.measure_3)
        measure4list.append(values.measure_4)
        measure5list.append(values.measure_5)
        measure6list.append(values.measure_6)
        #datelist.append(values.measure_date.strftime("%Y-%m-%d"))
        datelist.append(j)
        j += 1

    measure_values_dict = {
        "datelist": datelist, 
        "measure1list": measure1list,
        "measure2list": measure2list,
        "measure3list": measure3list,
        "measure4list": measure4list,
        "measure5list": measure5list,
        "measure6list": measure6list,
        }

    measure_values_list = [datelist, measure1list, measure2list, measure3list, measure4list,measure5list,measure6list] 

    correlations = []
    for i in range(1,7):
        for j in range(1,7):
            corr = np.corrcoef(measure_values_list[i],measure_values_list[j])[0,1]
            corr = round(corr,3)
            correlations.append(corr)
    corr_array = np.array([correlations[i:i+6] for i in range(0, len(correlations), 6)])
    #print(corr_array)
    #print("-----------")
    #print(np.corrcoef(measure_values_list[3],measure_values_list[2])[0,1])
    #print(measure_values_list[3],measure_values_list[2])
    # 3 -> sugar cons  ve  2 -> exercise
    #print("-----------")
    if measure_names1 != [" "," "," "," "," "," "]:
        axis_labels = (measure_names1.measure_1_name, measure_names1.measure_2_name, measure_names1.measure_3_name, measure_names1.measure_4_name, measure_names1.measure_5_name, measure_names1.measure_6_name, )
    else:
        axis_labels = ("","","","","","",)

    sns_plot = sns.heatmap(corr_array,annot=True,cmap="RdYlGn",xticklabels=axis_labels, yticklabels=axis_labels, linewidths=2, linecolor='gold')
    #sns_plot = sns.heatmap(corr_array,annot=True,xticklabels=axis_labels, yticklabels=axis_labels, linewidths=2, linecolor='gold')


    sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=45) 
    sns_plot.set_yticklabels(sns_plot.get_yticklabels(), rotation=0) 

    fig = sns_plot.get_figure()
    fig.tight_layout()

    if os.path.isfile('static/correlations/{}.png'.format(request.user.username)):
        os.remove('static/correlations/{}.png'.format(request.user.username))
    fig.savefig('static/correlations/{}.png'.format(request.user.username))
    plt.close()
    return render(request,"analyze.html",{"measure_names1":measure_names1,"measure_values_dict": measure_values_dict, "corr_array":corr_array})
