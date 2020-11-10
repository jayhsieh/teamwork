from django.shortcuts import render
from subprocess import Popen, PIPE


# Create your views here.
def dwarf_home(request):
    return render(request, 'index.html')
    # return HttpResponse("dwarf_home")


def start_zookeeper(request):
    cmd1 = 'bash /home/ken/installed/zookeeper/bin/start_zookeeper.sh'
    p1 = Popen(cmd1, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True)
    response = p1.stdout.read()

    cmd2 = 'lsof -i :2181 | wc -l'
    q = Popen(cmd2, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True)

    if int(q.stdout.read()) > 0:
        response = 'Zoo is open now.'
    else:
        response = 'Zoo is not ready yet.'
    return render(request, 'index.html', locals())


def start_kafka(request):
    cmd1 = 'bash /home/ken/installed/kafka/bin/start_kafka.sh'
    p1 = Popen(cmd1, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True)
    response = p1.stdout.read()

    cmd2 = 'lsof -i :9092 | wc -l'
    q = Popen(cmd2, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True)

    if int(q.stdout.read()) > 0:
        response = 'kafka is on.'
    else:
        response = "kafka is still sleeping."
    return render(request, 'index.html', locals())


def stop_kafka(request):
    cmd1 = 'bash /home/ken/installed/kafka/bin/stop_kafka.sh'
    p1 = Popen(cmd1, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True)
    response = p1.stdout.read()

    cmd2 = 'lsof -i :9092 | wc -l'
    q = Popen(cmd2, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True)

    if int(q.stdout.read()) > 0:
        response = 'kafka is still on.'
    else:
        response = "kafka is off."
    return render(request, 'index.html', locals())
