# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agreement(models.Model):
    agreement_id = models.AutoField(primary_key=True)
    school = models.ForeignKey('School', models.DO_NOTHING)
    status = models.CharField(max_length=20, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement'

    def __str__(self):
        school_name = getattr(self.school, "name", None) or "Sin escuela"
        return f"{school_name} (ID {self.agreement_id})"


class AppUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password_hash = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    role = models.CharField(max_length=20)
    active_flag = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'app_user'


class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey('Volunteer', models.DO_NOTHING)
    agreement = models.ForeignKey(Agreement, models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'


class AuditLog(models.Model):
    audit_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    record_id = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=20, blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    new_value = models.CharField(max_length=4000, blank=True, null=True)
    changed_by = models.CharField(max_length=50, blank=True, null=True)
    change_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClassSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    program = models.ForeignKey('Program', models.DO_NOTHING)
    session_date = models.DateTimeField()
    topic = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'class_session'

    def __str__(self):
        program_name = getattr(self.program, "name", None) or "Sesión"
        date_part = self.session_date.strftime("%Y-%m-%d") if self.session_date else "sin fecha"
        return f"{program_name} · {date_part}"


class Cohort(models.Model):
    cohort_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    period = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cohort'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EvaluationType(models.Model):
    eval_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_type'


class Help(models.Model):
    pk = models.CompositePrimaryKey('topic', 'seq')
    topic = models.CharField(max_length=50)
    seq = models.FloatField()
    info = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help'


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'

    def __str__(self):
        return self.name


class ProjectExpense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, models.DO_NOTHING, blank=True, null=True)
    school = models.ForeignKey('School', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    expense_date = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey(AppUser, models.DO_NOTHING, db_column='approved_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_expense'


class RedoDb(models.Model):
    dbid = models.FloatField()
    global_dbname = models.CharField(max_length=129, blank=True, null=True)
    dbuname = models.CharField(max_length=32, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    thread_field = models.FloatField(db_column='thread#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    resetlogs_scn_bas = models.FloatField(blank=True, null=True)
    resetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    resetlogs_time = models.FloatField()
    presetlogs_scn_bas = models.FloatField(blank=True, null=True)
    presetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    presetlogs_time = models.FloatField()
    seqno_rcv_cur = models.FloatField(blank=True, null=True)
    seqno_rcv_lo = models.FloatField(blank=True, null=True)
    seqno_rcv_hi = models.FloatField(blank=True, null=True)
    seqno_done_cur = models.FloatField(blank=True, null=True)
    seqno_done_lo = models.FloatField(blank=True, null=True)
    seqno_done_hi = models.FloatField(blank=True, null=True)
    gap_seqno = models.FloatField(blank=True, null=True)
    gap_ret = models.FloatField(blank=True, null=True)
    gap_done = models.FloatField(blank=True, null=True)
    apply_seqno = models.FloatField(blank=True, null=True)
    apply_done = models.FloatField(blank=True, null=True)
    purge_done = models.FloatField(blank=True, null=True)
    has_child = models.FloatField(blank=True, null=True)
    error1 = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    ts1 = models.FloatField(blank=True, null=True)
    ts2 = models.FloatField(blank=True, null=True)
    gap_next_scn = models.FloatField(blank=True, null=True)
    gap_next_time = models.FloatField(blank=True, null=True)
    curscn_time = models.FloatField(blank=True, null=True)
    resetlogs_scn = models.FloatField()
    presetlogs_scn = models.FloatField()
    gap_ret2 = models.FloatField(blank=True, null=True)
    curlog = models.FloatField(blank=True, null=True)
    endian = models.FloatField(blank=True, null=True)
    enqidx = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.DateField(blank=True, null=True)
    spare6 = models.CharField(max_length=65, blank=True, null=True)
    spare7 = models.CharField(max_length=129, blank=True, null=True)
    ts3 = models.FloatField(blank=True, null=True)
    curblkno = models.FloatField(blank=True, null=True)
    spare8 = models.FloatField(blank=True, null=True)
    spare9 = models.FloatField(blank=True, null=True)
    spare10 = models.FloatField(blank=True, null=True)
    spare11 = models.FloatField(blank=True, null=True)
    spare12 = models.FloatField(blank=True, null=True)
    tenant_key = models.FloatField()

    class Meta:
        managed = False
        db_table = 'redo_db'


class RedoLog(models.Model):
    dbid = models.FloatField()
    global_dbname = models.CharField(max_length=129, blank=True, null=True)
    dbuname = models.CharField(max_length=32, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    thread_field = models.FloatField(db_column='thread#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    resetlogs_scn_bas = models.FloatField(blank=True, null=True)
    resetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    resetlogs_time = models.FloatField()
    presetlogs_scn_bas = models.FloatField(blank=True, null=True)
    presetlogs_scn_wrp = models.FloatField(blank=True, null=True)
    presetlogs_time = models.FloatField()
    sequence_field = models.FloatField(db_column='sequence#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dupid = models.FloatField(blank=True, null=True)
    status1 = models.FloatField(blank=True, null=True)
    status2 = models.FloatField(blank=True, null=True)
    create_time = models.CharField(max_length=32, blank=True, null=True)
    close_time = models.CharField(max_length=32, blank=True, null=True)
    done_time = models.CharField(max_length=32, blank=True, null=True)
    first_scn_bas = models.FloatField(blank=True, null=True)
    first_scn_wrp = models.FloatField(blank=True, null=True)
    first_time = models.FloatField(blank=True, null=True)
    next_scn_bas = models.FloatField(blank=True, null=True)
    next_scn_wrp = models.FloatField(blank=True, null=True)
    next_time = models.FloatField(blank=True, null=True)
    first_scn = models.FloatField(blank=True, null=True)
    next_scn = models.FloatField(blank=True, null=True)
    resetlogs_scn = models.FloatField()
    blocks = models.FloatField(blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    old_blocks = models.FloatField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    error1 = models.FloatField(blank=True, null=True)
    error2 = models.FloatField(blank=True, null=True)
    filename = models.CharField(max_length=513, blank=True, null=True)
    ts1 = models.FloatField(blank=True, null=True)
    ts2 = models.FloatField(blank=True, null=True)
    endian = models.FloatField(blank=True, null=True)
    spare2 = models.FloatField(blank=True, null=True)
    spare3 = models.FloatField(blank=True, null=True)
    spare4 = models.FloatField(blank=True, null=True)
    spare5 = models.DateField(blank=True, null=True)
    spare6 = models.CharField(max_length=65, blank=True, null=True)
    spare7 = models.CharField(max_length=129, blank=True, null=True)
    ts3 = models.FloatField(blank=True, null=True)
    presetlogs_scn = models.FloatField()
    spare8 = models.FloatField(blank=True, null=True)
    spare9 = models.FloatField(blank=True, null=True)
    spare10 = models.FloatField(blank=True, null=True)
    old_status1 = models.FloatField(blank=True, null=True)
    old_status2 = models.FloatField(blank=True, null=True)
    old_filename = models.CharField(max_length=513, blank=True, null=True)
    tenant_key = models.FloatField()

    class Meta:
        managed = False
        db_table = 'redo_log'


class RemedialPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    trigger_eval = models.ForeignKey('StudentEvaluation', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remedial_plan'


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    location = models.CharField(max_length=150, blank=True, null=True)
    main_contact_name = models.CharField(max_length=100, blank=True, null=True)
    main_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'school'

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, models.DO_NOTHING)
    student_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    dni = models.CharField(unique=True, max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        parts = [self.last_name, self.first_name]
        name = ", ".join(filter(None, parts)) if any(parts) else str(self.student_id)
        if self.student_code:
            return f"{name} · {self.student_code}"
        return name


class StudentEnrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    cohort = models.ForeignKey(Cohort, models.DO_NOTHING)
    grade = models.CharField(max_length=20)
    section = models.CharField(max_length=10, blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_enrollment'
        unique_together = (('student', 'cohort'),)


class StudentEvaluation(models.Model):
    stu_eval_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    session = models.ForeignKey(ClassSession, models.DO_NOTHING)
    eval_type = models.CharField(max_length=50, blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_evaluation'


class Volunteer(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    specialty = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'volunteer'

    def __str__(self):
        name = ", ".join(filter(None, [self.last_name, self.first_name]))
        return name or str(self.volunteer_id)


class VolunteerApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey(Volunteer, models.DO_NOTHING)
    application_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    reviewed_by_user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteer_application'


class VolunteerEvaluation(models.Model):
    evaluation_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey(Volunteer, models.DO_NOTHING)
    eval_type = models.ForeignKey(EvaluationType, models.DO_NOTHING)
    evaluator_user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    result_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteer_evaluation'
