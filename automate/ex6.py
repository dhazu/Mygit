"""22. How would you write a regex that matches a sentence where the first
word is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive. It must match the
following:
    • 'Alice eats apples.'
    • 'Bob pets cats.'
    • 'Carol throws baseballs.'
    • 'Alice throws Apples.'
    • 'BOB EATS CATS.'
    but not the following:
    • 'RoboCop eats apples.'
    • 'ALICE THROWS FOOTBALLS.'
    • 'Carol eats 7 cats.'
"""

# Solution:
import re

nameregex = re.compile(r'''(
        (Alice|Bob|Carol)
        (\s)
        (eats|pets|throws)
        (\s)
        (apples|cats|baseballs))
        ''', re.VERBOSE|re.I)

name = input("Enter the names: ")
mo = nameregex.search(name)
print(mo.group())
