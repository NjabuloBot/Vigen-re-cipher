text = input()
custom_key = 'python'

def vigenere(message,key):
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   encrypted_text = ''
   
   for char in message.lower():
      if char == ' ':
         encrypted_text+=char
      else:
         index = alphabet.find(char)