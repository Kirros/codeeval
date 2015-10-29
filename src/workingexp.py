import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def process_date(date):
    return int(date[4:8]) * 12 + months.index(date[:3])


def bound(number, bottom_bound, top_bound):
    return max(bottom_bound, min(top_bound, number))


def process_intervals(intervals):
    number_of_months = 0
    for i in range(len(intervals)):
        (start, end) = intervals[i]
        interval = [1] * (end - start + 1)
        for other in intervals[i+1:]:
            (other_start, other_end) = other
            interval_start = bound(other_start - start, 0, len(interval))
            interval_end = bound(other_end - start + 1, 0, len(interval))
            for month in range(interval_start, interval_end):
                interval[month] = 0
        number_of_months += sum(interval)
    return number_of_months

for test in test_cases:
    ranges = map(lambda x: tuple(x.strip().split('-')), test.strip().split(';'))
    ranges = list(map(lambda x: (process_date(x[0]), process_date(x[1])), ranges))
    print(process_intervals(ranges) // 12)

test_cases.close()
