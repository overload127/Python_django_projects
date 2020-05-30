from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
import magic


def validate_mp4(value):
    if isinstance(value.file, TemporaryUploadedFile):
        type_file_inside = magic.from_file(value.file.temporary_file_path(), mime=True)
    elif isinstance(value.file, InMemoryUploadedFile):
        type_file_inside = magic.from_buffer(value.file.read(100), mime=True)
    else:
        raise ValidationError('Ошибка на сервере.')

    if type_file_inside == 'video/mp4':
        return value
    else:
        answer = 'Нужно выбрать файл формата mp4. Вы пытались '\
                f'загрузить файл {value.name} и он отличается от '\
                 'необходимого формата'
        raise ValidationError(answer)
