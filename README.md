## Overview
The script will calculate the likelihood of rolling at least a {1,2,3,4,5,6} at least {1,2,...} times.
The calculation is based on the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution).

```bash
python dice_probs.py $NUMBER_OF_D6 $NUMBER_OF_SUCCESSES $MIN_DIE_SUCCESS
```

It also outputs the likelihood of success assuming multiple trials. This is based on the [geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution).

## Extensions
Extending this to account for differently sided die would be simple and useful, presumably.
