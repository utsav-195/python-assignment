readInputFile = open("input.txt", "r")
s = ""
s = readInputFile.read().lower()
readInputFile.close()
# print(type(s))
listWords = s.split(" ")
listWords=set(listWords)
print(listWords)
# separatedWords=set(s)
# print(separatedWords)
print(sorted(listWords))
listWords = sorted(listWords)
for i in range(0, len(listWords)):
    listWords[i] = "".join(letter for letter in listWords[i] if letter.isalnum())
print(listWords)
readInputFile = open("input.txt", "r")
st = ""
st = readInputFile.read().lower()
readInputFile.close()
r = st.count("hi")
outputFile = open("output.txt", "w+")
for i in listWords:
    outputFile.write(i + " " + str(st.count(i)))
    print(i + " " + str(st.count(i)))
