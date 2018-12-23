from math import sqrt

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    },
}


def sim_euclidean(p1, p2, dataset=critics):
    result = sum([
        pow(p1_rating - dataset[p2][movie], 2)
        for movie, p1_rating in dataset[p1].items()
        if movie in dataset[p2]
    ])

    if result == 0:
        return 0

    return 1 / sqrt(result)


def sim_pearson(p1, p2, dataset=critics):
    in_common = set(dataset[p1]).intersection(dataset[p2])
    n = len(in_common)

    if n == 0:
        return 0

    sum_p1 = sum([dataset[p1][movie] for movie in in_common])
    sum_p2 = sum([dataset[p2][movie] for movie in in_common])

    sum_p1_pow = sum([pow(dataset[p1][movie], 2) for movie in in_common])
    sum_p2_pow = sum([pow(dataset[p2][movie], 2) for movie in in_common])

    num = sum([dataset[p1][movie] * dataset[p2][movie] for movie in in_common]) - (sum_p1 * sum_p2) / n
    den = sqrt((sum_p1_pow - pow(sum_p1, 2) / n) * (sum_p2_pow - pow(sum_p2, 2) / n))

    return num/den
