from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class HBulletin(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1024, blank=True, null=True)
    dept = models.ForeignKey('HDept', models.DO_NOTHING, db_column='dept')
    staff = models.ForeignKey('HStaff', models.DO_NOTHING, db_column='staff')
    date = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'h_bulletin'
        app_label = 'patient_management_app'


class HCasehistory(models.Model):
    id = models.OneToOneField('HPatient', models.DO_NOTHING, db_column='id', primary_key=True)
    food_allergies = models.CharField(max_length=500)
    medicine_allergies = models.CharField(max_length=500)
    family_inheritance = models.CharField(max_length=500)
    infectious_disease = models.CharField(max_length=500)
    major_injury = models.CharField(max_length=500)
    surgical_record = models.CharField(max_length=1000)
    doctor_advice = models.CharField(max_length=1000)
    remark = models.CharField(max_length=1000)
    prime_doc = models.ForeignKey('HStaff', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_casehistory'
        app_label = 'patient_management_app'


class HDept(models.Model):
    names = models.CharField(max_length=10)
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'h_dept'
        app_label = 'patient_management_app'


class HMedicine(models.Model):
    chinese_name = models.CharField(max_length=128, blank=True, null=True)
    english_name = models.CharField(max_length=128, blank=True, null=True)
    dosage = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_medicine'
        app_label = 'patient_management_app'


class HPatient(models.Model):
    firstvisit_date = models.CharField(max_length=20)
    patientname = models.CharField(max_length=20)
    gender = models.IntegerField()
    id_num = models.CharField(max_length=10)
    birth_date = models.CharField(max_length=20)
    dept_id = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=30)
    e_mail = models.CharField(db_column='e-mail', max_length=30)  # Field renamed to remove unsuitable characters.
    chart_id = models.IntegerField()
    blood_type = models.CharField(max_length=2)
    d_rh = models.IntegerField()
    organ_donation = models.IntegerField(db_column='organ-donation')  # Field renamed to remove unsuitable characters.
    dnr = models.IntegerField()
    participant_cat = models.CharField(max_length=2)
    health_insurance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'h_patient'
        app_label = 'patient_management_app'


class HStaff(models.Model):
    user_id = models.CharField(max_length=5)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=64)
    create_time = models.CharField(max_length=10)
    s_c_name = models.CharField(max_length=20)
    s_e_name = models.CharField(max_length=32)
    gender = models.IntegerField()
    position = models.CharField(max_length=64)
    dept = models.ForeignKey(HDept, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'h_staff'
        app_label = 'patient_management_app'

