from rest_framework.decorators import api_view
from app.models import Poc
from app.serializers import PocSerializer
from rest_framework.response import Response

@api_view(['GET'])
def poc_list(request):
    poc = Poc.objects.all()
    serializer = PocSerializer(poc, many=True)
    return Response(serializer.data)