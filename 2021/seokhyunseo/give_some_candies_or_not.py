import random


def trick_or_treat():
    """
    heavily borrowed from chanrankim's trick_or_treat.ipynb
    """
    return 'trick' if random.random() < .5 else 'treat'


def give_some_candies_or_not(tot):
    """
    tot : string
        trick or treat!
    return:
        # of candies: int (1~50) if treat
        None: None if trick
    """
    num_of_candies = random.randint(1, 50)
    if tot == 'treat':
        return num_of_candies
    else:
        return None


if __name__ == "__main__":
    tot = trick_or_treat()
    nc = give_some_candies_or_not(tot)
    print(f'{tot}')
    print(f'OK I will give you {nc} candies')