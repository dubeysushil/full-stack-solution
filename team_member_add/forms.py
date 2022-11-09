from django import forms
from .models import TeamMember
import re

class TeamMemberForm(forms.ModelForm):
    
    class Meta:
        model = TeamMember
        fields = '__all__'
        widgets = {
            'role': forms.RadioSelect()
        }
        
        
    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['placeholder'] = 'First Name'
        self.fields['lastName'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email ID'
        self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Phone Number'
        for key, field in self.fields.items():
            field.label = ""
        self.fields['role'].label = 'Role'
        
    def clean(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        super(TeamMemberForm, self).clean()
        phoneNumber = self.cleaned_data.get('phoneNumber')
        email = self.cleaned_data.get('email')
        if len(str(phoneNumber)) != 10 :
            self._errors['phoneNumber'] = self.error_class([
                'Invalid phone number'])
        if re.fullmatch(regex, email):
            print("valid")
        else:
            self._errors['email'] = self.error_class([
                'Invalid email id'])
        # return any errors if found
        return self.cleaned_data