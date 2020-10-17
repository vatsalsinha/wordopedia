from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Word

# Create your views here.
def home(request):
    wrds = Word.objects.all()
    return render(request,'words/home.html', {'wrds': wrds})

def word(request, word_id):
    wrd_dtl = get_object_or_404(Word, pk = word_id)
    return render(request, 'words/word.html', {'wrd_dtl': wrd_dtl})