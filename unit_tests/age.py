def get_age_category(age):
    if 0 <= age <= 9:
        return 'Child'
    elif 9 < age <= 18:
        return 'Adolescent'
    elif 18 < age <= 65:
        return 'Adult'
    elif 65 < age <= 150:
        return 'Golden Age'
    else:
        return f'Age not covered: {age}'