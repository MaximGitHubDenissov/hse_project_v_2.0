from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CheckListForm, DangerousCargoCheckListForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from .models import CheckList, Car
from django.http import JsonResponse
from django.views import View


# Это для тестовой проверки, не забудь поменять base и index !!!


@login_required
def checklist_select(request):
    return render(request, 'select.html')

@login_required
def add_checklist(request):
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.author = request.user
            checklist.save()
            print('ОК')
            return redirect(reverse('checklist_success'))
        else: print('NO')
        
    
    else:
        form = CheckListForm()    
        context = {'form': form}
        return render(request, 'checklist_form.html', context=context)
    
@login_required    
def checklist_success(request):
    return render(request, 'checklist_success.html')



class CarAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')  # Получаем текст, введенный пользователем
        if query:
            cars = Car.objects.filter(number__icontains=query)[:10]  # Ограничиваем 10 результатами
            results = [{'id': car.id, 'text': car.number} for car in cars]
        else:
            results = []
        return JsonResponse({'results': results})


@login_required
def dangerous_cargo_checklist(request):
    if request.method == 'POST':
        form = DangerousCargoCheckListForm(request.POST)
        if form.is_valid:
            checklist = form.save(commit=False)
            checklist.author = request.user
            checklist.save()
            print('ОК')
            return redirect(reverse('checklist_success'))
        else: print('NO')
        
    
    else:
        form = DangerousCargoCheckListForm()    
        context = {'form': form}
        return render(request, 'danger_cargo_checklist_form.html', context=context)