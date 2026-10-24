from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.serializers import StudentSerializer,CourseSerializer
from . models import Student,Course
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


'''
@api_view(['GET','POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        print(students)
        print(serializer)
        return Response (serializer.data)

    elif request.method =="POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','POST'])
def course_list_create(request):  
    if request.method == 'POST':
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    elif request.method =='GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

'''        
class StudentListCreate(APIView):
    def get(self,request):
        students = Student.objects.all()
        course_id = request.query_params.get('course')
        search = request.query_params.get('search')
        if search:
            students = students.filter(Q(name__icontains = search) | Q(email__icontains = search))
        serializer = StudentSerializer(students,many = True)
        return Response (serializer.data)


    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Student,pk=pk)    

    def get (self,request,pk):
        students = self.get_object(pk)
        serializer = StudentSerializer(students)
        return Response(serializer.data)

    def put(self,request,pk):
        students = self.get_object(pk)
        serializer = StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        students = self.get_object(pk)
        serializer = StudentSerializer(students, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        students = self.get_object(pk)
        students.delete()
        return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)

class CourseListCreate(APIView):
    def get(self,request):
        courses = Course.objects.all()
        search = request.query_params.get('search')
        if search:
            courses = courses.filter(Q(name__icontains=search))
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)    

    def post(self,request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseListView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Course,pk=pk)    

    
    def get (self,request,pk):
        courses = self.get_object(pk)
        serializer = CourseSerializer(courses)
        return Response(serializer.data)

    def put(self,request,pk):
        courses = self.get_object(pk)
        serializer = CourseSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# delete function
    def delete(self,request,pk):
        #course = self.get_object(pk)
        course = self.get_object(pk)
        course.delete()
        return Response("Deleted ", status=status.HTTP_204_NO_CONTENT)

    
