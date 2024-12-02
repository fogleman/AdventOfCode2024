from pyquery import PyQuery as pq
import datetime
import os
import requests

SESSION = ''
COOKIES = dict(session=SESSION)

def get_day():
    return datetime.date.today().day

def get_puzzle_input(day):
    url = 'https://adventofcode.com/2024/day/%d/input' % day
    print(url)
    r = requests.get(url, cookies=COOKIES)
    r.raise_for_status()
    return r.text

def get_example_inputs(day):
    url = 'https://adventofcode.com/2024/day/1'
    print(url)
    r = requests.get(url, cookies=COOKIES)
    r.raise_for_status()
    examples = [x.text for x in pq(r.text)('pre > code')]
    seen = set()
    return [x for x in examples if not (x in seen or seen.add(x))]

def fetch(day):
    path = '%02d.txt' % day
    if os.path.exists(path):
        return
    for i, example in enumerate(get_example_inputs(day)):
        example_path = '%02d.ex%d' % (day, i + 1)
        with open(example_path, 'w') as fp:
            fp.write(example)
    puzzle_input = get_puzzle_input(day)
    with open(path, 'w') as fp:
        fp.write(puzzle_input)

def main():
    fetch(get_day())

if __name__ == '__main__':
    main()
