text = input()
shift = 3

def vigenere(message,key):
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   encrypted_text = ''
   
   for char in message.lower():
      if char == ' ':
         encrypted_text+=char
      