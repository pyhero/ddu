scores = list()

# get scores
while True:
    score_input = input('Input score, end with -1: ')
    while not score_input.isdigit() and score_input != '-1':
        score_input = input('Input digit please: ')

    score = int(score_input)

    if score == -1:
        break

    scores.append(score)

# define result
score_avg, score_max, score_min = int(sum(scores)/len(scores)), max(scores), min(scores)

# debug
print(scores)

# print result
print('avg: {}, max: {}, min: {}'.format(score_avg, score_max, score_min))
