# re module means regular expression
import re 
text = "hi song my name is song and i love Song and my name is vishal is very and good bowler and batter"
pattern = r"lnd"
search = re.search(pattern, text, re.IGNORECASE)
if search:
    print(search.group())
else:
    print("not found")
