import os
import argparse
from _collections import deque
import requests

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="name of directory for files")
arg = parser.parse_args()


try:
    os.mkdir(arg.directory)
except FileExistsError:
    pass


back = deque()
current = []


def save_url(url):
    file = url.split('.')
    file = '.'.join(file[:-1])
    r = get_url(url)
    with open(f"{arg.directory}/{file}", 'w') as f:
            f.write(r)
            print(r)
    return main()


def get_url(url):
    if "http://" not in url[0:7]:
        url = "http://" + url
    r = requests.get(url)
    return r.text


def print_file(file):
    try:
        with open(f"{arg.directory}/{file}", 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: Incorrect URL")
    return main()


def main():
    url = input()
    if url == "exit":
        return exit()
    elif url == "back":
        title = back.pop()
        file = title.split('.')[0]
        return print_file(file)
    elif url[-4] == '.':
        if len(current) > 0:
            back.append(current.pop())
        current.append(url)
        return save_url(url)
    else:
        return print_file(url)


main()