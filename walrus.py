# New in Python 8.1 
# assignment expression also known as walrus operator
# :=
# var := expr
# it is a way to evaluate an expression and assign it to a variable in the same statement.
# use the walrus operator always in the context of an expression
# rather than as a stand alone statement

walrus = False
print(walrus)

print(walrus := True)
print(walrus)

#### this can be useful to simplify your code. ####
# without walrus
inputs = list()
while True:
    current = input("Write something ('quit' to stop): ")
    if current == "quit":
        break
    inputs.append(current)

print(inputs)
# with walrus
inputs = list()
while (current := input("Write something ('quit' to stop): ")) != "quit":
    inputs.append(current)
print(inputs)

#### useful for list comprehension and api requests ####
#### e.g. we have to wait for data repeatedly and then want to
#### filter it with list comprehension

# simulate api request
import random
def get_score_data():
    return random.randrange(1, 10)

# without walrus
scores = [get_score_data() for _ in range(20)]
scores = [score for score in scores if score >= 5]
print(scores)

# with walrus
scores = [score for _ in range(20) if (score := get_score_data()) >= 5]
print(scores)
