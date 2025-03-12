# Module imports
import os
import zipfile

# Fetches zip and txt file names from folder
for file in os.listdir():
    if file.endswith(".zip"):
        zip_file = "./" + file
    if file.endswith(".txt"):
        txt_file = "./" + file

# Creates list of all possible passwords
with open(txt_file) as f:
    raw_passwords = f.read()

passwords = raw_passwords.split()

# Runs through zip files until flag is found
flag_not_found = True

while flag_not_found:
    flag_not_found = False

    # Tries all passwords until correct one for given zip file is found
    for password in passwords:
        try:
            with zipfile.ZipFile(zip_file) as zip_ref:
                zip_ref.extractall(pwd=bytes(password, 'utf-8'))
                zip_file = "./" + zip_ref.namelist()[0]
                flag_not_found = True

        # Breaks if not zipfile, meaning flag was found
        except zipfile.BadZipfile:
            break

        # Continues through passwords otherwise
        finally:
            continue

# Opens flag file
with open(zip_file) as f:
    print(f.read())