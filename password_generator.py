import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9']
symbols = ['#','$','%','&','*','+','(',')','^','!','_','#','$','%','&','*','+','(',')','^','!','_','#','$','%','&','*','+','(',')','^','!','_']

print("Welcome to the Password Generator")
n_letters = int(input("Enter the number of letters do you want in your password: "))
n_numbers = int(input("Enter the number of numbers do you want in your password: "))
n_symbols = int(input("Enter the number of symbols do you want in your password: "))

l = random.sample(letters, n_letters)
n = random.sample(numbers, n_numbers)
s = random.sample(symbols, n_symbols)
final = l + n + s

random.shuffle(final)

final_pw = "".join(final)
print(f"\n Your generated password is: {final_pw}")