# -- coding: utf-8 --

import os
import zipfile


def _trim_path(parent_path, path):
    """
    Prepare the proper archive path by removing the useless absolute path.
    """
    path = path.replace(parent_path + os.path.sep, "", 1)
    return os.path.normcase(path)

def zip_folder(src_path, output_file):
    """
    Zip the entire source directory to a zip file.
    """
    print "start zip folders"
    def _write(root, filename):
        abs_path = os.path.join(root, filename)
        rel_path = _trim_path(src_path, abs_path)
        zip_file.write(abs_path, rel_path)
    try:
        zip_file = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in os.walk(src_path):
            for filename in folders + files:
                _write(root, filename)
    finally:
        zip_file.close()
        print "end zip folders"

def unzip_file(zip_file, output_path):
    print "start unzip file"
    if os.path.isfile(zip_file):
        print "unzip file..."
        zipfile.ZipFile(zip_file).extractall(output_path)
    print "end unzip file"


src_path = "./doc/sources"
output_file = "./doc/sources.zip"
zip_folder(src_path, output_file)

zip_file = "./doc/tiles.zip"
output_path = "./doc"
unzip_file(zip_file, output_path)