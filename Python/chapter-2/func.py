import random
import sys

random.seed()

def bnsc_gen_case_bigrange(num_ele, min_ele, max_ele):
    rs = set()
    while len(rs) < num_ele:
        rs.add(random.randint(min_ele, max_ele))
    s = sorted(list(rs))
    return random.choice(s), s


def bnsc_gen_case_smallrange(num_ele, min_ele, max_ele):
    s = sorted(random.sample(list(range(min_ele, max_ele+1)),
                             num_ele))
    return random.choice(s), s

def bnsc_rand_case_bigrange(num_ele):
    rmax = sys.maxsize
    rmin = -rmax - 1
    return bnsc_gen_case_bigrange(num_ele, rmin, rmax)

e, a = bnsc_rand_case_bigrange(12)

print(e)
print(a)
