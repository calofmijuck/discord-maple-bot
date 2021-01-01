import sys, os
sys.path.append(os.pardir)

from impl.exp_const import REQUIRED_EXP, CUMULATIVE_EXP

MAX_LEVEL = 300

def test_cumulative_exp():
    for i in range(MAX_LEVEL - 1):
        if REQUIRED_EXP[i] + CUMULATIVE_EXP[i] != CUMULATIVE_EXP[i + 1]:
            print("Cumulative EXP is not correct at level {}".format(i))
            return
    print("Cumulative EXP check passed")

test_cumulative_exp()
