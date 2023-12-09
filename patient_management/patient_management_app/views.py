from django.shortcuts import render, redirect, get_object_or_404
from patient_management_app.models import HPatient,HBulletin,HStaff,HDept
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# def login_view(request):
#     return LoginView.as_view(template_name='login.html')(request)

def patient_list(request):
    patients = HPatient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


# views.py
def edit_patient(request, patient_id):
    patient = HPatient.objects.get(pk=patient_id)

    if request.method == 'POST':
        patient.patientname = request.POST.get('patient_name')
        patient.id_num = request.POST.get('id_num')
        patient.birth_date = request.POST.get('birth_date')
        patient.phone = request.POST.get('phone')
        patient.e_mail = request.POST.get('e_mail')
        patient.address = request.POST.get('address')
        # 处理其他表单字段

        patient.save()
        return redirect('patient_list')  # 重定向到患者列表页面

    return render(request, 'edit_patient.html', {'patient': patient})


def add_patient(request):

    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        id_num = request.POST.get('id_num')
        birth_date = request.POST.get('birth_date')
        phone = request.POST.get('phone')
        e_mail = request.POST.get('e_mail')
        address = request.POST.get('address')
        # 获取其他字段的数据

        if patient_name:  # 检查是否为空
            patient = HPatient(patientname=patient_name, id_num=id_num, birth_date=birth_date, phone=phone, e_mail=e_mail, address=address)
            patient.save()
            return redirect('patient_list')  # 重定向到患者列表页面或其他页面
        else:
            error_message = "Patient Name cannot be empty."
            return render(request, 'add_patient.html', {'error_message': error_message})

    return render(request, 'add_patient.html')

def delete_patient(request, patient_id):
    patient = get_object_or_404(HPatient, pk=patient_id)
    patient.delete()
    return redirect('patient_list')  # Redirect to the patient list page after deletion



def home(request):
    bulletins = HBulletin.objects.all()
    return render(request, 'bulletin.html', {'bulletins': bulletins})

def edit_bulletin(request,bulletin_id):
    bulletin = HBulletin.objects.get(pk=bulletin_id)

    if request.method == 'POST':
        bulletin.title = request.POST.get('title')
        bulletin.content = request.POST.get('content')
        # bulletin.dept = request.POST.get('dept')
        # bulletin.staff = request.POST.get('staff')
        # bulletin.date = request.POST.get('date')
        # bulletin.status = request.POST.get('status')
        # 处理其他表单字段

        bulletin.save()
        return redirect('home')  # 重定向到患者列表页面

    return render(request, 'edit_bulletin.html', {'bulletin': bulletin})
def add_bulletin(request):

        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            # bulletin.dept = request.POST.get('dept')
            # bulletin.staff = request.POST.get('staff')
            # bulletin.date = request.POST.get('date')
            # bulletin.status = request.POST.get('status')
            # 获取其他字段的数据

            if title:  # 检查是否为空
                bulletin = HBulletin(title=title, content=content)
                bulletin.save()
                return redirect('home')  # 重定向到患者列表页面或其他页面
            else:
                error_message = "Title cannot be empty."
                return render(request, 'add_bulletin.html', {'error_message': error_message})

        return render(request, 'add_bulletin.html')

def delete_bulletin(request, bulletin_id):
    bulletin = get_object_or_404(HBulletin, pk=bulletin_id)
    bulletin.delete()
    return redirect('home')  # Redirect to the patient list page after deletion

def staff_list(request):
    staffs = HStaff.objects.all()
    depts = HDept.objects.all()


    return render(request, 'staff_list.html', {'staffs': staffs, 'depts': depts})

def edit_staff(request,staff_id):
    staff = HStaff.objects.get(pk=staff_id)

    if request.method == 'POST':
        staff.user_id = request.POST.get('user_id')
        staff.s_c_name = request.POST.get('s_c_name')
        staff.s_e_name = request.POST.get('s_e_name')
        staff.position = request.POST.get('position')
        staff.dept = request.POST.get('dept')
        staff.username = request.POST.get('username')
        staff.password = request.POST.get('password')
        # 处理其他表单字段

        staff.save()
        return redirect('staff_list')  # 重定向到患者列表页面

    return render(request, 'edit_staff.html', {'staff': staff})

def add_staff(request):

            if request.method == 'POST':
                user_id = request.POST.get('user_id')
                s_c_name = request.POST.get('s_c_name')
                s_e_name = request.POST.get('s_e_name')
                position = request.POST.get('position')
                # dept = request.POST.get('dept')
                username = request.POST.get('username')
                password = request.POST.get('password')
                # 获取其他字段的数据

                if user_id:  # 检查是否为空
                    staff = HStaff(user_id=user_id, s_c_name=s_c_name, s_e_name=s_e_name, position=position, username=username, password=password)
                    staff.save()
                    return redirect('staff_list')  # 重定向到患者列表页面或其他页面
                else:
                    error_message = "User ID cannot be empty."
                    return render(request, 'add_staff.html', {'error_message': error_message})

            return render(request, 'add_staff.html')

def delete_staff(request, staff_id):
    staff = get_object_or_404(HStaff, pk=staff_id)
    staff.delete()
    return redirect('staff_list')  # Redirect to the patient list page after deletion




# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate

# class CustomAuthenticationForm(AuthenticationForm):
#     user = None  # 添加 user 属性

#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             # 在这里执行你的自定义身份验证逻辑，例如验证用户名和密码是否匹配 HStaff 模型中的记录
#             self.user = authenticate(username='username', password='password', model=HStaff)

#             # 如果验证失败，可以使用 forms.ValidationError 抛出错误
#             if self.user is None or not self.user.is_active:
#                 raise forms.ValidationError('用户名或密码不正确')

#         return self.cleaned_data



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from patient_management_app.forms import CustomAuthenticationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 使用管理员账户进行身份验证
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 登录成功后重定向到适当的页面

    return render(request, 'login.html')