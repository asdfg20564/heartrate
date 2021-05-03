from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Heartrate
from .serializers import HeartRateSerializer

# Create your views here.
@api_view(['GET'])
def printLOG(request):
    f = open("data_log.txt", 'r')
    temp = f.readline()
    temp = temp.split('/')
    time_str = temp[0]
    bpm = int(temp[1])
    resp = int(temp[2])
    #time_str=time.strftime('%Y-%m-%d %h:%M:%S', time.localtime(time.time()))
    model = Heartrate(BPM = bpm, RESP = resp, time = time_str)
    model.save()
    model_form = Heartrate.objects.all()
    serializer = HeartRateSerializer(model_form, many=True)
    return Response(data=serializer.data)
    #return render(data=serializer.data, 'print_bpm.html')

@api_view(['GET'])
def printCUR(request):
    f = open("data_log.txt", 'r')
    temp = f.readline()
    temp = temp.split('/')
    time_str = temp[0]
    bpm = int(temp[1])
    resp = int(temp[2])
    #time_str=time.strftime('%Y-%m-%d %h:%M:%S', time.localtime(time.time()))
    model = Heartrate(BPM = bpm, RESP = resp, time = time_str)
    model.save()
    model_form = Heartrate.objects.order_by('-id').last()
    serializer = HeartRateSerializer(model)
    return Response(data=serializer.data)