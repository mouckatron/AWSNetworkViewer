# -*- coding: utf-8 -*-

import svgwrite

from awsnetworkbrowser import objects


if __name__ == '__main__':

    root_positioner = objects.Positioner('horizontal', buffer_space=20)
    root_positioner.add_child(objects.Account('123456789', 'Account 1'))
    root_positioner.add_child(objects.Account('234567890', 'Account 2'))

    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    root_positioner.write(dwg)

    dwg.save()
    print('.')
