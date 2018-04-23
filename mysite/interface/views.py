from django.shortcuts import render
from .models import Chapter,Course,Department,Material
from django.http import HttpResponse
# Create your views here.

def department(request):
    courses = Department.objects.order_by('title')
    chapters = []
    if courses:
        for x in courses:
            chapters.append(Course.objects.filter(department=x).count())
    else:
        chapters = 0
    if not courses:
        return HttpResponse("<p>No Departments Registered Yet contact DC</p>")
    courses = zip(courses, chapters)
    return render(request, 'interface/index.html', {'courses': courses})


def course(request,department_id):
    dpt = Department.objects.filter(pk=department_id)
    courses = Course.objects.filter(department=dpt[0])
    chapters=[]
    if courses:
        for x in courses:
            chapters.append(Chapter.objects.filter(course=x).count())
    else:
        chapters=0
    courses = zip(courses, chapters)
    if not courses:
        return HttpResponse("<p>No Courses Registered Yet contact DC</p>")
    return render(request, 'interface/interface.html', {'courses':courses,'dpt':dpt})

def chapters(request,course_id):
    course = Course.objects.filter(pk=course_id)
    chapterk=Chapter.objects.filter(course=course[0])
    pdfs=[]
    for x in chapterk:
        if Material.objects.filter(chapter=x):
            pdfs.append(Material.objects.filter(chapter=x))
        else:
            pdfs.append('')
    if not chapterk:
        return HttpResponse("<p>No Chapter Registered Yet contact DC</p>")
    chapter = zip(chapterk,pdfs)
    return render(request,'interface/interface_chapter.html',{'chapter':chapter,'course':course})



