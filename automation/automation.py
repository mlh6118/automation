import re

def emails_and_phone_numbers():
    file_existing_contacts = open(r"../assets/existing-contacts.txt", "r")
    textfile_potential_contacts = open(r"../assets/potential-contacts.txt", "r")
    file_phone_numbers = open(r"phone_numbers.txt", "w")
    file_emails = open(r"emails.txt", "w")

    find_potential_contacts = textfile_potential_contacts.read()
    pattern = r"[\"+\"]?[0-9]*?[\s]?[\"\-\"|\".\"]?[\"(\"]?[0-9]*?[\s]?[" \
        r"\")\"|\"\-\"|or\".\"]?[0-9]{3}[\"\-\"|\".\"][0-9]{4}[\"E\"]?[" \
        r"\"x\"]?[\"t\"]?[0-9]*"
    match = re.findall(pattern, find_potential_contacts)
    print(match)

    for number in match:
        file_phone_numbers.write(number)


    file_phone_numbers.close()
    file_emails.close()
    textfile_potential_contacts.close()
    file_existing_contacts.close()


if __name__ == "__main__":
    emails_and_phone_numbers()