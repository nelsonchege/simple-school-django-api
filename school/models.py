from django.db import models

# Create your models here.
class System_user(models.Model):

    categoeries = (
        ('Teacher','Teacher'),
        ('Student','Student'),
    )
    genders = (
        ('Male','Male'),
        ('Female','Female'),
    )
    users_name = models.CharField(max_length=200)
    users_age  = models.IntegerField()
    gender     = models.CharField(max_length = 50,null=True ,choices=genders)
    role       = models.CharField(max_length=200,null=True ,choices=categoeries)
    
    def __str__(self):
        return  str(self.id)

class Teacher(models.Model):
    system_id                   = models.CharField(blank=True,max_length=200)
    teachers_id                 = models.ForeignKey(System_user,on_delete=models.CASCADE)
    teachers_date_of_employment = models.DateField()
    teachers_department         = models.CharField(max_length=200)
    
    def save(self):
        teachersId = str(self.teachers_id)
        self.system_id = 'T-00'+teachersId
        super().save()

    def __str__(self):
        return  str(self.system_id)
    
class Student(models.Model):
    system_id         = models.CharField(blank=True,max_length=200)
    student_id        = models.ForeignKey(System_user,on_delete=models.CASCADE)
    student_class     = models.CharField(max_length=200)
    student_dormitory = models.CharField(max_length=200)
    
    def save(self):
        studentsId = str(self.student_id)
        self.system_id = 'S-00'+studentsId
        super().save()

    def __str__(self):
        return  str(self.id)


# Users -.primary key(id), name, age, dob, gender,  role
# Students - primary key (id using format “S-001”), foreign key(user_id), class, dormitory 
# Teachers - primary key(id using format “T-001”), foreign key(user_id), department, date of employment