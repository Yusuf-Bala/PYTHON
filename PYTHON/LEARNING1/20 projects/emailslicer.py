# collect email from user
# slice the email from the @ and ., the first part will be the username, then the second part eill be the domain, and then the third part is the extension 

def main():
    print("welcome to the email splitter")
    print()

    email_input = input("WHATS YOUR EMAIL? : ")
    [username , domain] = email_input.split("@")
    [domain, extension] = domain.split(".")

    print(f"USERNAME : {username}")
    print(f"DOMAIN : {domain}")
    print(f"EXTENSION : {extension}")

while True:
    main()