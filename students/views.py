from django.shortcuts import render, redirect
from django.db.models import Min, Max, Avg
from .models import Student

print("LOADED students.views", flush=True)

# Create your views here.
def home_view(request, errorList=None, formData=None):

    studentList = Student.objects.all().order_by('-studentId')
    studentCount = Student.objects.count()

    if studentCount > 0:
        minGrade = Student.objects.aggregate(Min('grade'))['grade__min']
        maxGrade = Student.objects.aggregate(Max('grade'))['grade__max']
        avgGrade = Student.objects.aggregate(Avg('grade'))['grade__avg']
        avgGrade = int(avgGrade)
    else:
        minGrade = None
        maxGrade = None
        avgGrade = None

    if studentCount >= 20:
        errorList = ['Student maximum has been reached']

    print(f"MinGrade: {minGrade}")
    return render(request
            , 'students/index.html' 
            , {'studentList': studentList
            , 'studentCount': studentCount
            , 'minGrade': minGrade
            , 'maxGrade': maxGrade
            , 'avgGrade': avgGrade
            , 'errorList': errorList or []
            , 'formData': formData
            }
        )


def validateStudentData(request):
    print("validation initiated")

    errorList =[]
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    grade = request.POST.get('grade')

    if Student.objects.count() >= 20:
        print("validation complete")
        errorList.append('Student maximum has been reached')
        print(f"errors found: {errorList}")
        return request, errorList

    #confirms name is not empty
    if not firstName:
        errorList.append('First Name is required')
        print("error found firstName")

    #confirms lastName is not empty
    if not lastName:
        errorList.append('Last Name is required')
        print("error found lastName")

    #Error handling for empty/non int grade entries
    if grade:
        try:
            grade = int(grade)
        except ValueError:
            grade = None
            errorList.append('Grade must be a number')

    #Confirms grade is between 50 and 100
    if grade:
        if grade <50 or grade >100:
            errorList.append('Grade must be between 50 and 100')
            print("error found grade")
    else:
        errorList.append('Grade is required')


    print("validation complete")
    print(f"errors found: {errorList}")
    return request, errorList


def submitButton(request):
    request, errors = validateStudentData(request)

    #if there are no errors
    if not errors:
        student = Student(
            firstName = request.POST.get('firstName'),
            lastName = request.POST.get('lastName'),
            grade = int(request.POST.get('grade'))
        )

        student.save()
        return redirect('home')

    #if there are errors
    else:
        if Student.objects.count() >= 20:
            return redirect('home')
        else:
            return home_view(request, errors, request.POST)
    
def clearStudentsButton(request):
    Student.objects.all().delete()
    return redirect('home')

    

