from unicodedata import normalize
from django.utils import timezone
from django.utils.encoding import smart_unicode
from barista.restaurants.models import Restaurant


def convert_to_readable(string):
    """
    Converts given unicode string to readeable ascii format with legal characters
    """

    # check if unicode or not
    if isinstance(string, unicode):
        readable_string = normalize('NFKD',string)
    else:
        readable_string = string
    # turn into ascii format for readability
    readable_string = readable_string.encode('ascii','ignore')
    # replace/delete every character that is not alpha-numeric in format
    return "".join(character for character in readable_string if character.isalnum())


def create_unique_name(obj):
    """
    Creates generic names
    """

    basic_name = obj.name.lower()
    if not basic_name:
        basic_name = "Restaurant"
    basic_name = convert_to_readable(basic_name)

    #if either of the email first name or last name fields arent given then a serial number is generated
    if Restaurant.objects.filter(name=basic_name).exists():
        i = 0
        temp_name = basic_name
        while Restaurant.objects.filter(name = temp_name).exists():
            i+=1
            temp_name = smart_unicode("%s%s"%(basic_name,i))
        name = temp_name
    else:
        name = basic_name
    return name


def is_lunchtime():
    """
    Checks whether user can vote or not
    """
    current_time = timezone.localtime(timezone.now()).hour
    if current_time <= 15 or current_time >= 17:
        return False
    return True