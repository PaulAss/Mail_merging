text=open("letter.txt","w")
text.write('''Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Paul
''')
text.close()

file=open("invited_names.txt","w")
file.write('''Pete
Bee
Lee
kath
Pam
Sue
Zara
Joe
Kath
Amma
 ''')
file.close()
PLACEHOLDER = "[name]"

file = open("invited_names.txt","r")
names =file.readlines()
file.close()
print(names)

file = open("letter.txt","r")
letter = file.read()
for name in names:
  strip_name=name.strip()
  #print(strip_name)
  new_letter = letter.replace(PLACEHOLDER ,strip_name)
  print(new_letter)
