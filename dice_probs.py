import sys

import fire
import scipy.special
import numpy as np


def dice_probs_impl(n_dice, n_success, p_success):
    assert 0 < p_success < 1
    if n_dice < n_success:
        return 0
    else:
        n_choose_k = scipy.special.binom(n_dice, n_success)
        p = (
            n_choose_k
            * p_success ** n_success
            * (1 - p_success) ** (n_dice - n_success)
        )
        return p


def dice_probs(n_dice, min_n_success, p_success=1 / 6):
    sum_success = 0
    for i in range(min_n_success, n_dice + 1):
        sum_success += dice_probs_impl(n_dice, i, p_success)
    print(sum_success)
    # assert sum_success < 1
    return sum_success


def test():
    assert dice_probs(1, 1) == 1 / 6
    assert dice_probs(2, 2) == 1 / 36
    assert np.isclose(dice_probs_impl(10, 3, 1 / 6), 0.1550453595742519)
    assert dice_probs(10, 3) > 0.1550453595742519


def main(dice, successes, min_success=6):
    assert type(dice) is int
    assert dice > 0
    assert type(successes) is int
    assert successes > 0
    assert min_success in {1, 2, 3, 4, 5, 6}
    if successes > dice:
        print(
            "Need more successes than dice! I don't like those odds.", file=sys.stderr
        )
    p_success = (6 - min_success + 1) / 6
    p = dice_probs(dice, successes, p_success)
    print(
        f"The probability that at least {successes} dice "
        f"are greater than {min_success-1} when rolling {dice} dice is:"
        "\n{0:.2f}%".format(100 * p)
    )
    print("Assuming you attempt the roll 10 times, your probabilities of success are:")
    p_rep = 0
    for i in range(1, 11):  # geometric distribution
        p_inc = (1 - p) ** (i - 1) * p
        p_rep += p_inc
        print("{}: {:.2f}%".format(i, 100 * p_rep))


if __name__ == "__main__":
    # test()
    fire.Fire(main)
