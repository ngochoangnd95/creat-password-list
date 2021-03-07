import datetime
import re


def generate_birth_date(end_date_string=None, format_='DDMMYYYY'):
    """
    Generate list of birth date.
    :param end_date_string: dateString of the end date.
    :param format_: format string. Default is 'DDMMYYYY'.
    """
    end_date = datetime.date.today()
    if end_date_string is not None:
        end_date = datetime.date.fromisoformat(end_date_string)

    is_trimming_day = False
    is_trimming_month = False
    is_trimming_year = False
    if not re.search('^D{2}M*', format_):
        is_trimming_day = True
    if re.search('DMYY*', format_):
        is_trimming_month = True
    if re.search('MYY$', format_):
        is_trimming_year = True

    with open('birth_date.txt', 'w') as file:
        date = datetime.date(1950, 1, 1)
        day_delta = datetime.timedelta(days=1)
        while date <= end_date:
            if is_trimming_day:
                date_as_string = str(date.day)
            else:
                date_as_string = date.strftime('%d')
            if is_trimming_month:
                date_as_string += str(date.month)
            else:
                date_as_string += date.strftime('%m')
            if is_trimming_year:
                date_as_string += date.strftime('%y')
            else:
                date_as_string += date.strftime('%Y')
            file.write(date_as_string + '\n')
            date += day_delta


if __name__ == "__main__":
    generate_birth_date()
