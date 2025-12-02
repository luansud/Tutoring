LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def main():
    password = ""
    while(password != "q" and password != "Q"):
        password = input("Enter your password (or 'q' to quit): ")
        print(f"Password Strength Score: {password_strength(password)}\n")

def word_in_file(word, filename,case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if case_sensitive == False:
                if word.lower() == line.lower().strip():
                    return True
            if case_sensitive == True:
                if word == line.strip():
                    return True

def word_has_character(word,character_list):
    for character in word:
        if character in character_list:
            return True

def word_complexity(word):
    complexity_score = 1
    if word_has_character(word,LOWER):
        complexity_score += 1
    if word_has_character(word,UPPER):
        complexity_score += 1
    if word_has_character(word,DIGITS):
        complexity_score += 1
    if word_has_character(word,SPECIAL):
        complexity_score += 1
    return complexity_score

def password_strength(password,min_length=10,strong_length=16):
    # check dictionary
    if word_in_file(password,"wordlist.txt",False):
        print("Password is a dictionary word and is not secure.")
        return 0
    # check known-passwords
    elif word_in_file(password,"toppasswords.txt",True):
        print("Password is a commonly used password and is not secure.")
        return 0
    # check length
    elif len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password")
        return 5 
    # check complexity
    else: return word_complexity(password)
    
if __name__ == "__main__":
    main()