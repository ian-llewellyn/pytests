def utc_start_end(input_date):
    """
    utc_start_end()
    Pass in a local date to this function and it will return a tuple with the
    UTC start and end times that correspond to that date.
    """
    import datetime
    from time import gmtime, mktime

    # Convert the input to naive start and end datetimes (local time)
    start = datetime.datetime.strptime(input_date, '%Y-%m-%d')
    end = start + datetime.timedelta(days=1)

    # Convert to aware UTC
    start = gmtime(mktime((start.year, start.month, start.day,
        start.hour, start.minute, start.second, start.microsecond,
        0, -1)))

    end = gmtime(mktime((end.year, end.month, end.day,
        end.hour, end.minute, end.second, end.microsecond,
        0, -1)))

    # Convert to naive UTC
    start = datetime.datetime(start.tm_year, start.tm_mon, start.tm_mday,
        start.tm_hour, start.tm_min, start.tm_sec)

    end = datetime.datetime(end.tm_year, end.tm_mon, end.tm_mday,
        end.tm_hour, end.tm_min, end.tm_sec)

    return (start, end)

# Case 1: Pass a naive date in as a string 'YYYY-mm-dd' during GMT
#         Return a tuple with aware start and end datetimes of the date in UTC.
case_1 = '2013-02-12'

# Case 2: Pass a naive date in as a string 'YYYY-mm-dd' during IST
#         Return a tuple with aware start and end datetimes of the date in UTC.
case_2 = '2013-06-21'

# Case 3: The spring equinox should have 23 hours.
case_3 = '2013-03-31'

# Case 4: The autumn time change should have 25 hours.
case_4 = '2013-10-27'

for input_date in [case_1, case_2, case_3, case_4]:
    print input_date, ': ', [str(i) for i in utc_start_end(input_date)]
