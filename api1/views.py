from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais
from .serializers import PaisSerializador

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def pais(request):
    print(request)
    if request.method == 'GET':
        snippets = Pais.objects.all()
        serializer = PaisSerializador(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = PaisSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
