import re 
text = "hi song my name is song and i love Song and my name is vishal is very And good bowler and batter"
pattern = r"and"
search = re.findall(pattern, text, re.IGNORECASE)
if search:
    print(search)
    print(len(search))
else:
    print("not found")
