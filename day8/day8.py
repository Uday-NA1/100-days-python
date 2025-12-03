def greet_with(name, location):
    print(f"Hello {name} from {location}")
greet_with("Uday", "Chennai") # Positional - in order of how the function defines it
greet_with(location="Chennai", name="Uday") # Uses keyword for each argument, can be in any order.

art = '''
        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88    

'''

print(art)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output = ""

    if encode_or_decode == 'decode':
                shift_amount *= -1

    for char in original_text:

        if char not in alphabet:
            output_text += char
        else:
            new_pos = alphabet.index(char) + shift_amount
            new_pos %= len(alphabet)
            output += alphabet[new_pos]
    
    print(f"Here is the {encode_or_decode} result: {output}")

    keepgoing = input("Do you want to continue the program? (y/n)").lower()
    if keepgoing == 'n':
        flag = True

flag = False
while not flag:
    direction = input("Type 'encode' if you want to encrypt, type 'decode' if you want to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    ceaser(text, shift, direction)