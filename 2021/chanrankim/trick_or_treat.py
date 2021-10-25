import random

# Returns Trick or Treat
def trcik_or_treat():
    if random.random() < .5:
        return 'trick'
    return 'treat'

if __name__ == "__main__":
    trcik_or_treat()