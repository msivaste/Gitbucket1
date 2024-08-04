s_username = "EMC"
s_password = "123"

u_name = input()
pwd = input()

def val():
    if (u_name == s_username) and (pwd==s_password):
        return "Validation success"
    else:
        return "Validation failed"

val_status = val()
print(val_status)
