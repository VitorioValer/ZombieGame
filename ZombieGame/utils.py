#!/usr/bin/env python

import subprocess
import os
import urllib.request

from constants import characters, IMAGES_PATH


def image_handler(character, img_source):
    zip_file_name = img_source.split('/')[-1]
    dir_path = os.path.join(IMAGES_PATH, f'{character}')

    if not os.path.exists(zip_file_name):
        urllib.request.urlretrieve(img_source, zip_file_name)

    terminal(command=['unzip', zip_file_name])
    terminal(command=['rm', zip_file_name])
    terminal(command=['mv', 'png', dir_path])

    for sb in os.listdir(dir_path):
        sb_path = os.path.join(dir_path, sb)

        if os.path.isdir(sb_path) and sb.islower():
            new_path = os.path.join(dir_path, sb.capitalize())

            terminal(command=['mv', sb_path, new_path])

    for root, _, files in os.walk(dir_path, topdown=True):
        for file in files:
            old_path = os.path.join(root, file)

            name = ''.join(
                [x for x in file[::] if x.isalpha()]
            ).replace('png', '')

            index = ''.join(
                [x for x in file[::] if x.isnumeric()]
            )

            try:
                index = int(index)

            except ValueError:
                index = '1'

            new_dir = os.path.join(root, name)

            if not os.path.exists(new_dir):
                terminal(command=['mkdir', new_dir])

            if character == 'Ninja' and name == 'Attack' and index % 2:
                terminal(command=['rm', old_path])

            else:
                new_path = os.path.join(new_dir, f'{name.lower()}{index}')
                terminal(command=['mv', old_path, new_path])


def find_directory():
    if not os.path.exists(IMAGES_PATH):
        _command = ['mkdir', IMAGES_PATH]
        terminal(_command)

    for character, img_source in characters.items():
        image_handler(character, img_source)


def terminal(command):
    _process = subprocess.Popen(command, stdout=subprocess.PIPE)
    _output, _error = _process.communicate()


def refresh_images():
    command = ['rm', '-r', 'Images', 'vector']
    terminal(command)

    find_directory()


if __name__ == '__main__':
    refresh_images()
