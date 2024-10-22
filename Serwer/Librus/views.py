from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Librus.models import Student, Grade
from Librus.serializer import GradeSerializer


class StudentGradesView(APIView):

    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
            grades = student.grades.all()
            grades_data = [GradeSerializer(g).data for g in grades]
            return JsonResponse(grades_data, safe=False)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        