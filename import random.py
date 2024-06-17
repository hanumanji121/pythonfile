import random
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ,abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="!@#$%^&*()_+{}[]?/|'';:<>,."
characters=alphabets+numbers+symbols
length=int(input("enter the length your password for your password"))
password=''.join(random.sample(characters,length))
print("the password is:",password)
