sentence=input("Enter a sentence/message: ")
word=input("enter the word to search: ")
characters=len(sentence)
start=0 
end =characters-1
while(start<characters and sentence[start]==" "):
    start=start+1
while(end>=0 and sentence[end]==" "):
    end =end-1
length=end-start+1
if(length<0):
    length=0
print("Original message: ",sentence)
print("total number of characters: ",characters)
print("length without leading and trailing spaces: ",length )
vowels=0
digits=0
spaces=0  
lowercase=sentence.lower()
lowercaseword=word.lower()
for char in lowercase:
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        vowels=vowels+1
    if(char>='0' and char<='9'):
        digits=digits+1
    if(char==" "):
        spaces=spaces+1

print("number of vowels: ",vowels)
print("number of digits: ",digits)
print("number of spaces: ",spaces)

if(lowercaseword in lowercase):
    print("word found")
else:
    print("word not found")
print("uppercase: ",sentence.upper())
print("lowercase: ",lowercase)