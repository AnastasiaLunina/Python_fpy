from pprint import pprint
import csv
import re

# Reading the phonebook in CSV format into the [] contacts_list

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Editing the phone numbers, formatting the records


def edit_phonebook(contacts_list):
    phone_pattern = r'(\+*)([7|8]*)([\s-]*)(\(?)([\s-]*)(\d{3})([\s-]*)(\)?)' \
                    r'([\s-]*)(\d{3})([\s-]*)(\d{2})([\s-]*)(\d{2})(\s?)([\s|(]*)' \
                    r'([доб.|\,])*(\s*)(\d*)([\s|)]*)'
    phone_pattern_edit = r'+7(\6)\10-\12-\14 доб.\19'

    formatted_phonebook = []
    for record in contacts_list:
        first_last_mid = ' '.join(record[:3]).split(' ')
        result = [first_last_mid[0], first_last_mid[1], first_last_mid[2], record[3], record[4],
                  re.sub(phone_pattern, phone_pattern_edit, record[5]), record[6]]
        formatted_phonebook.append(result)
    return get_unique_records(formatted_phonebook)


# Unite duplicated records

def get_unique_records(contacts_list):
    result_list = []

    for contact in contacts_list:
        first_name = contact[0]
        last_name = contact[1]
        for unique_contact in contacts_list:
            unique_first_name = unique_contact[0]
            unique_last_name = unique_contact[1]
            if first_name == unique_first_name and last_name == unique_last_name:
                if contact[2] == "":
                    contact[2] = unique_contact[2]

                if contact[3] == "":
                    contact[3] = unique_contact[3]

                if contact[4] == "":
                    contact[4] = unique_contact[4]

                if contact[5] == "":
                    contact[5] = unique_contact[5]

                if contact[6] == "":
                    contact[6] = unique_contact[6]

    for record in contacts_list:
        if record not in result_list:
            result_list.append(record)
    return result_list

# Write the phonebook in CSV format


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(edit_phonebook(contacts_list))



