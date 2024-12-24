from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CheckList, DangerousCargoChecklist

from django_select2.forms import Select2Widget

class CheckListForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}), 
                           label=_('Date'))
    driver = forms.CharField(label=_('Enter driver name'), max_length=25)
    comments = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%;height:100%'}))
    
    class Meta:
        model = CheckList
        exclude = [item + '_flag' for item in CheckList.INSPECTION_FIELDS ]
        exclude += ['author']
        widgets = {
            'car': Select2Widget(
                attrs={
                    'data-placeholder': _('Enter plate number'),  # Плейсхолдер
                    'data-url': '/car-autocomplete/',           # URL для AJAX
                    'style': 'width: 127px;',                   # Ширина виджета
                }
            ),
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        inspection_fields = CheckList.INSPECTION_FIELDS
        
        for field in inspection_fields: 
            mark_field_name = f'{field}_mark'
            self.fields[mark_field_name].widget = forms.RadioSelect(choices=CheckList.CHOICES)
            
            comment_field_name = f'{field}_comment'
            self.fields[comment_field_name] = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%;height:70px'}), max_length=100, required=False)
            
        self.fields['driver'].widget.attrs.update({'class': 'driver-field'})
        self.fields['car'].label = _('Enter plate number')
        
         
  
class DangerousCargoCheckListForm(CheckListForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        inspection_fields = DangerousCargoChecklist.CARGO_FIELDS
    
        for field in inspection_fields: 
            mark_field_name = f'{field}_mark'
            self.fields[mark_field_name].widget = forms.RadioSelect(choices=CheckList.CHOICES)
        
            comment_field_name = f'{field}_comment'
            self.fields[comment_field_name] = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%;height:70px'}), max_length=100, required=False)
                
    class Meta:
        model = DangerousCargoChecklist
        exclude = [item + '_flag' for item in CheckList.INSPECTION_FIELDS]
        exclude += ['author']
        widgets = {
            'car': Select2Widget(
                attrs={
                    'data-placeholder': _('Enter plate number'),  # Плейсхолдер
                    'data-url': '/car-autocomplete/',           # URL для AJAX
                    'style': 'width: 127px;',                   # Ширина виджета
                }
            ),
        }
               

                        
            
            
    
 

