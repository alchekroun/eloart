def probawin(ra, rb):
    return 1 / (1 + pow(10, (rb - ra) / 400))


def newelo(ra, rb, score):
    return ra + 32 * (score - probawin(ra, rb))
