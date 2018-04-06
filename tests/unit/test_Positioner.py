
import unittest
import unittest.mock

from awsnetworkbrowser import objects


class TestPositioner(unittest.TestCase):

    def test_positioner_with_defaults(self):

        subject = objects.Positioner()
        subject.add_child(objects.Account('123456789', 'Account 1'))

        assert subject.children[0].position == (0, 0)

    def test_positioner_with_horizontal_direction(self):
        subject = objects.Positioner(direction='horizontal')
        subject.add_child(objects.Account('123456789', 'Account 1'))

        assert subject.children[0].position == (0, 0)

    def test_positioner_with_beginning_x_offset(self):
        subject = objects.Positioner(direction='horizontal', begin_offset=(10, 0))
        subject.add_child(objects.Account('123456789', 'Account 1'))

        assert subject.children[0].position == (10, 0)

    def test_positioner_with_multiple_children_vertically(self):
        subject = objects.Positioner(buffer_space=0)
        objects.Account.height = 10  # force setting to known value in case code default changes
        objects.Account.width = 10  # force setting to known value in case code default changes

        subject.add_child(objects.Account('123456789', 'Account 1'))
        subject.add_child(objects.Account('123456789', 'Account 2'))

        assert subject.children[0].position == (0, 0)
        assert subject.children[1].position == (0, 10)

    def test_positioner_with_multiple_children_horizontally(self):
        subject = objects.Positioner(buffer_space=0, direction='horizontal')
        objects.Account.height = 10  # force setting to known value in case code default changes
        objects.Account.width = 10  # force setting to known value in case code default changes

        subject.add_child(objects.Account('123456789', 'Account 1'))
        subject.add_child(objects.Account('123456789', 'Account 2'))

        assert subject.children[0].position == (0, 0)
        assert subject.children[1].position == (10, 0)

    def test_positioner_with_multiple_children_and_buffer_space(self):
        subject = objects.Positioner(buffer_space=5)
        objects.Account.height = 10  # force setting to known value in case code default changes
        objects.Account.width = 10  # force setting to known value in case code default changes

        subject.add_child(objects.Account('123456789', 'Account 1'))
        subject.add_child(objects.Account('123456789', 'Account 2'))

        assert subject.children[0].position == (0, 0)
        assert subject.children[1].position == (0, 15)

    def test_positioner_writes(self):

        mock_svg = unittest.mock.Mock()
        mock_object = unittest.mock.Mock()
        mock_object.write = unittest.mock.Mock()

        subject = objects.Positioner()
        subject.children = [mock_object]

        subject.write(mock_svg)

        mock_object.write.assert_called_with(mock_svg)

    def test_positioner_writes_with_multiple_children(self):

        mock_object = unittest.mock.Mock()
        mock_object.write = unittest.mock.Mock()

        subject = objects.Positioner()
        subject.children = [mock_object, mock_object]

        subject.write(None)

        assert mock_object.write.call_count == 2
