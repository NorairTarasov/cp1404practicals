import random

print(dir(random))
# this gives:
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI',
# '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst',
# '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom',
# '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate',
# 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed',
# 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print(random.randint(5, 20))  # line 1
# line 1 gives results from 5 to 20 inclusive
# smallest number 5
# largest number 20

print(random.randrange(3, 10, 2))  # line 2
# line 2 gives results from 3 to 10, but only odd numbers
# smallest number 3
# largest number 9

print(random.uniform(2.5, 5.5))  # line 3
# line 3 gives results from 2.5 to 5.5 inclusive, the number goes to 1 over Quadrillion decimals, (0.000000000000001)
# smallest number: 2.5
# largest number: 5.5

print(random.randint(1, 100))
# line 4 gives results from 1 to 100 inclusive
# smallest number: 1
# largest number: 100
