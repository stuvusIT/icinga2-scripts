# Common parts for all Python checks.
#
# Import this file at the beginning of your check with:
#   `from common import doCheck`.
# Then, call doCheck where the only parameter is the function
# to execute in order to execute the check.
# The function must take a dict as parameter where you have to set
# the 'name' attribute.
# You can set the following attributes:
#
# name:
#     Name of your check
#
# state:
#     One of OK, WARNING, CRITICAL, or UNKNOWN
#
# output:
#     Short output of the check
#
# perfdata:
#     Performance data (see below)
#
# details:
#     Detailed output
#
# Syntax for perfdata:
#
# Multiple perfdata values are space-separated.
# warn, crit, min or max may be null. Trailing unfilled
# semicolons can be dropped
#
# label=value[UOM];[warn];[crit];[min];[max]
#
# label: Label of this perfdata. Use single quotes to use spaces.
#        Use two single quotes to specify a single quote in the string
# uom:   Unit of measure (optional; one of s (seconds), % (percentage),
#        B (bytes; also KB, MB, TB), c (continous counter)
# value: Value of this perfdata
# warn:  Warning value of this perfdata
# crit:  Critical value of this perfdata
# min:   Minimum value of this perfdata
# max:   Maxmimum value of this perfdata

import sys
import traceback

defaultCheckReturn = {
    'state': 'OK',
    'output': 'OK',
    'perfdata': '',
    'details': ''
}


def doCheck(checkFunc):
    # Use default values
    ret = defaultCheckReturn.copy()

    try:
        checkFunc(ret)
    except Exception as e:
        ret['state'] = 'UNKNOWN'
        ret['output'] = 'Python exception occured'
        ret['perfdata'] = ''
        ret['details'] = ''.join(traceback.format_exception(etype=type(e),
                                 value=e, tb=e.__traceback__))

    # Require name
    if 'name' not in ret:
        print('Internal error: No check name given')
        sys.exit(3)

    # Handle perfdata
    if ret['perfdata'] != '':
        ret['perfdata'] = ' | ' + ret['perfdata']

    # Print
    print(ret['name'] + ' ' + ret['state'] + ': ' +
          ret['output'] + ret['perfdata'])
    if ret['details'] != '':
        print(str(ret['details']).replace('|', ''))

    # Exit
    if ret['state'] == 'OK':
        sys.exit(0)
    elif ret['state'] == 'WARNING':
        sys.exit(1)
    elif ret['state'] == 'CRITICAL':
        sys.exit(2)
    else:
        exit(3)
