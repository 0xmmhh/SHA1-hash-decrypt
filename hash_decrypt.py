import ssl
from urllib.request import urlopen, hashlib

#I disabled SSL certificate verification because I couldn't reach the password files
#It is not recommended for production

context = ssl._create_unverified_context()

hash_sha1 = input("Please type in a hash to decrypt: ") #take the hash from the user

list_of_passwords = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt", context=context).read(), "utf-8")
for guess in list_of_passwords.split("\n"):
    guess_hash = hashlib.sha1(bytes(guess, "utf-8")).hexdigest()

    if guess_hash == hash_sha1: #checks if its true
        print(f"Password for {hash_sha1} is {str(guess)}")
        quit()
    elif guess_hash != hash_sha1:
        print(f"The guess {str(guess)} doesn't match, trying another one...")
print("Password not in the database")
