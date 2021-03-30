from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Heartrate
from .serializers import HeartRateSerializer
import time


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")


@api_view(['GET'])
def printBPM(request):
    f = open("bpm_log.txt", 'r')
    temp = f.readline()
    temp = temp.split('/')
    bpm = int(temp[1])
    time_str = temp[0]
    model = Heartrate(BPM= bpm, time=time_str)
    model.save()
    model_form = Heartrate.objects.all()
    serializer = HeartRateSerializer(model_form, many=True)
    return Response(data=serializer.data)
    #return render(data=serializer.data, 'print_bpm.html')
