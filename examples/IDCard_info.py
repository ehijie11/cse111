
first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
email_address = input("Input your email address: ")
phone_number = input("Input your phone number: ")
job_title = input("Input your job title: ")
id_number = input("Input your ID number: ")

output = f" {last_name.upper()} {first_name.capitalize()} \n {job_title.capitalize()} \n ID: {id_number} \n\n {email_address.lower()} \n {phone_number}"

print("Your ID is ")
print("------------------------------------------------------------")
print(output)
print("------------------------------------------------------------")