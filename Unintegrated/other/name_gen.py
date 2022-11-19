from datetime import datetime
import pytz  # timezone
import uuid  # random UUID String


def filename_generator():
    todays = datetime.now(pytz.timezone('Asia/Manila')).utcnow()
    utime = f'{uuid.uuid1()}{todays.hour}{todays.minute}{todays.second}'

    deduct = -2 if str(todays.year)[1] == '0' else -3
    udate = f"{str(todays.year)[deduct:]}{todays.month}{todays.day}"
    return f"{udate}{utime}"


print(filename_generator())
