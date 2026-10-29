import re

text = """
My address is in Pune, Maharashtra, PIN code 411001.
Another PIN code is 400001, and another is 110001.
The number 12345 is not a valid PIN code.
"""

pattern = r'\b[1-9][0-9]{5}\b'

pin_codes = re.findall(pattern, text)

print("Extracted Indian PIN Codes:")
for pin in pin_codes:
    print(pin)
    