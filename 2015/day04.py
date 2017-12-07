import hashlib
import itertools

with open('day04.input') as f:
    input = str(f.read().rstrip())


def solve(secret, prefix):
    # start counting from 1 to infinity, friend
    for i in itertools.count(1):
        hash =  hashlib.md5((secret + str(i)).encode()).hexdigest()

        # if we have the proper prefix (preceeding zeroes), we're done!
        if hash[:len(prefix)] == prefix:
            return i

print(solve(input, '00000'))
print(solve(input, '000000'))
