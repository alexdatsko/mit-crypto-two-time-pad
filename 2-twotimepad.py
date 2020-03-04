ciphertext1=[0xe9,0x3a,0xe9,0xc5,0xfc,0x73,0x55,0xd5]
ciphertext2=[0xf4,0x3a,0xfe,0xc7,0xe1,0x68,0x4a,0xdf]
key=[0,0,0,0,0,0,0,0]
message1=[0,0,0,0,0,0,0,0]
message2=[0,0,0,0,0,0,0,0]

f=open('word8.txt','r')
f2=open('poss.txt','a')

def alpha(ch):
  #ch=ord(c)
  if (ch>64 and ch<91) or (ch>96 and ch<123):
    return 1
  else:
    return 0

for c in range(len(ciphertext1)):
  key[c]=ciphertext1[c]^ciphertext2[c]

print("key: ",key)
for c in range(len(ciphertext1)):
  print(chr(key[c]),end='')
print()

print("message1: ")
word=f.readline()
while word:
  string1=''
  badword=0
  for c in range(len(message1)):
    message1[c]=ord(word[c])^key[c]
    if not (alpha(message1[c])):
      badword=1
      break
    string1+=chr(message1[c])
  if not badword:
    print(string1)
    f2.write(string1+"\n")
  word=f.readline()

print("message2: ")
for c in range(len(ciphertext2)):
  message2[c]=ciphertext2[c]^key[c]
  print(chr(message2[c]),end='')
print()


