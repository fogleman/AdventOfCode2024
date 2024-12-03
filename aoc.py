#!/usr/bin/env python

from pyquery import PyQuery as pq
import datetime
import glob
import os
import requests
import subprocess
import sys

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
    url = 'https://adventofcode.com/2024/day/%d' % day
    print(url)
    r = requests.get(url, cookies=COOKIES)
    r.raise_for_status()
    examples = [x.text for x in pq(r.text)('pre > code')]
    seen = set()
    return [x for x in examples if not (x in seen or seen.add(x))]

def submit_answer(day, level, answer):
    url = 'https://adventofcode.com/2024/day/%d/answer' % day
    data = dict(level=level, answer=answer)
    print(url, data)
    r = requests.post(url, cookies=COOKIES, data=data)
    r.raise_for_status()
    result = [x.text for x in pq(r.text)('main > article > p')]
    if len(result) == 1:
        print(result[0])
    else:
        print(r.text)

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

def run_input(day, filename):
    result = subprocess.run(
        ['python', '%02d.py' % day, filename],
        capture_output=True,
        text=True)
    output = result.stdout.rstrip()
    if result.returncode:
        print(result.stderr.rstrip())
    return output

def run(day):
    prefix = '%02d' % day
    filenames = glob.glob(prefix + '.ex*') + [prefix + '.txt']
    answer = None
    for filename in filenames:
        print(filename)
        output = run_input(day, filename)
        lines = output.split('\n')
        answer = lines[-1]
        print(output)
        print()
    return answer

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        day = int(args[0])
    else:
        day = get_day()
    fetch(day)
    answer = run(day)
    if answer:
        level = input('Submit %r? [1/2] ' % answer)
        if level and level in '12':
            submit_answer(day, level, answer)

if __name__ == '__main__':
    main()
