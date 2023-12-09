# myapp/serializers.py

from rest_framework import serializers
from .models import HPatient  # 请根据您的项目目录结构导入模型类

class HPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = HPatient  # 指定要序列化的模型
        fields = [
            'firstvisit_date',
            'patientname',
            'gender',
            'id_num',
            'birth_date',
            'dept_id',
            'phone',
            'address',
            'e_mail',
            'chart_id',
            'blood_type',
            'd_rh',
            'organ_donation',
            'dnr',
            'participant_cat',
            'health_insurance',
        ]