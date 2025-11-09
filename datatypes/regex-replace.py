import re
text = "my name is seema sharma"
pattern = r"sharma"
rep = "bhargav"
change = re.sub(pattern, rep, text)
print(change)
