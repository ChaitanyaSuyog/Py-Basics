
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not is_tall:
    print("You are a short male.")
elif not is_male and is_tall:
    print("You are tall, but not male.")
else:
    print("You are short and not a male.")
