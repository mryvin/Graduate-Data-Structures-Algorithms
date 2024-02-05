from random import shuffle, randint
import sys

def arrange(jars, lids):
    """
    This method cannot compare any lid to any other lid and cannot 
    compare any jar to any other jar.
    The mehod can compare a jar to a lid an vice versa.
    For example, jar[i] < jar[j] is not allowed but jar[i] < lid[j] is allowed
    """
    pass

jars = list({randint(0, sys.maxsize) for i in range(15)})
lids = list(jars)

shuffle(jars)
shuffle(lids)

print(lids)
print(jars)

arrange(jars, lids)

print(jars == lids)
