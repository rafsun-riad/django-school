from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    brithDate = models.DateField()
    currentClass = models.ForeignKey(
        Class, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class ClassSubject(models.Model):
    classObj = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='class_subject')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='class_subject')

    class Meta:
        unique_together = ('classObj', 'subject')

    def __str__(self):
        return f'{self.classObj.name} - {self.subject.name}'


class Mark(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='marks')
    classObj = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='marks')
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.marks}'
