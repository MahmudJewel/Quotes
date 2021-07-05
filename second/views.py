from django.shortcuts import render, redirect
from . import models
from .models import addQuotes
# Create your views here.

def htmlfile(request):
	documents=addQuotes.objects.all()
	context={
		'documents' :documents,
	}
	return render(request,'index.html', context)



def add_quotes(request):
	#Start saved on database
	quotes=request.POST.get('htmlQuotes')
	author=request.POST.get('htmlAuthor')
	if request.method == 'POST':
		#quotes=request.POST.get('htmlQuotes')
		#author=request.POST.get('htmlAuthor')
		dt=addQuotes(quotes=quotes, author=author)
		dt.save()
		print('Savedon db',quotes, author)
	#End saved on database
	
	return render(request, 'add-quotes.html')


def delete_quotes(request,docid):
	docid=int(docid)
	documents=addQuotes.objects.all()
	document=addQuotes.objects.get(id = docid)
	context={
		'documents' : documents,
		'document' : document,
	}

	return render(request, 'delete-quotes.html', context)