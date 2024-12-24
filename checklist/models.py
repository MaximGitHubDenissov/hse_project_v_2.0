from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User 


class Direction(models.Model):
    name = models.CharField(_("Direction/Subcontractor name"), max_length=25)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Direction")
        

class Car(models.Model):
    number = models.CharField(_("Plate number"), max_length=10)
    direction = models.ForeignKey(Direction,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.number
    
class CheckList(models.Model):
    CHOICES = [
        (1, _('YES')),
        (0, _('NO')),
        (2, _('N/A')),
    ]

    FLAG_CHOICES = [
        (1, _('Critical')),
        (2, _('Need correction')),
        (3, _('OK')),
    ]

    date = models.DateField(_('Date'))
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=_('Car'))
    driver = models.CharField(_('Driver name'), max_length=25)
    comments = models.CharField(max_length=350, verbose_name=_('Corrective actions'), blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'), related_name="checklists")

    # Поля для инспекций
    INSPECTION_FIELDS = ['fuel', 'oil', 'brake_fluid', 'cooling_fluid', 'windshield_fluid', 
                         'headlights', 'reversing_lights', 'turn_and_stop_lights',
                         'steering', 'clutch', 'brake', 'monitoring_devices', 'heater_conditioner', 'wipers',
                         'beep', 'reverse_signal', 'gps', 'dvr', 'battery',
                         'inside_outside', 'mirrors', 'seat_belts', 'tires', 'discs', 'number_plate', 'wheel_nuts',
                         'fire_extinguisher', 'first_aid_kit', 'tools', 'spare_wheel', 'warning_triangel', 'wheel_chocks',
                         'phone', 'vest', 'flagpole',
                         'driver_license', 'car_docs',]
    
    CRITICAL_FIELDS = ['brake_fluid', 'headlights', 'reversing_lights', 'turn_and_stop_lights',
                       'steering', 'clutch', 'brake', 'seat_belts', 'tires', 'discs', 'wheel_nuts',]
    
    NEED_CORRECTION_FIELDS = ['wipers', 'beep', 'fire_extinguisher', 'first_aid_kit', 'warning_triangel', 'wheel_chocks', 
                              'flagpole',]

    # Генерация оценочных и флаговых полей
    for field in INSPECTION_FIELDS:
        # Поля для оценок
        vars()[f'{field}_mark'] = models.IntegerField(
            choices=CHOICES,
            verbose_name=_(f'{field.replace("_", " ").capitalize()} mark')
        )
        # Поля для флагов
        vars()[f'{field}_flag'] = models.IntegerField(
            choices=FLAG_CHOICES, default=3,
            verbose_name=_(f'{field.replace("_", " ").capitalize()} status')
        )
        # Поля для комментариев
        vars()[f'{field}_comment'] = models.CharField(
            max_length=100,
            verbose_name=_(f'{field.replace("_", " ").capitalize()} comment'), blank=True
        )
    
    class Meta:
        verbose_name = _('Checklist')
        verbose_name_plural = _('Checklists')

    def __str__(self):
        return f"{self.date} - {self.car} - {self.driver}"
    
 
    def save(self, *args, **kwargs):
        # Устанавливаем флаг "Critical" для критичных полей
        if not self.pk:  # Проверяем, если запись новая
            for field in self.INSPECTION_FIELDS:
                if field in self.CRITICAL_FIELDS:
                    setattr(self, f"{field}_flag", 1)  # Устанавливаем "Critical" (1)
                elif field in self.NEED_CORRECTION_FIELDS:
                    setattr(self, f"{field}_flag", 2) # Устанавливаем "Need correction" (2)
                    
        super().save(*args, **kwargs)
        
        
class DangerousCargoChecklist(CheckList):
    
    CARGO_FIELDS = ['vehicle_approval', 'driver_approval', 'license_card', 'driver_instruction', 'emergency_plan',
                    'waybill' , 'contacts', 'transportation_form', 'danger_waybill',
                    'danger_signs', 'no_entry_sign', 'signal_tape',
                    'acid_ppe', 'valves_pressure', 'valves_leakage', 'hatch', 'level_sensor', 'drainage', 'ladder',
                    'water', 'soda', 'radiation_signs',
                    'mount', 'ammonium_rad_signs', 'tuk_fastenings',
                    'canopy', 'cargo_condition', 'cleanliness', 'exhaust_pipe',
                    'sleeves', 'oil_valves_leakage', 'oil_hatch', 'oil_ladder', 'blanket', 'chain']
    
    for field in CARGO_FIELDS:
         vars()[f'{field}_mark'] = models.IntegerField(
            choices=CheckList.CHOICES,
            verbose_name=_(f'{field.replace("_", " ").capitalize()} mark')
        )
         vars()[f'{field}_comment'] = models.CharField(
            max_length=100,
            verbose_name=_(f'{field.replace("_", " ").capitalize()} comment'), blank=True
        )
         
    class Meta:
        verbose_name = _('Dangerous cargo checklist')
        verbose_name_plural = _('Dangerous cargo checklists')
        
    def __str__(self):
        return super().__str__()
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)         