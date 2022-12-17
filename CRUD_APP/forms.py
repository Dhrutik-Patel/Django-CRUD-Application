from django import forms
from CRUD_APP.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('full_name', 'mobile_no', 'employee_no', 'employee_position')
        labels = {
            'full_name': 'Full Name',
            'mobile_no': 'Mobile No',
            'employee_no': 'Employee No',
            'employee_position': 'Employee Position'
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['employee_position'].empty_label = 'Please select employee position'
