from django.urls import path

from .views import checklist_select, add_checklist, checklist_success, CarAutocompleteView, dangerous_cargo_checklist

urlpatterns = [
    path('select/', checklist_select, name='checklist_select'),
    path('checklist/add/',add_checklist , name='checklist_add'),
    path('checklist/success/', checklist_success, name='checklist_success'),
    path('car-autocomplete/', CarAutocompleteView.as_view(), name='car-autocomplete'),
    path('checklist/dangerous_cargo_checklist/', dangerous_cargo_checklist, name='dangerous_cargo_checklist')
        
]

