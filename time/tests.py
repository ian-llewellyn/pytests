import unittest

def naive_iso_to_utc(in_iso):
    """iso2utc
    Convert a naive ISO 8601 timespec into UTC ready for entry into a database
    """
    from time import gmtime, mktime

    in_date, in_time = list(in_iso.split('T'))
    # You could say there's a BUG here - what if there's no time?
    in_year, in_month, in_day = list(in_date.split('-'))
    # Again, the ISO spec doesn't say there has to be any more than a date
    in_hour, in_minute, in_second = list(in_time.split(':'))
    # If there are microseconds, they should be taken care of

    in_year = int(in_year)
    in_month = int(in_month)
    in_day = int(in_day)
    in_hour = int(in_hour)
    in_minute = int(in_minute)
    in_second = int(in_second)
    in_microsecond = 0

    return gmtime(mktime((in_year, in_month, in_day,
        in_hour, in_minute, in_second, in_microsecond, 0, -1)))

def utc_to_local(utc, aware=True):
    """utc_to_local(utc) => datetime.datetime
    Convert an aware UTC time to an aware local time.
    """
    pass

def local_to_utc(local, aware=None):
    """local_to_utc(local) => datetime.datetime
    Convert a naive local datetime to an aware datetime.
    """
    pass

class TestTimes(unittest.TestCase):
    import time
    utc_time = time.gmtime()
    local_time = time.localtime()
    naive_iso_local_time = '2013-06-01T12:00:00'
    '2013-12-01 12:00:00'
    '2013-12-01 12:00:00'
    # Test during the summer
    '2013-06-01 12:00:00'
    '2013-06-01 13:00:00'

    def test_naive_iso_to_utc(self):
        self.assertEqual(naive_iso_to_utc('2013-06-01T12:00:00'),
            )

    def test_utc_to_local(self):
        # Test now!
        self.assertEqual(utc_to_local(time.gmtime()), time.localtime())
        # Test during the winter
        self.assertEqual('2013-12-01 12:00:00', '2013-12-01 12:00:00')
        # Test during the summer
        self.assertEqual('2013-06-01 12:00:00', '2013-06-01 13:00:00')

    def test_local_to_utc(self):
        # Test now!
        self.assertEqual(local_to_utc(time.localtime()), time.gmtime())
        # Test during the winter
        self.assertEqual('2013-12-01 12:00:00', '2013-12-01 12:00:00')
        # Test during the summer
        self.assertEqual('2013-06-01 13:00:00', '2013-06-01 12:00:00')
