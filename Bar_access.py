legal_age = 18
password = "ok"
print("İf you want to enter the bar you should in your 18.")
ok_not = (input("İf you are ready write ok:"))


if ok_not == password:
    print("Let's go")
else:
    print("bye *_*")
    exit()

print("Guardian:")
user_age = int(input("-What's your age? : "))
if user_age >= legal_age:
    print("You can pass bro!")
else:
    print("you can't pass bro :(")
