from rest_framework.decorators import api_view
from rest_framework.response import Response

from school.models import Class, Student


@api_view(['POST'])
def studentPromoteView(request):
    studentId = request.data.get('studentId')
    classId = request.data.get('classId')

    student = Student.objects.get(pk=studentId)
    newClass = Class.objects.get(pk=classId)
    student.currentClass = newClass
    student.save()

    return Response({'Promote': 'Success'}, status=200)
