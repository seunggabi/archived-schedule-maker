import json

day = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

config = {
    'max': 11
}

list = [
    {
        'name': '김다윤',
        'fix': [0, 1, 2, 5, 6],
        'o': [],
        'x': [3, 4],
        'cnt': 5
    },
    {
        'name': '조예진',
        'fix': [0, 1, 3, 4, 6],
        'o': [],
        'x': [2, 5],
        'cnt': 5
    },
    {
        'name': '이재준',
        'fix': [1, 2, 3, 4, 5],
        'o': [],
        'x': [0, 6],
        'cnt': 5
    },
    {
        'name': '김도량',
        'fix': [1, 2, 3, 6],
        'o': [],
        'x': [0, 3, 4],
        'cnt': 4
    },
    {
        'name': '김초연',
        'fix': [0, 1, 2, 3],
        'o': [],
        'x': [4, 5, 6],
        'cnt': 4
    },
    {
        'name': '박선정',
        'fix': [2, 3],
        'o': [],
        'x': [0, 1, 4, 5, 6],
        'cnt': 2
    },
    {
        'name': '최재인',
        'fix': [],
        'o': [],
        'x': [5],
        'cnt': 4
    },
    {
        'name': '조윤지',
        'fix': [],
        'o': [],
        'x': [5, 6],
        'cnt': 5
    },
    {
        'name': '이선민',
        'fix': [],
        'o': [],
        'x': [5],
        'cnt': 4
    },
    {
        'name': '임세빈',
        'fix': [],
        'o': [],
        'x': [5, 6],
        'cnt': 5
    },
    {
        'name': '황윤정',
        'fix': [3, 4, 5],
        'o': [],
        'x': [],
        'cnt': 3
    },
    {
        'name': '정다희',
        'fix': [],
        'o': [],
        'x': [0, 2],
        'cnt': 5
    },
    {
        'name': '김태식',
        'fix': [0, 4, 5, 6],
        'o': [],
        'x': [],
        'cnt': 4
    },
    {
        'name': '조민경',
        'fix': [],
        'o': [],
        'x': [2, 6],
        'cnt': 5
    },
    {
        'name': '문지연',
        'fix': [],
        'o': [],
        'x': [5, 6],
        'cnt': 5
    },
    {
        'name': '이재형',
        'fix': [],
        'o': [],
        'x': [3, 5, 6],
        'cnt': 3
    },
    {
        'name': '표예진',
        'fix': [],
        'o': [],
        'x': [3, 6],
        'cnt': 3
    },
    {
        'name': '김미정',
        'fix': [],
        'o': [],
        'x': [],
        'cnt': 5
    },
    {
        'name': '문주희',
        'fix': [],
        'o': [],
        'x': [0, 5, 6],
        'cnt': 3
    },
]


def fix():
    m = {}

    for k in list:
        for i in k['fix']:
            if i not in m:
                m[i] = []

            m[i].append(k['name'])
            k['cnt'] -= 1

    return m


def o(m):
    for k in list:
        for i in sorted(m.keys(), reverse=True):
            if k['cnt'] == 0:
                break

            if len(m[i]) == config['max']:
                continue

            if i in k['x']:
                continue

            if k['name'] in m[i]:
                continue

            m[i].append(k['name'])
            k['cnt'] -= 1

    return m


def sum(m):
    cnt = 0

    for i in m:
        cnt += len(m[i])

    return cnt


def pretty(obj):
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        indent=4)

def print_day(m):
    for i in sorted(m.keys()):
        print(m[i])

if __name__ == '__main__':
    m = fix()

    while (True):
        m = o(m)

        print(sum(m))
        print(list)
        if sum(m) == config['max'] * len(day.keys()):
            break
        print(config['max'] * len(day.keys()))
        break

    print_day(m)
