# mengganti email lama dengan email baru

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    print(f"return ke-1 yg dieksekusi")
    return new_email
  print(f"return ke-2 yg dieksekusi")
  return email
print(replace_domain("myemail@gmail.com", "gmail.com", "yosiro.com"))