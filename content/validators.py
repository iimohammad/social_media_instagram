from django.core.exceptions import ValidationError


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg',
                        '.png', '.gif', '.mp4', '.avi', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_hashtag(value):
    if not value.startswith('#'):
        raise ValidationError('Hashtag must start with #')
