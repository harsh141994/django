from django.core.exceptions import ValidationError
#for validating the values entered while creating the object(restaurantlocation)

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def validate_email(value):
        email = value
        if ".edu" in email:
            raise ValidationError("We do not accept edu emails")



CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(" not a valid category")