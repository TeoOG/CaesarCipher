alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def caesar(mytext, myshift):
    
    cipher_list = []
    message = ""
    
    for char in mytext:
       
        if char.isalpha():

            char_index = alphabet.index(char) # Get the index 
        
            if direction == "encode":
                message = "encoded"
                             
                new_index = - len(alphabet) + char_index + (myshift % len(alphabet))
                            
            elif direction == "decode":
                message = "decoded"
                new_index = char_index - (myshift % len(alphabet))
                           
            # print(f"new_index is {new_index}")
            new_element = (alphabet[new_index])
            
            cipher_list.append(new_element)
        else:
            cipher_list.append(char)
    
    cipher_text = "".join(cipher_list)
    print(f"The {message} text is: {cipher_text}") 
    
go_again = True

while(go_again):
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    incorrect_order = True
    if not direction == "encode" and not direction == "decode":
        while incorrect_order:
            print("Type the correct order ")
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == "encode" or direction == "decode":
                incorrect_order = False

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(mytext=text, myshift=shift)

    repeat_decision = input("Do you want to go again? Type 'yes or 'no' ")
   
    if repeat_decision.lower() == "no":
        go_again = False
        print("Goodbye")
       
