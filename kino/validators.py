import os
from django.core.exceptions import ValidationError
def validate_file_extension(value):
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.jpg','.jpeg','.gif','.png']
  if not ext in valid_extensions:
    raise ValidationError(u'Файл не подходит!')