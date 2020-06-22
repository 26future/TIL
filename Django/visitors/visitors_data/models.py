from django.db import models
from django.core.exceptions import ValidationError
# from .validators import validate_number

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=5)
    number = models.CharField(max_length=11, validators=[])
    number2 = models.CharField(max_length=11)
    date = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=10)

    def number_validator(self, *args, **kwargs):
        number = self.number
        number2 = self.number2
    
        if number != number2:
            print('----------')
            msg = '전화번호를 다시 확인해주세요'
            raise ValidationError(msg)
        
        