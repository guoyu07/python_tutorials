# -- coding: utf-8 --

import subprocess
import os

krpano_path = "/Users/leehenry/Desktop/数据运营管理平台/krpanotools-1.16.9-mac64"
image_path = "/Users/leehenry/backup/krpano_test"
folder_path = "%s/cube" %(image_path)
krpano_command = "%s/kmakemultires -config=%s/templates/tc_huilian_cube.config %s/abudhabi_20080731_15.jpg"%(krpano_path, krpano_path, image_path)

def rename_folder():
    print "rename folder..."
    folders = { '1': '512', '2': '1024', '3': '2048' }
    for key,value in folders.iteritems():
        os.rename(os.path.join(folder_path, key),
                  os.path.join(folder_path, value))
    print "OK."


p = subprocess.Popen(krpano_command, shell=True, stderr=subprocess.PIPE)

while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        print "krpano convert cube images done."
        rename_folder()
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()