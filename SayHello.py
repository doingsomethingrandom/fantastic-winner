import random
age = random.randrange(0, 100)
fname = "Tharun"
lname = "Pandiyan"
fullName = f"{fname} {lname}"
greet = f"Hello {fullName}"
println(f"""{fname} is {age}-years-old.
His last name is {lname}.
He's {age}-year-old.
Say hello to him.
{greet}.""")
