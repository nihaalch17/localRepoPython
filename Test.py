Original = "Hello World"
S = list(Original)
i = 0
j = len(S)-1

while(i<j):
    temp = S[i]
    S[i] = S[j]
    S[j] = temp
    i+=1
    j-=1

print("Original String: " + Original)
print("Reversed String: " + "".join(S))
print("Code ran successfully!!")
print("One more changes")