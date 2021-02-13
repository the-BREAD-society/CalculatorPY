"""
# :author: nukestye, exdoth
# :version: 0.20
# :description: A command-line interface calculator made solely of python.
# :license:
CalculatorPY  Copyright (C) 2021  nukestye, exdoth
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
"""

# Import
import operation
import util

inpt = input("Input your calculation: ")  # input: 1 / 2 * 3 + 4 - 5

operations = util.operationsFrom(inpt)
calculations = util.toList(inpt)

util.checksum(inpt)
operation.check(operations, calculations)
# 1 / 2 + 3 - 5 * 3 = -11.5
