# Function that returns the month based on a corresponding abbreviation
# i.e. get_month('jan') = 'January'

def get_month(abbr):
    months = {
        'jan': 'January', 'feb': 'February', 'mar': 'March',
        'apr': 'April', 'may': 'May', 'jun': 'June', 'jul': 'July',
        'aug': 'August', 'sep': 'September', 'oct': 'October',
        'nov': 'November', 'dec': 'December'
    }

    return months[abbr.lower()]

if __name__ == '__main__':
    print(get_month('NOV'))