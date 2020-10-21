from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics



# Create your views here.
def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username exists'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'], first_name = request.POST['name'], email = request.POST['emailid'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'accounts/signup.html', {'error' : 'password must match'})
	else:
		return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'invalid credentials'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')

@api_view(['GET'])
#@authentication_classes([SessionAuthentication, BasicAuthentication])
#@permission_classes([IsAuthenticated])
def userprofile_detail_view(request, *args, **kwargs):
    user = request.user
    userprof = UserProfile.objects.filter(user = user.id)
    userprof_obj = userprof.first()
    qs = UserProfile.objects.filter(user = userprof_obj.user)
    if not qs.exists():
        return Response({})
    obj = qs.first()
    serializer = UserProfileSerializer(obj)
    return Response(serializer.data)

class userprofile_create_view(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "user"

# @api_view(['PUT'])
#   #@authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def userprofile_create_view(request, pk, *args, **kwargs):
#     instance = UserProfile.objects.filter(user=pk)
#     serializer = UserSerializer(instance, data=request.data)

#     if serializer.is_valid(raise_exception=True):
#         # create or update data
#         serializer.save()
#         print(request.user)
#         return Response(serializer.data)
#     return Response({"some error occurred"})

# class userprofile_create_view(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     def get_queryset(self):
#         user = self.request.user
#         userprof = UserProfile.objects.filter(user = user.id)
#         userprof_obj = userprof.first()
#         return User rofile.objects.filter(user = userprof_obj.user)
#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)
#     serializer_class = UserSerializer


# @api_view(['GET'])
# def userprofile_list_view(request, *args, **kwargs):
#     qs = UserProfile.objects.all().order_by('id')
#     serializer = UserSerializer(qs, many = True)
#     return Response(serializer.data)


