from django.db import models

class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=4)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)  # usa hash en la práctica
    firstname = models.CharField(max_length=18, blank=True)
    lastname = models.CharField(max_length=18, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, blank=True)
    role = models.CharField(max_length=11)
    activeflag = models.BooleanField(default=True)

    class Meta:
        db_table = "user"


class Volunteer(models.Model):
    volunteerid = models.CharField(primary_key=True, max_length=4)
    dni = models.CharField(max_length=8, unique=True)
    firstname = models.CharField(max_length=18)
    lastname = models.CharField(max_length=18)
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=20, blank=True)
    experiencetext = models.TextField(blank=True)
    registrationdate = models.DateField()
    status = models.CharField(max_length=14)

    class Meta:
        db_table = "volunteer"


class School(models.Model):
    schoolid = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50, unique=True)
    ubication = models.CharField(max_length=70, blank=True)
    maincontactname = models.CharField(max_length=40, blank=True)
    maincontactphone = models.CharField(max_length=11, blank=True)
    needssummary = models.TextField(blank=True)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = "school"


class Student(models.Model):
    studentid = models.CharField(primary_key=True, max_length=4)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    studentcode = models.CharField(max_length=10, unique=True, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True, null=True, blank=True)
    firstname = models.CharField(max_length=18)
    lastname = models.CharField(max_length=18)
    birthdate = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    section = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = "student"


class Agreement(models.Model):
    agreementid = models.CharField(primary_key=True, max_length=4)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    agreementstatus = models.CharField(max_length=20)
    filepath = models.CharField(max_length=150)
    signedby = models.CharField(max_length=40, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "agreement"


class Assignment(models.Model):
    assignmentid = models.CharField(primary_key=True, max_length=4)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    agreement = models.ForeignKey(Agreement, null=True, blank=True, on_delete=models.SET_NULL)
    startdate = models.DateField()
    enddate = models.DateField()
    role = models.CharField(max_length=30)
    assignmentstatus = models.CharField(max_length=13)

    class Meta:
        db_table = "assignment"


class Session(models.Model):
    sessionid = models.CharField(primary_key=True, max_length=4)
    sessiondate = models.DateTimeField()
    topic = models.CharField(max_length=255)

    class Meta:
        db_table = "session"


class StudentEvaluation(models.Model):
    stuevalid = models.CharField(primary_key=True, max_length=4)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    evaldate = models.DateField()
    evaltype = models.CharField(max_length=30, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    attendanceflag = models.BooleanField(default=True)
    comments = models.TextField(blank=True)
    createdbyuser = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "studentevaluation"
