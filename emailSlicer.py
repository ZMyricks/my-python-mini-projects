

def email_slicing(email):
    email = email.strip()
    username = email[:email.index("@")]
    domainname = email[email.index("@")+1:]
    format_ =(f"Your username is '{username}' and your domain name is '{domainname}'")
    print(format_)

email_slicing("lolafalooa.patola@itsalovelyday.com")
