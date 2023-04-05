# Definindo a string
string = "exemplo"

# Invertendo os caracteres
inverted_string = ""
for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

# Imprimindo a string invertida
print(inverted_string)