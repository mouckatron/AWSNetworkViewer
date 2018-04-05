# -*- coding: utf-8 -*-

import svgwrite


class Positioner(object):

    def __init__(self, direction='vertical', buffer_space=2):
        self.children = []
        self.begin_x = 0
        self.begin_y = 0
        self.direction = direction
        self.buffer_space = buffer_space

    def add_child(self, child):
        self.children.append(child)
        self.set_child_positions()

    def set_child_positions(self):
        x = self.begin_x
        y = self.begin_y

        if self.direction == 'vertical':
            self._set_child_positions_vertically(x, y)
        else:
            self._set_child_positions_horizontally(x, y)

    def _set_child_positions_horizontally(self, x, y):

        for child in self.children:
            child.position = (x, y)
            x += (child.width + self.buffer_space)

    def set_child_positions_vertically(self, x, y):
        for child in self.children:
            child.position = (x, y)
            y += (child.width + self.buffer_space)

    def write(self, svg_object):
        for child in self.children:
            child.write(svg_object)


class SVGObject(object):

    def __init__(self, width, height, object_id):
        self.width = width
        self.height = height
        self.object_id = object_id

    def calculate_size(self):
        pass

    def write(self, svg_object):
        svg_object.add(svgwrite.shapes.Rect(self.position, (self.width, self.height), fill='white'))


class SVGObjectWithTitleBar(SVGObject):

    def __init__(self, width, height, object_id, title):
        super(SVGObjectWithTitleBar, self).__init__(width, height, object_id)
        self.title = title

    def write(self, svg_object):
        container = svgwrite.container.Group()
        container.add(svgwrite.shapes.Rect(self.__get_relative_position(0, 0), (self.width, self.height), fill='white', stroke='black'))

        titlecontainer = svgwrite.container.Group()
        titlecontainer.add(svgwrite.shapes.Rect(self.__get_relative_position(1, 1), (self.width-2, 12), fill='black'))
        titlecontainer.add(svgwrite.text.Text(self.title, self.__get_relative_position(1, 12), fill='white'))

        container.add(titlecontainer)
        svg_object.add(container)

    def __get_relative_position(self, x, y):
        begin_x, begin_y = self.position
        return ((begin_x + x), (begin_y + y))


class Account(SVGObjectWithTitleBar):

    width = 200
    height = 200

    def __init__(self, object_id, title):
        super(self.__class__, self).__init__(Account.width, Account.height, object_id, title)
        self.position = (0, 0)


class Region(SVGObject):
    pass


class VPC(SVGObject):
    pass


class VPCPeering(SVGObject):
    pass


class Subnet(SVGObject):
    pass
