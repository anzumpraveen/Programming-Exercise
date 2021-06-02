d={"one":1,"two":2,"three":3,"four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0","fifty":"50"}
user=input("enter alphanumaric")
for ele in user.split():
    res=" ".join(d[ele])
    print(res)


from word2number import w2n
print(w2n.word_to_num("six six"))
