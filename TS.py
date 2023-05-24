import csv

def generate_wordlist():
    with open(r"C:\Users\Sutton\OneDrive - Maggie L Walker High School\UNIV Mentorship\School Password\us-cities.csv") as csvfile:
        data = list(csv.reader(csvfile, delimiter="\n"))

    sep = ','
    stripped_city_names = []
    wordlist = []
    symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]

    for line in data:
        first_stripped_line = str(line).split(sep, 1)[0]
        second_stripped_line = first_stripped_line[2:]
        final_stripped_line = second_stripped_line.replace(" ", "")
        stripped_city_names.append(final_stripped_line)

    textfile = open(r"C:\Users\Sutton\OneDrive - Maggie L Walker High School\UNIV Mentorship\School Password\mlwgspasswordlist.txt", "a")

    for city in stripped_city_names:
        for symbol in symbol_list:
            pass_string = city + symbol
            wordlist.append(pass_string)                
            textfile.write(pass_string + "\n")
    print(wordlist)

generate_wordlist()
                

                