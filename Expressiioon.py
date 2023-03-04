import re
text = "phone number is 408,555,1234."
'phone' in text
pattern = 'phone'
print(re.search(pattern, text))
