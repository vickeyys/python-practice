# in this it will split the word according to the loction like [0] means arn [1] means aws and so on this will split by : and then we will filter the username jhon by [-1] it means last word after last :
arn = "arn:aws:iam::123456789012:user/John"
sp = arn.split(':')[0]
sp2 = arn.split(':')[1]
sp3 = arn.split(':')[2]
user = arn.split(':')[-1]
username = arn.split('/')[-1]
print(user)
print(sp)
print(sp2)
print(sp3)

