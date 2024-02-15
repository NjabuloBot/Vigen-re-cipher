text = input()
custom_key = 'python'

def vigenere(message,key):
   key_index = 0
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   encrypted_text = ''
   
   for char in message.lower():
      #Append space to the message
      if char == ' ':
         encrypted_text+=char
      else:
         key_char = key[key_index % len(key)]
         index = alphabet.find(char)