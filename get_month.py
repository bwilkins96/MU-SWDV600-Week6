# Function that returns the month based on a corresponding number
# i.e. get_month(1) = 'January'

def get_month(month_int):
    months = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August', 'September',
        'October', 'November', 'December'
    ]

    return months[month_int-1]

if __name__ == '__main__':
    for i in range(1, 13):
        print(get_month(i))