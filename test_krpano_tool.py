# -- coding: utf-8 --

import krpano_tool

# pano_path = "/Users/leehenry/backup/krpano_test"
# image_name = "abudhabi.jpg"

#krpano_tool.tile_full(pano_path, image_name)

tile_path = "/Users/leehenry/backup/krpano_test/20131227151858296440_zsgyzrxq"
origin_image = "/Users/leehenry/backup/krpano_test/20131227151858296440_zsgyzrxq/abudhabi.jpg"
krpano_tool.tile_sphere(tile_path, origin_image)
