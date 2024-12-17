import random
def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = "" 
    for j in range(pwlength):
        next_letter_index = random.randrange(len(alphabet))
        password += alphabet[next_letter_index]
    password = replaceWithNumber(password)
    password = replaceWithUppercaseLetter(password)
    return password
def replaceWithNumber(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword
def replaceWithUppercaseLetter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword
def main():
    print("Password length must be between 8 and 12.")
    length = int(input("Enter the length of the password: "))
    if length < 8:
        length = 8
        print("Length too short. Setting password length to 8.")
    elif length > 12:
        length = 12
        print("Length too long. Setting password length to 12.")
    password = generatePassword(length)
    print("Generated Password: " + password)
main()
