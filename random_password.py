import random
import string


user_choice = int(input("What should be the password length? :"))
def generate_password(a):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(a))
    return password

password = generate_password(user_choice)
print(f"Generated password : {password}")