def to_minutes(value):
    hours, minutes = value.split(":")
    return int(hours) * 60 + int(minutes)
