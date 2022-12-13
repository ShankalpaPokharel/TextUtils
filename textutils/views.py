from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {"name":"Shankalpa","place":"Mars"}
    return render(request,'index.html', params)




def analyze(request):
    # get the text
    print("hello analyze")
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','default')
    capall = request.POST.get('capall','default')
    charCount = request.POST.get('charCount','default')
    print(removepunc)
    print(djtext) 
    print("hello")
    # analyzed = djtext

    

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
   
        # return HttpResponse("remove punc")
        return render(request, 'analyze.html', params)
    
    
    
    elif capall == "on":
        analyzed = djtext.upper()
        params = {'purpose':'Capitaize All', "analyzed_text":analyzed}
        
        
        return render(request,'analyze.html', params)

    elif charCount == "on":
        analyzed = len(djtext)
        params = {'purpose':'Character Counter', "analyzed_text":analyzed}
        
        
        return render(request,'analyze.html', params)

    
    
    
    
    else:
        return HttpResponse("Error")