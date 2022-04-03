from django import forms


class CityForm(forms.Form):
    CityName = forms.CharField(max_length=200,label='Search City or Zip Code')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fields_name in self.fields:
            field = self.fields.get(fields_name)
            self.fields[fields_name].widget.attrs.update({'placeholder':field.label})