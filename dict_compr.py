# dictionary comprihension

# square = {1:1, 2:4, 3:9}

# square = { f" square of {num} " :num**2 for num in range(1,11)}
# for k,n in square.items() :
#     print(f"{k}:{n}")

# def word_count(s):
#     return {char:s.count(char) for char in s}

# print(word_count("arun solanki"))

odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11) }
print(odd_even)