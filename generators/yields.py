def generator():
    print(1)
    yield "Alisson"
    # The line below will be executed only
    # after the first yield is executed
    print(2)
    yield "Lima"
    print(3)

    # With yield from I'm saying:
    # Apeend the results of the next generator to the end of the results
    # created in this generator
    yield from generator()

gen = generator()

r = next(gen)
print(r)
# 1
# Alisson

r = next(gen)
print(r)
# 2
# Lima

# The next call will finish the generator function execution
# and then will start again because of the recursive call of the 
# last line of code in the function
r = next(gen)
print(r)
# 3 
# 1
# Alisson

# Print the values infinitelly because of the recursion
# i is used to break after some executions
i = 0
for r in generator():
    print (r)
    i = i + 1
    if (i == 10): 
        break;