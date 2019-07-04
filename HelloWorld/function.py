#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'helloworld.html')

def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    word_dict ={}
    for eachWord in user_text:
        if eachWord not in word_dict:
            word_dict[eachWord] = 1
        else:
            word_dict[eachWord] += 1

    sorted_count = sorted(word_dict.items(),key = lambda w: w[1],reverse = True)

    return render(request, 'count.html', {'count': total_count,'text':user_text,'sorted':sorted_count})

def about(request):
    return render(request,'about.html')