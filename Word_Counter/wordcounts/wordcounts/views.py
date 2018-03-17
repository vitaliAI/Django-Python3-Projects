from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hithere':'thas me'})

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    wordlist_dic = dict()
    for word in word_list:
        if word in wordlist_dic:
            wordlist_dic[word] += 1
        else:
            wordlist_dic[word] = 1
    sorted_list = sorted(wordlist_dic.items(), key= operator.itemgetter(1), reverse=True)


    return render(request, 'count.html',{'fulltext':fulltext, 'number':len(word_list), 'dictonary': sorted_list})

def about(request):
    return render(request, 'about.html', {})