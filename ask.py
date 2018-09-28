answers = dict()
persons = ['A', 'B', 'C', 'D']

# get answers
for person in persons:
    print('Ask {}'.format(person))
    answer = dict()
    total = {'0': 0, '1': 0, '2': 0}
    for p in [x for x in persons if x != person]:
        value = input('Is {} the prisoners？ 0: No, 1: Yes, 2 Unknown: '.format(p))
        while value not in ['0', '1', '2']:
            value = input('Bad input, chose from: 0: No, 1: Yes, 2 Unknown: ')

        total[value] += 1
        answer[p] = int(value)

    mapping = {'是凶手票数': total['1'], '不是凶手票数': total['0'], '不知道票数': total['2']}
    answers[person] = [mapping, answer]

# judge prisoners
for k, v in answers.items():
    print('{}: {}, 投票情况: {}'.format(k, v[0], v[1]))

result = sorted(answers.items(), key=lambda x: x[1][0]['是凶手票数'])[-1][0]
print('凶手是{}'.format(result))
