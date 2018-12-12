# Common parts for all bash checks.
#
# Source this file at the beginning of your check with a relative path.
# Set `checkName` to the name of your check.
# Set `checkState`, `checkOutput`, `checkPerfdata`, and `checkDetails` according to your
# result and call `checkReturn`, which will exit using the proper code.
#
# checkName:
#     Name of your check
#
# checkState:
#     One of OK, WARNING, CRITICAL, or UNKNOWN
#
# checkOutput:
#     Short output of the check
#
# checkPerfdata:
#     Performance data (see below)
#
# checkDetails:
#     Detailed output
#
# Syntax for perfdata:
#
# Multiple perfdata values are space-separated.
# warn, crit, min or max may be null. Trailing unfilled semicolons can be dropped
#
# label=value[UOM];[warn];[crit];[min];[max]
#
# label: Label of this perfdata. Use single quotes to use spaces. Use two single quotes to specify a single quote in the string
# uom:   Unit of measure (optional; one of s (seconds), % (percentage), B (bytes; also KB, MB, TB), c (continous counter)
# value: Value of this perfdata
# warn:  Warning value of this perfdata
# crit:  Critical value of this perfdata
# min:   Minimum value of this perfdata
# max:   Maxmimum value of this perfdata

set -e
set -o nounset
set -o pipefail

checkState=OK
checkOutput=OK
checkPerfdata=
checkDetails=

checkReturn() {
	if [ -n "${checkPerfdata}" ]; then
		checkPerfdata=" | ${checkPerfdata}"
	fi
	
	echo "${checkName} ${checkState}: ${checkOutput}${checkPerfdata}"
	[ -n "${checkDetails}" ] && echo "${checkDetails}" | tr -d '|'

	case "${checkState}" in
		OK)
			exit 0
			;;
		WARNING)
			exit 1
			;;
		CRITICAL)
			exit 2
			;;
		*)
			exit 3
			;;
	esac
}
