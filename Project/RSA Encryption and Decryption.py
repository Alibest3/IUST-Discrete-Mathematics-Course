option = input("do you want to encrypt word or decrypt a number? (1 for encrypt, 2 for decrypt): ")
# first you must choose encryption or decryption
if option == "1":
    word = input("Please Enter You Word: ")
    word = word.lower()
    
elif option == "2":
    entered_number = input("Please Enter Your Number: ")
    encrypted_numbers_list = []
    counter = 0
    s = ""
    for digit in entered_number:
        s += digit
        counter += 1
        if counter % 2 == 0:
            encrypted_numbers_list.append(s)
            s = ""
    if len(entered_number)% 2 != 0:
        encrypted_numbers_list.append(entered_number[-1])

    for i in range(len(encrypted_numbers_list)):   #change type of numbers in list to integers
        if encrypted_numbers_list[i][0] == "0":
            encrypted_numbers_list[i] = int(encrypted_numbers_list[i][1:])
        else:
            encrypted_numbers_list[i] = int(encrypted_numbers_list[i])
    
letters_dict = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,
                "s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

key_list = list(letters_dict.keys())
val_list = list(letters_dict.values())
n = 115
k = 7
encrypted_letters_list = []
result_list = []

    

def encrypt_word(word):
    global m,new_m
    for letter in word:
        
        m = letters_dict[letter]  
        new_m = (m*k)%n
        encrypted_letters_list.append(new_m)
    result_list.extend(*[encrypted_letters_list])

    encrypted_number = ""
    for number in result_list:
        if number == 1:
            number = "01"
            encrypted_number += number
            
        elif number == 2:
            number = "02"
            encrypted_number += number
            
        elif number == 3:
            number = "03"
            encrypted_number += number
            
        elif number == 4:
            number = "04"
            encrypted_number += number
            
        elif number == 5:
            number = "05"
            encrypted_number += number
            
        elif number == 6:
            number = "06"
            encrypted_number += number
            
        elif number == 7:
            number = "07"
            encrypted_number += number
            
        elif number == 8:
            number = "08"
            encrypted_number += number
            
        elif number == 9:
            number = "09"
            encrypted_number += number
            
            
        else:
            number = str(number)
            encrypted_number += number
            
            
    return encrypted_number,encrypted_letters_list
        


def decrypt_word(encrypted_numbers_list):
    encrypted_word = "" 
    for number in encrypted_numbers_list:
        inverse_new_m = pow(number,-1,115) #calculates multiplicative inverse modulo of m
                                            #if it doesn't have an inverse modulo, and error raise
        m = pow(inverse_new_m *k,-1,115)
        encrypted_word += key_list[m-1]
        
    return encrypted_word

if option == "1":
    print(f"Encrypted word : {encrypt_word(word)}")

elif option == "2":
    print(f"Decrypted word : {decrypt_word(encrypted_numbers_list)}")
