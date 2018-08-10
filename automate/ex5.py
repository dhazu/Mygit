"""21. How would you write a regex that matches the full name of someone
whose last name is Nakamoto? You can assume that the first name that
comes before it will always be one word that begins with a capital letter.
The regex must match the following:
    • 'Satoshi Nakamoto'
    • 'Alice Nakamoto'
    • 'RoboCop Nakamoto'
    but not the following:
    • 'satoshi Nakamoto' (where the first name is not capitalized)
    • 'Mr. Nakamoto' (where the preceding word has a nonletter character)
    • 'Nakamoto' (which has no first name)
    • 'Satoshi nakamoto' (where Nakamoto is not capitalized)"""

## Solution:
import re
nameregex = re.compile(r'([A-Z]\w+\sNakamoto)')
mo = nameregex.findall("""His name is alice Nakamoto or his name is RoboCop Nakamoto, 
his name is Satoshi Nakamoto, His name is Mr. Nakamoto
satoshi Nakamoto, Nakamoto, Satoshi nakamoto""")
for names in mo:
    print(names)
