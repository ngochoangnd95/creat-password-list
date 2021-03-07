import re


headers = [
    '086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039',
    '088', '091', '094', '081', '082', '083', '084', '085',
    '089', '090', '093', '070', '076', '077', '078', '079',
    '092', '056', '058'
]


def __validate(num_str):
    while num_str:
        count = num_str.count(num_str[0])
        if count > 4:
            return False
        elif count == 4:
            if re.search("%s{4}" % (num_str[0]), num_str):
                return False
        num_str = num_str.replace(num_str[0], '')
    return True


def generate_phone_number(is_all_headers_used=False):
    """
    Generate phone numbers.
    Rule:
    - There are at maximum 4 same digits.
    - There are at maximum 3 same digits joined.
    :return: None
    """
    with open('phone_number.txt', 'w') as file:
        for n in range(1011, 10 ** 7):
            num_str = str(n).rjust(7, '0')
            # 20 is an amount of the headers of Viettel and Vinaphone
            # It costs about 35 seconds to write numbers with one header
            max_range = 20
            if is_all_headers_used:
                max_range = len(headers)
            for i in range(max_range):
                if __validate(num_str):
                    file.write(headers[i] + num_str + '\n')


if __name__ == "__main__":
    generate_phone_number()
