from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from .models import File, ProcessLog
from os import walk
from .utils import (
    log,
    task1,
    task2,
    task3
)


def dash_view(request):
    if request.method == "POST":
        file_name = request.POST.get('file-name')
        file = request.FILES.get('file')
        slug = slugify(file_name)

        File.objects.create(
            file_name=file_name,
            slug=slug,
            file=file,
        ).save()

    task1_files = []
    task2_files = []
    task3_files = []

    for (dirpath, dirnames, filenames) in walk('media/process1'):
        task1_files.extend(filenames)
    for (dirpath, dirnames, filenames) in walk('media/process2'):
        task2_files.extend(filenames)
    for (dirpath, dirnames, filenames) in walk('media/process3'):
        task3_files.extend(filenames)

    files = File.objects.order_by('-time_stamp')
    context = {
        'title': "Dashboard",
        'files': files,
        'task1_files': task1_files,
        'task2_files': task2_files,
        'task3_files': task3_files
    }

    return render(request, 'dash/home.html', context)


def process_log_view(request):
    process_logs = ProcessLog.objects.order_by('-time_stamp')
    context = {
        'title': 'Process Log',
        'process_logs': process_logs
    }
    return render(request, 'dash/log.html', context)


# Task 1
def task1_endpoint(request, file_name):
    raw_file_path = "media/raw/" + file_name
    log("Processing File: " + raw_file_path)
    log("Initiating Task 1")

    task1(str(file_name))

    return redirect('/')

# Task 2
def task2_endpoint(request, file_name):
    raw_file_path = "media/raw/" + file_name
    log("Processing File: " + raw_file_path)
    log("Initiating Task 2")

    task2(str(file_name))

    return redirect('/')

# Task 2
def task3_endpoint(request, file_name):
    raw_file_path = "media/raw/" + file_name
    log("Processing File: " + raw_file_path)
    log("Initiating Task 3")

    task3(str(file_name))

    return redirect('/')