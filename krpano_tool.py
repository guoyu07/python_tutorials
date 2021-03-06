# -- coding: utf-8 --

"""Module for Python to call Krpano kmaketiles tools to tile, resize and convert images.

There are four ways to use this module.
1. tile_full()   can tile spherical images to cube, sphere and cover images.
2. tile_cube()   can tile spherical images to cube images.
3. tile_sphere() can tile spherical images to sphere images.
4. tile_cover()  can tile spherical images to cover images.
"""

from datetime import datetime
import string
import random
import os
import sys
import subprocess
import zipfile
import shutil

KRPANO_PATH = "/Users/leehenry/Desktop/数据运营管理平台/krpanotools-1.16.9-mac64"
KRPANO_CUBE_CONFIG = KRPANO_PATH + "/templates/huilian_cube.config"
KRPANO_SPHERE_CONFIG = KRPANO_PATH + "/templates/huilian_sphere.config"
KMAKEMULTIRES_TOOL = KRPANO_PATH + "/kmakemultires"
KMAKETILES_TOOL = KRPANO_PATH + "/kmaketiles"


CUBE_TILE_PATH = "/cube/tiles"
CUBE_FOLDERS = { '1': '512', '2': '1024', '3': '2048' }

SPHERE_PATH = '/sphere/'
SPHERE_SETTINGS = { '1024x512': [['512h.jpg', '95'], ['512m.jpg', '85'], ['512l.jpg', '75']],
                    '2048x1024': [['1024h.jpg', '95'], ['1024m.jpg', '85'], ['1024l.jpg', '75']],
                    '4096x2048': [['2048h.jpg', '95'], ['2048m.jpg', '85'], ['2048l.jpg', '75']]}

def _make_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def _splice_path(path, folder):
    return "%s/%s" %(path, folder)

def _random_number():
    return ''.join(random.choice(string.ascii_lowercase) for x in range(8))

def _secure_imagename():
    return '_'.join([datetime.now().strftime("%Y%m%d%H%M%S%f"), _random_number()])

def _rename_cube_folders(path):
    folder_path = path + CUBE_TILE_PATH
    for key,value in CUBE_FOLDERS.iteritems():
        os.rename(os.path.join(folder_path, key),
                  os.path.join(folder_path, value))

def _copy_image(pano_path, image_name, tile_path):
    input_image = _splice_path(pano_path, image_name)
    origin_image = _splice_path(tile_path, image_name)
    os.link(input_image, origin_image)
    return origin_image

def _trim_path(parent_path, path):
    path = path.replace(parent_path + os.path.sep, "", 1)
    return os.path.normcase(path) 

def _zip_folder(pano_path, tile_path, output_file):
    contents = os.walk(tile_path)
    zip_file = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
    for root, folders, files in contents:
        for folder_name in folders:
            absolute_path = os.path.join(root, folder_name)
            relative_path = _trim_path(tile_path, absolute_path)
            zip_file.write(absolute_path, relative_path)
        for file_name in files:
            absolute_path = os.path.join(root, file_name)
            relative_path = _trim_path(tile_path, absolute_path)
            zip_file.write(absolute_path, relative_path)
    zip_file.close()

def _remove_folder(tile_path):
    shutil.rmtree(tile_path)

def tile_cube(path, image):
    print "start tile cube"
    cube_command = "%s -config=%s %s"%(KMAKEMULTIRES_TOOL, KRPANO_CUBE_CONFIG, image)
    pcube = subprocess.Popen(cube_command, shell=True, stderr=subprocess.PIPE)

    while True:
        out = pcube.stderr.read(1)
        if out == '' and pcube.poll() != None:
            _rename_cube_folders(path)
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

    print "end tile cube"


def tile_sphere(tile_path, origin_image):
    print "tile sphere"
    for resize,spheres in SPHERE_SETTINGS.iteritems():
        for sphere in spheres:
            output_image = tile_path + SPHERE_PATH + sphere[0]
            sphere_command = "%s %s %s 0 -resize=%s -jpegquality=%s" %(KMAKETILES_TOOL, origin_image, output_image, resize, sphere[1])
            pcube = subprocess.Popen(sphere_command, shell=True, stderr=subprocess.PIPE)

            while True:
                out = pcube.stderr.read(1)
                if out == '' and pcube.poll() != None:
                    break
                if out != '':
                    sys.stdout.write(out)
                    sys.stdout.flush()
    print "end tile sphere"


def tile_cover():
    print "tile cover"

    print "end tile cover"


def tile_full(pano_path, image_name):
    zip_folder = _secure_imagename()
    zip_file = _splice_path(pano_path, zip_folder + '.zip')
    tile_path = _splice_path(pano_path, zip_folder)
    _make_directory(tile_path)

    origin_image = _copy_image(pano_path, image_name, tile_path)

    try:
        tile_cube(tile_path, origin_image)
        #tile_sphere(tile_path, origin_image)
        tile_cover()
    except Exception:
        print "tile caused exception"
    else:
        _zip_folder(pano_path, tile_path, zip_file)
    finally:
        _remove_folder(tile_path)
