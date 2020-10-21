from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Word
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import WordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
def home(request):
    wrds = Word.objects.all()
    wrd = Word.objects.first
    return render(request,'words/home.html', {'wrds': wrds, 'wrd':wrd})

def word(request, word_id):
    wrd_dtl = get_object_or_404(Word, pk = word_id)
    return render(request, 'words/word.html', {'wrd_dtl': wrd_dtl})

@api_view(['GET'])
def words_list_view(request, *args, **kwargs):
    qs = Word.objects.all().order_by('id')
    serializer = WordSerializer(qs, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
#@permission_classes([IsAuthenticated])
def words_detail_view(request, word_id, *args, **kwargs):
    qs = Word.objects.filter(id = word_id)
    if not qs.exists():
        return Response({})
    obj = qs.first()
    serializer = WordSerializer(obj)
    return Response(serializer.data)

