"""
pygame-menu
https://github.com/ppizarror/pygame-menu

TEST FRAME WIDGET
Test Frame. Frame is the most complex widget as this interacts with menu, modifies
it's layout and contains other widgets.

License:
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2017-2021 Pablo Pizarro R. @ppizarror

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------
"""

__all__ = ['FrameWidgetTest']

from test._utils import MenuUtils, surface, PygameEventUtils, test_reset_surface, TEST_THEME, PYGAME_V2, \
    WIDGET_MOUSEOVER, reset_widgets_over
import unittest

import pygame
import pygame_menu

from pygame_menu.controls import KEY_MOVE_UP, KEY_LEFT, KEY_RIGHT, JOY_RIGHT, JOY_LEFT, KEY_MOVE_DOWN
from pygame_menu.locals import ORIENTATION_VERTICAL, ORIENTATION_HORIZONTAL
from pygame_menu.widgets import Button


class FrameWidgetTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setup frame widget test.
        """
        test_reset_surface()

    def test_general(self) -> None:
        """
        Test frame widget containers.
        """
        menu = MenuUtils.generic_menu(theme=TEST_THEME.copy())

        menu.add.button('rr')
        frame = menu.add.frame_h(250, 100, background_color=(200, 0, 0))
        frame._pack_margin_warning = False
        btn = menu.add.button('nice1')
        menu.add.button('44')
        frame2 = menu.add.frame_v(50, 250, background_color=(0, 0, 200))
        frame2._pack_margin_warning = False
        btn2 = menu.add.button('nice2')
        btn3 = menu.add.button('nice3')

        frame11 = menu.add.frame_v(50, 90, background_color=(0, 200, 0))
        frame11._pack_margin_warning = False
        btn11 = menu.add.button('11')
        btn12 = menu.add.button('12')

        frame11.pack(btn11)
        frame11.pack(btn12)

        frame.pack(btn)
        frame.pack(btn2, pygame_menu.locals.ALIGN_CENTER, vertical_position=pygame_menu.locals.POSITION_CENTER)
        frame.pack(frame11, pygame_menu.locals.ALIGN_RIGHT, vertical_position=pygame_menu.locals.POSITION_SOUTH)

        frame2.pack(menu.add.button('1'))
        frame2.pack(menu.add.button('2'), alignment=pygame_menu.locals.ALIGN_CENTER)
        frame2.pack(menu.add.button('3'), alignment=pygame_menu.locals.ALIGN_RIGHT)

        for w in frame.get_widgets():
            w.get_selection_effect().zero_margin()
        for w in frame2.get_widgets():
            w.get_selection_effect().zero_margin()

        menu.render()
        wid = menu.get_widgets()
        self.assertEqual(wid[0].get_col_row_index(), (0, 0, 0))
        self.assertEqual(wid[1].get_col_row_index(), (0, 1, 1))
        self.assertEqual(wid[2].get_col_row_index(), (0, 1, 2))
        self.assertEqual(wid[3].get_col_row_index(), (0, 1, 3))
        self.assertEqual(wid[4].get_col_row_index(), (0, 1, 4))
        self.assertEqual(wid[5].get_col_row_index(), (0, 1, 5))
        self.assertEqual(wid[6].get_col_row_index(), (0, 1, 6))
        self.assertEqual(wid[7].get_col_row_index(), (0, 2, 7))
        self.assertEqual(wid[8].get_col_row_index(), (0, 3, 8))
        self.assertEqual(wid[9].get_col_row_index(), (0, 3, 9))
        self.assertEqual(wid[10].get_col_row_index(), (0, 3, 10))
        self.assertEqual(wid[11].get_col_row_index(), (0, 3, 11))
        self.assertEqual(wid[12].get_col_row_index(), (0, 4, 12))

        self.assertIsNone(btn3.get_frame())
        self.assertEqual(btn2.get_frame(), frame)
        self.assertEqual(btn2.get_translate(), (0, 0))
        self.assertEqual(btn2.get_translate(virtual=True), (88, 29))
        self.assertFalse(btn2.is_floating())
        menu.remove_widget(btn2)
        self.assertIsNone(btn2.get_frame())
        self.assertEqual(btn2.get_translate(), (0, 0))
        self.assertEqual(btn2.get_translate(virtual=True), (0, 0))
        self.assertTrue(btn2.is_floating())

        wid = menu.get_widgets()
        if PYGAME_V2:
            self.assertEqual(wid[0].get_position(), (288, 5))
            self.assertEqual(wid[1].get_position(), (175, 56))
            self.assertEqual(wid[2].get_position(), (175, 56))
            self.assertEqual(wid[3].get_position(), (375, 66))
            self.assertEqual(wid[4].get_position(), (375, 66))
            self.assertEqual(wid[5].get_position(), (375, 107))
            self.assertEqual(wid[6].get_position(), (283, 166))
            self.assertEqual(wid[7].get_position(), (275, 217))
            self.assertEqual(wid[8].get_position(), (275, 217))
            self.assertEqual(wid[9].get_position(), (291, 258))
            self.assertEqual(wid[10].get_position(), (308, 299))
            self.assertEqual(wid[11].get_position(), (263, 477))
        else:
            self.assertEqual(wid[0].get_position(), (288, 5))
            self.assertEqual(wid[1].get_position(), (175, 57))
            self.assertEqual(wid[2].get_position(), (175, 57))
            self.assertEqual(wid[3].get_position(), (375, 67))
            self.assertEqual(wid[4].get_position(), (375, 67))
            self.assertEqual(wid[5].get_position(), (375, 109))
            self.assertEqual(wid[6].get_position(), (283, 167))
            self.assertEqual(wid[7].get_position(), (275, 219))
            self.assertEqual(wid[8].get_position(), (275, 219))
            self.assertEqual(wid[9].get_position(), (291, 261))
            self.assertEqual(wid[10].get_position(), (308, 303))
            self.assertEqual(wid[11].get_position(), (263, 479))

        theme = TEST_THEME.copy()
        menu = MenuUtils.generic_menu(theme=theme)
        menu.get_theme().widget_selection_effect.zero_margin()
        menu.get_theme().widget_font_size = 18

        frame = menu.add.frame_v(250, 150, background_color=(50, 50, 50))
        frame._pack_margin_warning = False
        frame_title = menu.add.frame_h(250, 30, background_color=(180, 180, 180))
        frame_title._pack_margin_warning = False
        frame_content = menu.add.frame_v(250, 120)
        frame_content._pack_margin_warning = False
        frame.pack(frame_title)
        frame.pack(frame_content)

        frame_title.pack(menu.add.label('Settings'), margin=(2, 2))
        closebtn = frame_title.pack(
            menu.add.button('Close', pygame_menu.events.EXIT, padding=(0, 5), background_color=(160, 160, 160)),
            alignment=pygame_menu.locals.ALIGN_RIGHT, margin=(-2, 2))
        frame_content.pack(menu.add.label('Pick a number', font_color=(150, 150, 150)),
                           alignment=pygame_menu.locals.ALIGN_CENTER)
        frame_numbers = menu.add.frame_h(250, 42, background_color=(255, 255, 255), font_color=(2000, 0, 0),
                                         frame_id='frame_numbers')
        frame_numbers._pack_margin_warning = False
        frame_content.pack(frame_numbers)
        for i in range(9):
            frame_numbers.pack(menu.add.button(i, font_color=(5 * i, 11 * i, 13 * i), font_size=30),
                               alignment=pygame_menu.locals.ALIGN_CENTER)
        self.assertRaises(AssertionError, lambda: frame_numbers.pack(closebtn))
        frame_content.pack(menu.add.vertical_margin(15))
        frame_content.pack(menu.add.toggle_switch('Nice toggle', False, width=100, font_color=(150, 150, 150)),
                           alignment=pygame_menu.locals.ALIGN_CENTER)
        menu.render()

        self.assertEqual(menu.get_width(widget=True), 250)
        self.assertEqual(menu.get_height(widget=True), 150)
        self.assertEqual(menu._widget_offset[1], 97)
        self.assertEqual(frame_numbers.get_widgets()[0].get_translate(), (0, 0))
        self.assertEqual(frame_numbers.get_widgets()[0].get_translate(virtual=True), (48, 0))
        self.assertEqual(frame_numbers.get_widgets()[0].get_position(), (223, 153 if PYGAME_V2 else 154))
        self.assertEqual(frame_numbers._recursive_render, 0)
        previwdg = frame_numbers.get_widgets()
        cwidget = frame_numbers._control_widget
        self.assertEqual(cwidget, previwdg[0])
        frame_numbers.unpack(cwidget)
        self.assertTrue(cwidget.is_floating())
        self.assertIn(cwidget, menu.get_widgets())
        self.assertRaises(ValueError, lambda: frame_numbers.unpack(previwdg[0]))
        self.assertEqual(frame_numbers._control_widget, previwdg[1])
        for w in frame_numbers.get_widgets():
            frame_numbers.unpack(w)
        self.assertEqual(len(frame_numbers._widgets), 0)
        self.assertRaises(AssertionError, lambda: frame_numbers.unpack(previwdg[0]))

        # Test sizes
        size_exception = pygame_menu.widgets.widget.frame._FrameSizeException
        self.assertFalse(frame_numbers._relax)
        self.assertEqual(len(frame_numbers.get_widgets(unpack_subframes_include_frame=True)), 0)
        self.assertRaises(size_exception, lambda: frame_numbers.pack(menu.add.frame_v(100, 400)))
        self.assertRaises(size_exception, lambda: frame_numbers.pack(menu.add.frame_v(400, 10)))
        self.assertEqual(len(frame_numbers.get_widgets(unpack_subframes_include_frame=True)), 0)
        frame_numbers.pack(menu.add.frame_v(10, 10), alignment=pygame_menu.locals.ALIGN_CENTER)
        frame_numbers.pack(menu.add.frame_v(10, 10), alignment=pygame_menu.locals.ALIGN_RIGHT)
        frame_numbers.pack(menu.add.frame_v(10, 10))

        frame_v = menu.add.frame_v(400, 100, font_color=(2000, 0, 0))  # Clearly a invalid font color
        frame_v._pack_margin_warning = False
        self.assertRaises(size_exception, lambda: frame_v.pack(menu.add.frame_v(100, 400)))
        self.assertRaises(size_exception, lambda: frame_v.pack(menu.add.frame_v(500, 100)))
        frame_v.pack(menu.add.frame_v(25, 25), vertical_position=pygame_menu.locals.POSITION_CENTER)
        frame_v.pack(menu.add.frame_v(25, 25), vertical_position=pygame_menu.locals.POSITION_CENTER)
        frame_v.pack(menu.add.frame_v(25, 25), vertical_position=pygame_menu.locals.POSITION_CENTER)
        frame_v.pack(menu.add.frame_v(25, 25), vertical_position=pygame_menu.locals.POSITION_SOUTH)
        self.assertRaises(size_exception, lambda: frame_v.pack(menu.add.frame_v(100, 1)))

        # Apply transforms
        wid = frame_v
        wid.set_position(1, 1)
        self.assertEqual(wid.get_position(), (1, 1))

        wid.translate(1, 1)
        self.assertEqual(wid.get_translate(), (1, 1))

        wid.rotate(10)
        self.assertEqual(wid._angle, 0)

        wid.scale(100, 100)
        self.assertFalse(wid._scale[0])
        self.assertEqual(wid._scale[1], 1)
        self.assertEqual(wid._scale[2], 1)

        wid.resize(10, 10)
        self.assertFalse(wid._scale[0])
        self.assertEqual(wid._scale[1], 1)
        self.assertEqual(wid._scale[2], 1)

        wid.flip(True, True)
        self.assertFalse(wid._flip[0])
        self.assertFalse(wid._flip[1])

        wid.set_max_width(100)
        self.assertIsNone(wid._max_width[0])

        wid.set_max_height(100)
        self.assertIsNone(wid._max_height[0])

        # Selection
        wid.select()
        self.assertFalse(wid.is_selected())
        self.assertFalse(wid.is_selectable)

        weff = wid.get_selection_effect()
        wid.set_selection_effect(menu.get_theme().widget_selection_effect)
        self.assertEqual(wid.get_selection_effect(), weff)

        draw = [False]

        # noinspection PyUnusedLocal
        def _draw(*args) -> None:
            draw[0] = True

        drawid = wid.add_draw_callback(_draw)
        wid.draw(surface)
        self.assertTrue(draw[0])
        draw[0] = False
        wid.remove_draw_callback(drawid)
        wid.draw(surface)
        self.assertFalse(draw[0])

        wid._draw(surface)
        wid.update([])

        # Test frame with Widgets not included in same menu
        frame_v.clear()
        self.assertEqual(frame_v.get_widgets(), ())
        b1 = frame_v.pack(menu.add.button('v1'))
        b2 = frame_v.pack(menu.add.button('v1'))
        self.assertFalse(b1.is_floating())
        self.assertFalse(b2.is_floating())
        self.assertEqual(b1.get_frame(), frame_v)
        self.assertEqual(b2.get_frame(), frame_v)
        self.assertEqual(b1.get_translate(virtual=True), (0, 0))
        self.assertEqual(b2.get_translate(virtual=True), (0, 25 if PYGAME_V2 else 26))
        menu.remove_widget(frame_v)
        self.assertTrue(b1.is_floating())
        self.assertTrue(b2.is_floating())
        self.assertIsNone(b1.get_frame())
        self.assertIsNone(b2.get_frame())
        self.assertIsNone(frame_v.get_menu())
        self.assertEqual(b1.get_translate(virtual=True), (0, 0))
        self.assertEqual(b2.get_translate(virtual=True), (0, 0))

        # Test widget addition on frame which is not inserted in a menu
        self.assertRaises(AssertionError, lambda: frame_v.pack(menu.add.button('invalid')))

        h = menu.add.frame_h(400, 300, background_color=(0, 60, 80))
        btn = pygame_menu.widgets.Button('button')
        self.assertRaises(AssertionError, lambda: h.pack(btn))  # Not configured
        menu.add.configure_defaults_widget(btn)
        h.pack(btn)
        h.pack(menu.add.button('button legit'))
        self.assertTrue(h.contains_widget(btn))

    def test_sort(self) -> None:
        """
        Test frame sorting.
        """
        menu = MenuUtils.generic_menu()
        b0 = menu.add.button('b0')
        b1 = menu.add.button('b1')
        b2 = menu.add.button('b2')
        b3 = menu.add.button('b3')
        f1 = menu.add.frame_v(300, 800, frame_id='f1')
        f2 = menu.add.frame_v(200, 500, frame_id='f2')

        # Test basics
        self.assertEqual(f1.get_size(), (300, 800))
        self.assertEqual(f2.get_size(), (200, 500))
        self.assertEqual(menu._widgets, [b0, b1, b2, b3, f1, f2])
        f1.pack(b1)
        self.assertEqual(b1.get_frame(), f1)
        self.assertEqual(menu._widgets, [b0, b2, b3, f1, b1, f2])
        f2.pack(b3)
        self.assertEqual(menu._widgets, [b0, b2, f1, b1, f2, b3])
        f1.pack(b2)
        self.assertEqual(menu._widgets, [b0, f1, b1, b2, f2, b3])
        f1.pack(f2)
        self.assertEqual(menu._widgets, [b0, f1, b1, b2, f2, b3])
        self.assertEqual(menu.get_selected_widget(), b0)

        # Add two more buttons
        b4 = menu.add.button('b4')
        self.assertEqual(menu._widgets, [b0, f1, b1, b2, f2, b3, b4])
        b5 = menu.add.button('b5')
        self.assertEqual(menu._widgets, [b0, f1, b1, b2, f2, b3, b4, b5])

        # Test positioning
        self.assertEqual(f1.get_indices(), (2, 4))
        self.assertEqual(f2.get_indices(), (5, 5))
        f2.pack(b5)
        self.assertEqual(menu._widgets, [b0, f1, b1, b2, f2, b3, b5, b4])
        f1.pack(b0)
        self.assertEqual(menu.get_selected_widget(), b0)
        self.assertEqual(menu._widgets, [f1, b1, b2, f2, b3, b5, b0, b4])
        f1.pack(b4)
        self.assertEqual(menu._widgets, [f1, b1, b2, f2, b3, b5, b0, b4])
        self.assertRaises(AssertionError, lambda: f1.pack(b4))
        self.assertRaises(AssertionError, lambda: f1.pack(b3))
        self.assertEqual(f2.get_frame(), f1)
        self.assertEqual(f2.get_frame_depth(), 1)
        self.assertEqual(b3.get_frame(), f2)
        self.assertEqual(b3.get_frame_depth(), 2)
        self.assertEqual(f1.get_indices(), (1, 7))
        self.assertEqual(f2.get_indices(), (4, 5))

        # Unpack f2
        f1.unpack(f2)
        self.assertEqual(menu._widgets, [f1, b1, b2, b0, b4, f2, b3, b5])
        self.assertEqual(f1.get_indices(), (1, 4))
        self.assertEqual(f2.get_indices(), (6, 7))

        # Create new frame 3, inside 2
        f3 = menu.add.frame_h(150, 200, frame_id='f3')
        f2.pack(f3)
        self.assertEqual(f3.get_indices(), (-1, -1))
        self.assertEqual(menu._widgets, [f1, b1, b2, b0, b4, f2, b3, b5, f3])
        self.assertEqual(b1, f3.pack(f1.unpack(b1)))
        self.assertEqual(menu._widgets, [f1, b2, b0, b4, f2, b3, b5, f3, b1])

        # Create container frame
        f4 = menu.add.frame_v(400, 1500, frame_id='f4')
        self.assertIsNone(f2.get_frame())
        f4.pack(f2)
        self.assertEqual(menu._widgets, [f1, b2, b0, b4, f4, f2, b3, b5, f3, b1])
        f4.pack(f1.unpack(b2))
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, f2, b3, b5, f3, b1, b2])

        # Sort two widgets
        menu.move_widget_index(b2, f2)
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, b3, b5, f3, b1])
        self.assertRaises(AssertionError, lambda: menu.move_widget_index(b2, b3))
        menu.move_widget_index(b3, b5)
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, b5, b3, f3, b1])
        menu.move_widget_index(f3, b5)
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, f3, b1, b5, b3])
        f3.pack(f2.unpack(b5))
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, f3, b1, b5, b3])
        menu.move_widget_index(b1, b5)
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, f3, b5, b1, b3])
        menu.move_widget_index(b3, f3)
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, b3, f3, b5, b1])
        menu.move_widget_index(f3, b3)
        self.assertEqual(menu._widgets, [f1, b0, b4, f4, b2, f2, f3, b5, b1, b3])
        self.assertEqual(menu.get_selected_widget(), b0)

        # Test advanced packing
        f4.pack(f1)
        self.assertEqual(menu._widgets, [f4, b2, f2, f3, b5, b1, b3, f1, b0, b4])
        f4.unpack(f2)
        self.assertEqual(menu._widgets, [f4, b2, f1, b0, b4, f2, f3, b5, b1, b3])
        menu.remove_widget(f4)
        self.assertIsNone(b2.get_frame())
        self.assertIsNone(f1.get_frame())
        self.assertEqual(b0.get_frame(), f1)
        self.assertEqual(b4.get_frame(), f1)
        self.assertEqual(menu._widgets, [f2, f3, b5, b1, b3, b2, f1, b0, b4])
        f3.pack(f1)
        self.assertEqual(menu._widgets, [f2, f3, b5, b1, f1, b0, b4, b3, b2])

        # Assert limits
        self.assertEqual(f1.get_indices(), (5, 6))
        self.assertEqual(f2.get_indices(), (1, 7))
        self.assertEqual(f3.get_indices(), (2, 4))
        self.assertEqual(f4.get_indices(), (-1, -1))

        f2.pack(b2)
        self.assertEqual(menu._widgets, [f2, f3, b5, b1, f1, b0, b4, b3, b2])
        self.assertEqual(f1.get_indices(), (5, 6))
        self.assertEqual(f2.get_indices(), (1, 8))
        self.assertEqual(f3.get_indices(), (2, 4))
        self.assertEqual(f4.get_indices(), (-1, -1))

        f2.pack(f3.unpack(f1))
        self.assertEqual(menu._widgets, [f2, f3, b5, b1, b3, b2, f1, b0, b4])
        f2.pack(f2.unpack(f3))
        self.assertEqual(menu._widgets, [f2, b3, b2, f1, b0, b4, f3, b5, b1])
        self.assertEqual(f1.get_indices(), (4, 5))
        self.assertEqual(f2.get_indices(), (1, 6))
        self.assertEqual(f3.get_indices(), (7, 8))

        # Unpack f3 and move to first
        f2.unpack(f3)
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [f3, b5, b1, f2, b3, b2, f1, b0, b4])
        self.assertEqual(f1.get_indices(), (7, 8))
        self.assertEqual(f2.get_indices(), (4, 6))
        self.assertEqual(f3.get_indices(), (1, 2))

        # Remove b5
        menu.remove_widget(b5)
        self.assertNotIn(b5, f1.get_widgets())
        self.assertEqual(b5.get_menu(), b5.get_frame())

        # Add again b5, this time this widget is not within menu
        f3.pack(b5)
        self.assertRaises(AssertionError, lambda: f3.pack(f4))
        self.assertIsNone(f4.get_menu())
        f3.pack(f2.unpack(b3))
        self.assertEqual(f3.get_widgets(unpack_subframes=False), (b1, b5, b3))
        menu.move_widget_index(b1, b3)
        self.assertEqual(f3.get_widgets(unpack_subframes=False), (b3, b1, b5))

        self.assertEqual(f2.get_indices(), (4, 5))
        self.assertEqual(f1.get_indices(), (6, 7))
        menu.remove_widget(b4)
        self.assertEqual(f2.get_indices(), (4, 5))
        self.assertEqual(f1.get_indices(), (6, 6))

        menu.move_widget_index(b3, b1)
        self.assertEqual(f3.get_widgets(unpack_subframes=False), (b1, b5, b3))
        self.assertRaises(AssertionError, lambda: menu.move_widget_index(b1, 5))
        self.assertRaises(AssertionError, lambda: menu.move_widget_index(b1, 1))
        menu.move_widget_index(b3, 1)
        f3.pack(b4)
        self.assertEqual(f3.get_widgets(unpack_subframes=False), (b3, b1, b5, b4))
        self.assertEqual(menu._widgets, [f3, b3, b1, f2, b2, f1, b0])

        # Sort two frames, considering non-menu widgets
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [f2, b2, f1, b0, f3, b3, b1])
        self.assertEqual(f3.get_widgets(unpack_subframes=False), (b3, b1, b5, b4))

        # Rollback
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [f3, b3, b1, f2, b2, f1, b0])

        # Add non-menu to last frame within frame
        f1.pack(f3.unpack(b4))
        self.assertEqual(f3.get_widgets(unpack_subframes=False), (b3, b1, b5))
        self.assertEqual(f1.get_widgets(unpack_subframes=False), (b0, b4))

        # Move again
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [f2, b2, f1, b0, f3, b3, b1])
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [f3, b3, b1, f2, b2, f1, b0])

        # Move, but 3 frame in same levels
        f2.unpack(f1)
        self.assertEqual(menu.get_selected_widget(), b0)
        menu.move_widget_index(f1, f3)
        self.assertEqual(menu._widgets, [f1, b0, f3, b3, b1, f2, b2])
        menu.move_widget_index(f2, f3)
        self.assertEqual(menu._widgets, [f1, b0, f2, b2, f3, b3, b1])
        menu.move_widget_index(f2, f3)
        self.assertEqual(menu._widgets, [f1, b0, f3, b3, b1, f2, b2])
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [f1, b0, f2, b2, f3, b3, b1])
        menu.move_widget_index(None)
        self.assertEqual(menu._widgets, [f3, b3, b1, f2, b2, f1, b0])
        self.assertEqual(menu.get_selected_widget(), b0)

        # Add really long nested frames
        frec = []
        n = 10
        for i in range(n):
            frec.append(menu.add.frame_v(100, 100, frame_id='frec{}'.format(i)))
            frec[i].relax()
            if i >= 1:
                frec[i - 1].pack(frec[i])

        # Check indices
        for i in range(n):
            self.assertEqual(frec[i].get_indices(), (-1, -1))
            self.assertEqual(frec[i].get_frame(), None if i == 0 else frec[i - 1])

        self.assertEqual(menu._widgets, [f3, b3, b1, f2, b2, f1, b0, *frec])

        # Test frame with none menu as first
        self.assertEqual(f1.get_widgets(), (b0, b4))
        f1.pack(f1.unpack(b0))
        self.assertEqual(f1.get_widgets(), (b4, b0))
        self.assertEqual(menu._widgets, [f3, b3, b1, f2, b2, f1, b0, *frec])

        # Move widgets
        menu.move_widget_index(f2, frec[0])
        self.assertEqual(menu._widgets, [f3, b3, b1, *frec, f2, b2, f1, b0])
        menu.move_widget_index(f3, frec[0])
        self.assertEqual(menu._widgets, [*frec, f3, b3, b1, f2, b2, f1, b0])
        menu.move_widget_index(f3, f2)
        self.assertEqual(menu._widgets, [*frec, f2, b2, f3, b3, b1, f1, b0])
        menu.move_widget_index(f3, frec[0])
        self.assertEqual(menu._widgets, [f3, b3, b1, *frec, f2, b2, f1, b0])

        # Add button to deepest frame
        frec[-1].pack(f3.unpack(b3))
        self.assertEqual(menu.get_selected_widget(), b0)
        for i in range(n):
            self.assertEqual(frec[i].get_indices(), (3 + i, 3 + i))
        menu.select_widget(b3)
        for w in [b1, b0, b2, b3]:
            menu._down()
            self.assertEqual(menu.get_selected_widget(), w)

        #  Unpack button from recursive
        f3.pack(frec[-1].unpack(b3))
        for i in range(n):
            self.assertEqual(frec[i].get_indices(), (-1, -1))
        for w in [b1, b0, b2, b3]:
            menu._down()
            self.assertEqual(menu.get_selected_widget(), w)
        for w in [b2, b0, b1, b3]:
            menu._up()
            self.assertEqual(menu.get_selected_widget(), w)

        menu._test_print_widgets()

    def test_scrollarea(self) -> None:
        """
        Test scrollarea frame.
        """
        menu = MenuUtils.generic_menu()
        self.assertRaises(AssertionError, lambda: menu.add.frame_v(300, 400, max_width=400))
        self.assertRaises(AssertionError, lambda: menu.add.frame_v(300, 400, max_height=500))
        self.assertRaises(AssertionError, lambda: menu.add.frame_v(300, 400, max_height=-1))
        img = pygame_menu.BaseImage(pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU)
        frame_sc = menu.add.frame_v(300, 400, max_height=200, background_color=img, frame_id='frame_sc')
        frame_scroll = frame_sc.get_scrollarea(inner=True)
        frame2 = menu.add.frame_v(400, 200, background_color=(30, 30, 30), padding=25)
        menu.add.frame_v(300, 200, background_color=(255, 255, 0))
        self.assertIsNone(menu.get_selected_widget())
        btn_frame21 = frame2.pack(menu.add.button('Button frame nosc'))
        btn_frame22 = frame2.pack(menu.add.button('Button frame nosc 2'))
        btn = frame_sc.pack(menu.add.button('Nice', lambda: print('Clicked'), padding=10))
        btn2 = frame_sc.pack(menu.add.button('Nice2', lambda: print('Clicked'), padding=10))
        btn3 = frame_sc.pack(menu.add.button('Nice3', lambda: print('Clicked'), padding=10))
        btn4 = frame_sc.pack(menu.add.button('Nice4', lambda: print('Clicked'), padding=10))
        btn5 = frame_sc.pack(menu.add.button('Nice5', lambda: print('Clicked'), padding=10))
        btn_real = menu.add.button('Normal button', lambda: print('Clicked'), background_color=(255, 0, 255))

        # First, test structure
        #   btn    \
        #   btn2   |
        #   btn3   | frame_sc scrollarea enabled
        #   btn4   |
        #   btn5   /
        #   btn_frame21 (x) \ frame2 no scrollarea <-- selected by default
        #   btn_frame22     /
        #   btn_real
        self.assertTrue(frame_sc.is_scrollable)
        self.assertFalse(frame2.is_scrollable)
        self.assertEqual(btn.get_frame(), frame_sc)
        self.assertEqual(btn2.get_frame(), frame_sc)
        self.assertEqual(btn.get_scrollarea(), frame_sc.get_scrollarea(inner=True))
        self.assertIsNone(btn_real.get_frame())
        self.assertEqual(btn_real.get_scrollarea(), menu.get_scrollarea())
        self.assertEqual(btn_frame21.get_frame(), frame2)
        self.assertEqual(btn_frame22.get_frame(), frame2)
        self.assertTrue(btn_frame21.is_selected())
        self.assertEqual(frame_scroll.get_parent(), menu.get_scrollarea())

        btn_frame21.active = True
        menu._mouse_motion_selection = True
        if PYGAME_V2:
            self.assertEqual(menu._draw_focus_widget(surface, btn_frame21),
                             {1: ((0, 0), (600, 0), (600, 165), (0, 165)),
                              2: ((0, 166), (124, 166), (124, 214), (0, 214)),
                              3: ((400, 166), (600, 166), (600, 214), (400, 214)),
                              4: ((0, 215), (600, 215), (600, 600), (0, 600))}
                             )
        else:
            self.assertEqual(menu._draw_focus_widget(surface, btn_frame21),
                             {1: ((0, 0), (600, 0), (600, 164), (0, 164)),
                              2: ((0, 165), (124, 165), (124, 214), (0, 214)),
                              3: ((400, 165), (600, 165), (600, 214), (400, 214)),
                              4: ((0, 215), (600, 215), (600, 600), (0, 600))}
                             )
        btn_frame21.active = False

        # Test scrollareas position
        vpos = 0.697
        vpos2 = 0.61
        vpos3 = 1
        vpos4 = 0.003
        if PYGAME_V2:
            self.assertEqual(menu.get_selected_widget(), btn_frame21)
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos)
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_HORIZONTAL), 0)
            self.assertEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            menu.update(PygameEventUtils.key(KEY_MOVE_UP, keydown=True))
            self.assertEqual(menu.get_selected_widget(), btn_frame22)
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos)
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_HORIZONTAL), 0)
            self.assertEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos4)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos2)
            self.assertEqual(menu.get_selected_widget(), btn5)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos4)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos2)
            self.assertEqual(menu.get_selected_widget(), btn4)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos4)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos2)
            self.assertEqual(menu.get_selected_widget(), btn3)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos4)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0.255)
            self.assertEqual(menu.get_selected_widget(), btn2)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos4)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            self.assertEqual(menu.get_selected_widget(), btn)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos3)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            self.assertEqual(menu.get_selected_widget(), btn_real)
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos4)
            self.assertAlmostEqual(frame_scroll.get_scroll_value_percentual(ORIENTATION_VERTICAL), vpos2)
            self.assertEqual(menu.get_selected_widget(), btn5)
        else:
            menu.select_widget(btn5)

        # Test active within scroll
        btn5.active = True
        if PYGAME_V2:
            self.assertEqual(menu._draw_focus_widget(surface, btn5),
                             {1: ((0, 0), (600, 0), (600, 276), (0, 276)),
                              2: ((0, 277), (147, 277), (147, 337), (0, 337)),
                              3: ((247, 277), (600, 277), (600, 337), (247, 337)),
                              4: ((0, 338), (600, 338), (600, 600), (0, 600))}
                             )
        else:
            self.assertEqual(menu._draw_focus_widget(surface, btn5),
                             {1: ((0, 0), (600, 0), (600, 275), (0, 275)),
                              2: ((0, 276), (147, 276), (147, 337), (0, 337)),
                              3: ((247, 276), (600, 276), (600, 337), (247, 337)),
                              4: ((0, 338), (600, 338), (600, 600), (0, 600))}
                             )
        btn5.active = False
        btn.select(update_menu=True)

        self.assertEqual(btn.get_rect(to_real_position=True), pygame.Rect(148, 155 if PYGAME_V2 else 156,
                                                                          82, 61 if PYGAME_V2 else 62))
        self.assertEqual(frame_scroll.get_absolute_view_rect(), pygame.Rect(148, 155 if PYGAME_V2 else 156, 284, 192))

        # Move inner scroll by 10%
        frame_scroll.scroll_to(ORIENTATION_VERTICAL, 0.1)
        self.assertEqual(frame_scroll.get_absolute_view_rect(), pygame.Rect(148, 155 if PYGAME_V2 else 156, 284, 192))
        self.assertEqual(btn.get_rect(to_real_position=True), pygame.Rect(148, 155 if PYGAME_V2 else 156,
                                                                          82, 41 if PYGAME_V2 else 42))

        # Move menu scroll by 10%
        menu.get_scrollarea().scroll_to(ORIENTATION_VERTICAL, 0.1)
        self.assertEqual(frame_scroll.get_absolute_view_rect(), pygame.Rect(148, 155, 284, 164))
        self.assertEqual(btn.get_rect(to_real_position=True), pygame.Rect(148, 155, 82, 13 if PYGAME_V2 else 14))

        # Move menu scroll by 50%
        menu.get_scrollarea().scroll_to(ORIENTATION_VERTICAL, 0.5)
        self.assertEqual(frame_scroll.get_absolute_view_rect(), pygame.Rect(148, 155, 284, 45))
        self.assertEqual(btn.get_rect(to_real_position=True), pygame.Rect(148, 155, 0, 0))

        menu.get_scrollarea().scroll_to(ORIENTATION_VERTICAL, 1)
        self.assertEqual(frame_scroll.get_absolute_view_rect(), pygame.Rect(0, 155, 0, 0))
        self.assertEqual(btn.get_rect(to_real_position=True), pygame.Rect(0, 155, 0, 0))

        menu.get_scrollarea().scroll_to(ORIENTATION_VERTICAL, 0)
        frame_scroll.scroll_to(ORIENTATION_VERTICAL, 0)
        self.assertEqual(btn.get_rect(to_real_position=True), pygame.Rect(148, 155 if PYGAME_V2 else 156,
                                                                          82, 61 if PYGAME_V2 else 62))
        self.assertEqual(frame_scroll.get_absolute_view_rect(), pygame.Rect(148, 155 if PYGAME_V2 else 156, 284, 192))

        # Remove btn
        menu.remove_widget(btn)
        self.assertFalse(btn.is_selected())
        self.assertIsNone(btn.get_menu())

        # Hide button 5
        btn5.hide()

        # Add textinput to frame
        # First, test structure
        #   btn2   \  <-- selected by default
        #   btn3   | frame_sc scrollarea enabled
        #   btn4   |
        #   btn5   |
        #   text   /
        #   btn_frame21 (x) \ frame2 no scrollarea
        #   btn_frame22     /
        #   btn_real
        text = frame_sc.pack(menu.add.text_input('text: '))
        self.assertEqual(text.get_position(), (8, 187 if PYGAME_V2 else 190))
        self.assertEqual(text.get_translate(virtual=True), (-148, 182 if PYGAME_V2 else 185))
        self.assertEqual(text.get_translate(), (0, 0))

        # Test text events within frame
        menu.select_widget(btn2)
        menu.select_widget(text)
        self.assertFalse(text.active)
        self.assertEqual(text.get_value(), '')
        menu.update(PygameEventUtils.key(pygame.K_a, char='a', keydown=True))
        self.assertTrue(text.active)
        self.assertEqual(text.get_value(), 'a')
        for i in range(10):
            menu.update(PygameEventUtils.key(pygame.K_a, char='a', keydown=True))
        menu.draw(surface)
        menu.update(PygameEventUtils.key(pygame.K_a, char='a', keydown=True))  # the last one to be added
        self.assertRaises(pygame_menu.widgets.widget.frame._FrameSizeException, lambda: menu.mainloop(surface))
        text.set_value('')
        self.assertTrue(text.active)
        menu.update(PygameEventUtils.key(pygame_menu.controls.KEY_APPLY, keydown=True))
        self.assertFalse(text.active)

        # Set widgets as floating
        #   btn4,text, btn2  \
        #   btn3             | frame_sc scrollarea enabled
        #   btn6             /
        #   btn_frame21 (x) \ frame2 no scrollarea
        #   btn_frame22     /
        #   btn_real
        btn4.set_float()
        text.set_float()
        btn6 = frame_sc.pack(menu.add.button('btn6'))
        if PYGAME_V2:
            self.assertEqual(menu._test_widgets_status(), (
                (('Frame',
                  (0, 0, 0, 148, 1, 304, 192, 148, 155, 148, 1),
                  (0, 0, 0, 1, 1, 0, 0),
                  (1, 6)),
                 ('Button-Nice2',
                  (0, 0, 1, 0, 0, 99, 61, 148, 155, 0, 154),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Button-Nice3',
                  (0, 0, 2, 0, 61, 99, 61, 148, 216, 0, 215),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Button-Nice4',
                  (0, 0, 3, 0, 0, 99, 61, 148, 155, 0, 154),
                  (1, 1, 0, 1, 0, 1, 1)),
                 ('Button-Nice5',
                  (-1, -1, 4, -158, 172, 99, 61, 148, 155, -158, 326),
                  (1, 0, 0, 0, 0, 1, 1)),
                 ('TextInput-text: ',
                  (0, 0, 5, 0, 0, 87, 49, 148, 155, 0, 154),
                  (1, 1, 1, 1, 0, 1, 1),
                  ''),
                 ('Button-btn6',
                  (0, 0, 6, 0, 122, 80, 49, 148, 277, 0, 276),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Frame',
                  (0, 1, 7, 100, 193, 400, 200, 100, 347, 100, 193),
                  (0, 0, 0, 1, 0, 0, 0),
                  (8, 9)),
                 ('Button-Button frame nosc',
                  (0, 1, 8, 125, 218, 275, 49, 125, 372, 125, 218),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Button-Button frame nosc 2',
                  (0, 1, 9, 125, 267, 300, 49, 125, 421, 125, 267),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Frame',
                  (0, 2, 10, 150, 393, 300, 200, 0, 155, 150, 393),
                  (0, 0, 0, 1, 0, 0, 0),
                  (-1, -1)),
                 ('Button-Normal button',
                  (0, 3, 11, 188, 593, 224, 49, 0, 155, 188, 593),
                  (1, 0, 0, 1, 0, 0, 0)))
            ))

        # Test widget unpacking within scrollarea
        self.assertEqual(btn6.get_scrollarea(), frame_sc.get_scrollarea(inner=True))
        frame_sc.unpack(btn6)
        self.assertEqual(btn6.get_scrollarea(), menu.get_scrollarea())

        # Translate widget within scrollarea
        btn3.translate(250, 100)
        menu.render()
        self.assertEqual(btn3.get_translate(), (250, 100))

        # Add another scrollarea within scrollarea
        w = frame_sc.clear()
        for v in w:
            menu.remove_widget(v)
        self.assertNotIn(btn6, w)
        menu.remove_widget(btn6)
        if PYGAME_V2:
            self.assertEqual(menu._test_widgets_status(), (
                (('Frame',
                  (0, 0, 0, 148, 1, 304, 192, 0, 155, 148, 1),
                  (0, 0, 0, 1, 1, 0, 0),
                  (-1, -1)),
                 ('Frame',
                  (0, 1, 1, 100, 193, 400, 200, 100, 155, 100, 193),
                  (0, 0, 0, 1, 0, 0, 0),
                  (2, 3)),
                 ('Button-Button frame nosc',
                  (0, 1, 2, 125, 218, 275, 49, 125, 169, 125, 218),
                  (1, 0, 1, 1, 0, 1, 1)),
                 ('Button-Button frame nosc 2',
                  (0, 1, 3, 125, 267, 300, 49, 125, 218, 125, 267),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Frame',
                  (0, 2, 4, 150, 393, 300, 200, 150, 344, 150, 393),
                  (0, 0, 0, 1, 0, 0, 0),
                  (-1, -1)),
                 ('Button-Normal button',
                  (0, 3, 5, 188, 593, 224, 49, 0, 155, 188, 593),
                  (1, 0, 0, 1, 0, 0, 0)))
            ))

        btn1 = frame_sc.pack(menu.add.button('btn1'))
        btn2 = frame_sc.pack(menu.add.button('btn2'))
        btn3 = pygame_menu.widgets.Button('btn3')
        menu.add.configure_defaults_widget(btn3)
        frame_sc.pack(btn3)
        frame_rnoscroll = menu.add.frame_v(150, 100, background_color=(160, 0, 60), frame_id='rno')
        btn4 = frame_rnoscroll.pack(menu.add.button('btn4', button_id='nice'))
        frame_rscroll = menu.add.frame_v(200, 500, max_height=100, background_color=(60, 60, 60), frame_id='r')
        frame_sc.pack(frame_rscroll)
        frame_sc.pack(frame_rnoscroll)
        bnice = menu.add.button('nice', font_color=(255, 255, 255))
        btn5 = frame_rscroll.pack(bnice)
        frame_sc.translate(-50, 0)

        # btn1                    \
        # btn2                    |
        # btn3                    | frame_sc, frame_scroll
        # btn5  > frame_rscroll   |
        # btn4  > frame_rnoscroll /
        # btn_frame21 (x) \ frame2 no scrollarea
        # btn_frame22     /
        # btn_real
        self.assertEqual(btn1.get_scrollarea(), frame_scroll)
        self.assertEqual(btn2.get_scrollarea(), frame_scroll)
        self.assertEqual(btn3.get_scrollarea(), frame_scroll)
        self.assertEqual(frame_rscroll.get_scrollarea(), frame_scroll)
        self.assertEqual(btn5.get_scrollarea().get_parent(), frame_scroll)
        self.assertEqual(frame_rnoscroll.get_scrollarea(), frame_scroll)
        self.assertEqual(btn5.get_scrollarea(), frame_rscroll.get_scrollarea(inner=True))
        self.assertEqual(btn4.get_scrollarea(), frame_scroll)
        self.assertEqual(frame_rscroll.get_size(), (204, 92))
        self.assertEqual(frame_sc.get_scrollarea(inner=True), frame_scroll)
        self.assertEqual(frame_rscroll.get_scrollarea(), frame_scroll)
        self.assertEqual(frame_rscroll.get_scrollarea(inner=True).get_parent(), frame_rscroll.get_scrollarea())

        # Normal frame with inner frames
        frame_out = menu.add.frame_v(400, 900, background_color=(0, 200, 0))
        nice1 = frame_out.pack(menu.add.button('Nice1'))
        frame_out_rnoscroll = menu.add.frame_v(150, 100, background_color=(160, 0, 60))
        nice2 = frame_out_rnoscroll.pack(menu.add.button('Nice2'))
        frame_out_rnoscroll2 = menu.add.frame_v(150, 100, background_color=(20, 50, 140))
        nice3 = frame_out_rnoscroll2.pack(menu.add.button('Nice3'))
        frame_out_rnoscroll_rscroll = menu.add.frame_v(200, 500, max_height=100, background_color=(60, 60, 60))
        nice4 = frame_out_rnoscroll_rscroll.pack(menu.add.button('Nice4'))
        frame_out.pack(frame_out_rnoscroll)
        frame_out.pack(frame_out_rnoscroll2)
        frame_out.pack(frame_out_rnoscroll_rscroll)
        self.assertEqual(nice2.get_scrollarea(), menu.get_scrollarea())

        self.assertIn(nice1, frame_out.get_widgets())
        self.assertIn(nice3, frame_out.get_widgets())
        self.assertIn(nice4, frame_out.get_widgets())

        # frame_sc.translate(-50, 0)

        def drawrect() -> None:
            """
            Draw absolute rect on surface for testing purposes.
            """
            # surface.fill((160, 0, 0), frame_scroll.get_absolute_view_rect())
            # surface.fill((60, 0, 60), btn.get_scrollarea().to_real_position(btn.get_rect(), visible=True))
            # surface.fill((255, 255, 255), btn.get_rect(to_real_position=True))
            # surface.fill((255, 0, 0), frame_rscroll.get_scrollarea(inner=True).get_absolute_view_rect())
            # surface.fill((0, 255, 0), nice4.get_rect(to_real_position=True))
            # surface.fill((0, 255, 255), btn4.get_rect(to_real_position=True))
            return

        menu.get_decorator().add_callable(drawrect, prev=False, pass_args=False)

        # Scroll down each subelement
        frame_sc.scrollh(1)
        frame_sc.scrollv(1)
        frame_rscroll.scrollv(1)
        frame_out_rnoscroll_rscroll.scrollv(1)
        menu.select_widget(btn_real)

        if PYGAME_V2:
            for v in [0.301, 0.347, 0.427, 0.543, 0.003, 0.003, 0.003, 0.003, 0.003, 0.003, 0.255]:
                menu._up()
                self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), v)
        self.assertEqual(menu.get_selected_widget(), btn_real)

        frame_sc.scrollh(1)
        frame_sc.scrollv(1)
        frame_rscroll.scrollv(1)
        frame_out_rnoscroll_rscroll.scrollv(1)

        # Now up
        if PYGAME_V2:
            for v in [0.213, 0.175, 0.003, 0.003, 0.003, 0.003, 0.543, 0.543, 0.543, 0.532, 0.487]:
                menu._down()
                self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), v)
        self.assertEqual(menu.get_selected_widget(), btn_real)

        # Select two widgets
        btn_frame21.select()
        menu._test_print_widgets()

        # Check selection
        self.assertRaises(pygame_menu.menu._MenuMultipleSelectedWidgetsException, lambda: menu.render())
        menu.render()
        self.assertEqual(menu.get_selected_widget(), btn_frame21)

    def test_scrollarea_frame_within_scrollarea(self) -> None:
        """
        Test scrollarea frame within scrollareas.
        """
        menu = MenuUtils.generic_menu()
        f1 = menu.add.frame_v(450, 400, background_color=(0, 0, 255), frame_id='f1')
        f2 = menu.add.frame_v(400, 400, max_height=300, background_color=(255, 0, 0), frame_id='f2')
        f3 = menu.add.frame_v(350, 400, max_height=200, background_color=(0, 255, 0), frame_id='f3')
        f4 = menu.add.frame_v(300, 400, max_height=100, background_color=(0, 255, 255), frame_id='f4')

        f4._pack_margin_warning = False

        # Get scrollareas
        s0 = menu.get_scrollarea()
        s1 = f2.get_scrollarea(inner=True)
        s2 = f3.get_scrollarea(inner=True)
        s3 = f4.get_scrollarea(inner=True)

        vm = f2.pack(menu.add.vertical_margin(25, margin_id='margin'))
        b1 = f1.pack(menu.add.button('btn1', button_id='b1'), margin=(25, 0))
        b2 = f2.pack(menu.add.button('btn2', button_id='b2'), margin=(25, 0))
        b3 = f3.pack(menu.add.button('btn3', button_id='b3'), margin=(25, 0))
        b4 = f4.pack(menu.add.button('btn4', button_id='b4'), margin=(25, 0))

        # Pack frames
        f1.pack(f2)
        f2.pack(f3)
        f3.pack(f4)

        # Add last button
        b5 = menu.add.button('btn5', button_id='b5')

        # Test positioning
        #
        # .------------f1-----------.
        # | btn1                 s0 |
        # | .----------f2---------. |
        # | | <25px>           s1 ^ |
        # | | btn2                | |
        # | | .--------f3-------. | |
        # | | | btn3         s2 ^ | |
        # | | | .------f4-----. | | |
        # | | | | btn4     s3 ^ | | |
        # | | | |             v | | |
        # | | | .-------------. v | |
        # | | .-----------------. v |
        # | .---------------------. |
        # .-------------------------.
        # btn5
        self.assertEqual(b1.get_frame_depth(), 1)
        self.assertEqual(b2.get_frame_depth(), 2)
        self.assertEqual(b3.get_frame_depth(), 3)
        self.assertEqual(b4.get_frame_depth(), 4)
        self.assertEqual(b5.get_frame_depth(), 0)

        self.assertEqual(menu._scrollable_frames, [f4, f3, f2])

        self.assertFalse(f1.is_scrollable)
        self.assertTrue(f2.is_scrollable)
        self.assertTrue(f3.is_scrollable)
        self.assertTrue(f4.is_scrollable)

        self.assertIsNone(s0.get_parent())
        self.assertEqual(f1.get_scrollarea(), s0)
        self.assertEqual(f2.get_scrollarea(), s0)
        self.assertEqual(f3.get_scrollarea(), s1)
        self.assertEqual(f4.get_scrollarea(), s2)

        self.assertEqual(s0.get_depth(), 0)
        self.assertEqual(s1.get_depth(), 1)
        self.assertEqual(s2.get_depth(), 2)
        self.assertEqual(s3.get_depth(), 3)

        if PYGAME_V2:
            self.assertEqual(s0.get_absolute_view_rect(), pygame.Rect(0, 155, 580, 345))
            self.assertEqual(s1.get_absolute_view_rect(), pygame.Rect(83, 209, 384, 291))
            self.assertEqual(s2.get_absolute_view_rect(), pygame.Rect(83, 283, 334, 192))
            self.assertEqual(s3.get_absolute_view_rect(), pygame.Rect(83, 332, 284, 92))

            self.assertEqual(s0.get_parent_position(), (0, 0))
            self.assertEqual(s1.get_parent_position(), (0, 155))
            self.assertEqual(s2.get_parent_position(), (83, 209))
            self.assertEqual(s3.get_parent_position(), (83, 283))

        def drawrect() -> None:
            """
            Draw absolute rect on surface for testing purposes.
            """
            # surface.fill((0, 0, 0), s3.get_absolute_view_rect())
            return

        menu.get_decorator().add_callable(drawrect, prev=False, pass_args=False)

        self.assertEqual(menu.get_selected_widget(), b1)
        self.assertEqual(f1.get_indices(), (1, 2))
        self.assertEqual(f2.get_indices(), (4, 5))
        self.assertEqual(f3.get_indices(), (6, 7))
        self.assertEqual(f4.get_indices(), (8, 8))

        # Scroll all to bottom, test movement
        f2.scrollv(1)
        f3.scrollv(1)
        f4.scrollv(1)
        if PYGAME_V2:
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            menu._down()
            self.assertEqual(menu.get_selected_widget(), b5)
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), 0.99)
            self.assertAlmostEqual(f2.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0.99)
            self.assertAlmostEqual(f3.get_scroll_value_percentual(ORIENTATION_VERTICAL), 1)
            self.assertAlmostEqual(f4.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0.993)
            menu._down()
            self.assertEqual(menu.get_selected_widget(), b4)
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            self.assertAlmostEqual(f2.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            self.assertAlmostEqual(f3.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            self.assertAlmostEqual(f3.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
            self.assertEqual(menu._test_widgets_status(), (
                (('Frame',
                  (0, 0, 0, 75, 1, 450, 400, 75, 156, 75, 1),
                  (0, 0, 0, 1, 0, 0, 0),
                  (1, 2)),
                 ('Button-btn1',
                  (0, 0, 1, 108, 5, 80, 49, 108, 160, 108, 5),
                  (1, 0, 0, 1, 0, 1, 1)),
                 ('Frame',
                  (0, 0, 2, 83, 54, 404, 292, 83, 209, 83, 54),
                  (0, 0, 0, 1, 1, 1, 1),
                  (4, 5)),
                 ('VMargin', (0, 0, 3, 0, 0, 0, 25, 0, 0, 0, 0), (0, 0, 0, 1, 0, 1, 2)),
                 ('Button-btn2',
                  (0, 0, 4, 25, 25, 80, 49, 108, 234, 25, 180),
                  (1, 0, 0, 1, 0, 1, 2)),
                 ('Frame',
                  (0, 0, 5, 0, 74, 354, 192, 83, 283, 0, 229),
                  (0, 0, 0, 1, 1, 1, 2),
                  (6, 7)),
                 ('Button-btn3',
                  (0, 0, 6, 25, 0, 80, 49, 108, 283, 108, 209),
                  (1, 0, 0, 1, 0, 1, 3)),
                 ('Frame',
                  (0, 0, 7, 0, 49, 304, 92, 83, 332, 83, 258),
                  (0, 0, 0, 1, 1, 1, 3),
                  (8, 8)),
                 ('Button-btn4',
                  (0, 0, 8, 25, 0, 80, 49, 108, 332, 108, 283),
                  (1, 0, 1, 1, 0, 1, 4)),
                 ('Button-btn5',
                  (0, 1, 9, 260, 401, 80, 49, 0, 155, 260, 401),
                  (1, 0, 0, 1, 0, 0, 0)))
            ))

        def check_all_visible() -> None:
            """
            Check all widgets are visible.
            """
            self.assertTrue(f1.is_visible())
            self.assertTrue(b1.is_visible())
            self.assertTrue(b1.is_visible(check_frame=False))
            self.assertTrue(f2.is_visible())
            self.assertTrue(b2.is_visible())
            self.assertTrue(b2.is_visible(check_frame=False))
            self.assertTrue(f3.is_visible())
            self.assertTrue(b3.is_visible())
            self.assertTrue(b3.is_visible(check_frame=False))
            self.assertTrue(f4.is_visible())
            self.assertTrue(b4.is_visible())
            self.assertTrue(b4.is_visible(check_frame=False))
            self.assertTrue(b5.is_visible())
            self.assertTrue(b5.is_visible(check_frame=False))

        # Test hide
        f1.hide()
        self.assertEqual(menu.get_selected_widget(), b5)
        self.assertFalse(f1.is_visible())
        self.assertFalse(b1.is_visible())
        self.assertTrue(b1.is_visible(check_frame=False))
        self.assertFalse(f2.is_visible())
        self.assertFalse(b2.is_visible())
        self.assertFalse(f3.is_visible())
        self.assertFalse(b3.is_visible())
        self.assertFalse(f4.is_visible())
        self.assertFalse(b4.is_visible())
        self.assertTrue(b5.is_visible())

        f1.show()
        self.assertEqual(menu.get_selected_widget(), b5)
        check_all_visible()

        f2.hide()
        self.assertTrue(f1.is_visible())
        self.assertTrue(b1.is_visible())
        self.assertFalse(f2.is_visible())
        self.assertFalse(b2.is_visible())
        self.assertFalse(f3.is_visible())
        self.assertFalse(b3.is_visible())
        self.assertFalse(f4.is_visible())
        self.assertFalse(b4.is_visible())
        self.assertTrue(b5.is_visible())

        f2.show()
        check_all_visible()
        f3.hide()
        self.assertTrue(f1.is_visible())
        self.assertTrue(b1.is_visible())
        self.assertTrue(f2.is_visible())
        self.assertTrue(b2.is_visible())
        self.assertFalse(f3.is_visible())
        self.assertFalse(b3.is_visible())
        self.assertFalse(f4.is_visible())
        self.assertFalse(b4.is_visible())
        self.assertTrue(b5.is_visible())

        f3.show()
        check_all_visible()
        f4.hide()
        self.assertTrue(f1.is_visible())
        self.assertTrue(b1.is_visible())
        self.assertTrue(f2.is_visible())
        self.assertTrue(b2.is_visible())
        self.assertTrue(f3.is_visible())
        self.assertTrue(b3.is_visible())
        self.assertFalse(f4.is_visible())
        self.assertFalse(b4.is_visible())
        self.assertTrue(b5.is_visible())

        f4.show()
        check_all_visible()
        menu.get_scrollarea().scroll_to(ORIENTATION_VERTICAL, 0.562)

        # Move widgets
        menu.select_widget(b4)
        self.assertEqual(menu.get_selected_widget(), b4)
        self.assertEqual(menu.get_widgets(), (f1, b1, f2, vm, b2, f3, b3, f4, b4, b5))
        menu.move_widget_index(f1, b5)
        self.assertEqual(menu.get_selected_widget(), b4)
        self.assertEqual(menu.get_widgets(), (b5, f1, b1, f2, vm, b2, f3, b3, f4, b4))

        # Test scroll on up
        f3.scrollv(0)
        menu._down()
        self.assertEqual(menu.get_selected_widget(), b3)
        self.assertAlmostEqual(f3.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
        if PYGAME_V2:
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), 0.562)

        f2.scrollv(0)
        menu._down()
        self.assertEqual(menu.get_selected_widget(), b2)
        self.assertAlmostEqual(f2.get_scroll_value_percentual(ORIENTATION_VERTICAL), 0)
        if PYGAME_V2:
            self.assertAlmostEqual(menu.get_scrollarea().get_scroll_value_percentual(ORIENTATION_VERTICAL), 0.562)
        menu._down()
        menu._down()
        self.assertEqual(menu.get_selected_widget(), b5)

        # Check all widgets are non floating
        for w in menu.get_widgets():
            self.assertFalse(w.is_floating())

        # Pack all widgets within deepest frame
        f4.unpack(b4)
        self.assertRaises(AssertionError, lambda: f4.pack(f1.unpack(f1)))
        f4.pack(f1.unpack(b1))
        menu.remove_widget(vm)
        self.assertNotIn(vm, f2.get_widgets())
        f4.pack(f2.unpack(b2))
        f4.pack(f3.unpack(b3))
        f4.pack(b4)
        f4.pack(b5)
        b5.set_float()
        f4w = f4.get_widgets()
        for w in f4w:
            self.assertTrue(w.is_floating())
            self.assertEqual(w.get_position(), f4w[0].get_position())
        self.assertEqual(menu.get_selected_widget(), b5)
        self.assertEqual(f4.get_widgets(), (b1, b2, b3, b4, b5))

        # Unfloat widgets
        f4.unfloat()
        menu.select_widget(b1)
        for w in [b5, b4, b3, b2, b1]:
            menu._down()
            self.assertEqual(menu.get_selected_widget(), w)

        for w in [b2, b3, b4, b5, b1]:
            menu._up()
            self.assertEqual(menu.get_selected_widget(), w)

        menu._test_print_widgets()

        # Remove f4 from menu
        menu.remove_widget(f4)
        self.assertEqual(menu._scrollable_frames, [f3, f2])

    def test_menu_support(self) -> None:
        """
        Test frame menu support.
        """
        # Test frame movement
        theme = TEST_THEME.copy()
        theme.widget_margin = (0, 0)
        theme.widget_font_size = 20
        menu = MenuUtils.generic_menu(columns=3, rows=2, theme=theme)

        # btn0 | f1(btn2,btn3,btn4,btn5) | f2(btn7,
        #      |                         |    btn8,
        #      |                         |    f3(btn9,btn10))
        # btn1 |           btn6          | f4(btn11,btn12,btn13)
        btn0 = menu.add.button('btn0')
        btn1 = menu.add.button('btn1')
        f1 = menu.add.frame_h(200, 50, frame_id='f1')
        btn2 = menu.add.button('btn2 ')
        btn3 = menu.add.button('btn3 ')
        btn4 = menu.add.button('btn4 ')
        btn5 = menu.add.button('btn5 ')
        btn6 = menu.add.button('btn6')
        f2 = menu.add.frame_v(200, 132, background_color=(100, 0, 0), frame_id='f2')
        f3 = menu.add.frame_h(200, 50, background_color=(0, 0, 100), frame_id='f3')
        f4 = menu.add.frame_h(260, 50, frame_id='f4')
        btn7 = menu.add.button('btn7')
        btn8 = menu.add.button('btn8')
        btn9 = menu.add.button('btn9 ')
        btn10 = menu.add.button('btn10')
        btn11 = menu.add.button('btn11 ')
        btn12 = menu.add.button('btn12 ')
        btn13 = menu.add.button('btn13')
        f1.pack((btn2, btn3, btn4, btn5))
        f3.pack((btn9, btn10))
        f2.pack((btn7, btn8, f3), alignment=pygame_menu.locals.ALIGN_CENTER)
        f4.pack((btn11, btn12, btn13))

        menu._test_print_widgets()

        # Test min max indices
        self.assertEqual(f1.get_indices(), (3, 6))
        self.assertEqual(f2.get_indices(), (9, 11))
        self.assertEqual(f3.get_indices(), (12, 13))
        self.assertEqual(f4.get_indices(), (15, 17))

        # Check positioning
        self.assertEqual(btn0.get_col_row_index(), (0, 0, 0))
        self.assertEqual(btn1.get_col_row_index(), (0, 1, 1))
        self.assertEqual(f1.get_col_row_index(), (1, 0, 2))
        self.assertEqual(btn6.get_col_row_index(), (1, 1, 7))
        self.assertEqual(f2.get_col_row_index(), (2, 0, 8))
        self.assertEqual(f4.get_col_row_index(), (2, 1, 14))

        self.assertFalse(f1.is_scrollable)
        self.assertFalse(f2.is_scrollable)
        self.assertFalse(f3.is_scrollable)
        self.assertEqual(menu._test_widgets_status(), (
            (('Button-btn0',
              (0, 0, 0, 13, 82, 42, 28, 13, 237, 13, 82),
              (1, 0, 1, 1, 0, 0, 0)),
             ('Button-btn1',
              (0, 1, 1, 13, 110, 42, 28, 13, 265, 13, 110),
              (1, 0, 0, 1, 0, 0, 0)),
             ('Frame',
              (1, 0, 2, 84, 82, 200, 50, 84, 237, 84, 82),
              (0, 0, 0, 1, 0, 0, 0),
              (3, 6)),
             ('Button-btn2 ',
              (1, 0, 3, 84, 82, 47, 28, 84, 237, 84, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn3 ',
              (1, 0, 4, 131, 82, 47, 28, 131, 237, 131, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn4 ',
              (1, 0, 5, 178, 82, 47, 28, 178, 237, 178, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn5 ',
              (1, 0, 6, 225, 82, 47, 28, 225, 237, 225, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn6',
              (1, 1, 7, 163, 132, 42, 28, 163, 287, 163, 132),
              (1, 0, 0, 1, 0, 0, 0)),
             ('Frame',
              (2, 0, 8, 351, 82, 200, 132, 351, 237, 351, 82),
              (0, 0, 0, 1, 0, 0, 0),
              (9, 11)),
             ('Button-btn7',
              (2, 0, 9, 430, 82, 42, 28, 430, 237, 430, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn8',
              (2, 0, 10, 430, 110, 42, 28, 430, 265, 430, 110),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Frame',
              (2, 0, 11, 351, 138, 200, 50, 351, 293, 351, 138),
              (0, 0, 0, 1, 0, 1, 1),
              (12, 13)),
             ('Button-btn9 ',
              (2, 0, 12, 351, 138, 47, 28, 351, 293, 351, 138),
              (1, 0, 0, 1, 0, 1, 2)),
             ('Button-btn10',
              (2, 0, 13, 398, 138, 53, 28, 398, 293, 398, 138),
              (1, 0, 0, 1, 0, 1, 2)),
             ('Frame',
              (2, 1, 14, 321, 214, 260, 50, 321, 369, 321, 214),
              (0, 0, 0, 1, 0, 0, 0),
              (15, 17)),
             ('Button-btn11 ',
              (2, 1, 15, 321, 214, 58, 28, 321, 369, 321, 214),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn12 ',
              (2, 1, 16, 379, 214, 58, 28, 379, 369, 379, 214),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn13',
              (2, 1, 17, 437, 214, 53, 28, 437, 369, 437, 214),
              (1, 0, 0, 1, 0, 1, 1)))
        ))

        # Arrow keys
        self.assertEqual(menu.get_selected_widget(), btn0)
        menu.update(PygameEventUtils.key(KEY_RIGHT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn2)
        menu.update(PygameEventUtils.key(KEY_RIGHT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn3)
        menu.update(PygameEventUtils.key(KEY_RIGHT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn4)
        menu.update(PygameEventUtils.key(KEY_RIGHT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn5)
        menu.update(PygameEventUtils.key(KEY_RIGHT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn7)
        menu.update(PygameEventUtils.key(KEY_RIGHT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn0)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn10)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn9)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn5)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn4)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn3)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn2)
        menu.update(PygameEventUtils.key(KEY_LEFT, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn0)
        for bt in (btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn0, btn1):
            menu.update(PygameEventUtils.key(KEY_MOVE_UP, keydown=True))
            self.assertEqual(menu.get_selected_widget(), bt)
        for bt in (btn6, btn11, btn12, btn13, btn1):
            menu.update(PygameEventUtils.joy_key(JOY_RIGHT))
            self.assertEqual(menu.get_selected_widget(), bt)
        for bt in (btn0, btn13, btn12, btn11, btn10, btn9, btn8, btn7, btn6, btn5, btn4, btn3, btn2, btn1, btn0):
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
            self.assertEqual(menu.get_selected_widget(), bt)
        menu.update(PygameEventUtils.key(KEY_MOVE_UP, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn1)
        for bt in (btn13, btn12, btn11, btn6, btn1):
            menu.update(PygameEventUtils.joy_key(JOY_LEFT))
            self.assertEqual(menu.get_selected_widget(), bt)

        # Check mouse events
        for bt in (btn0, btn13, btn12, btn11, btn10, btn9, btn8, btn7, btn6, btn5, btn4, btn3, btn2, btn1, btn0):
            menu.update(PygameEventUtils.middle_rect_click(bt, evtype=pygame.MOUSEBUTTONDOWN))
            self.assertEqual(menu.get_selected_widget(), bt)

        # btn0 | f1(btn2,btn3,btn4,btn5) | f2(btn7,
        #      |                         |    btn8)
        # btn1 |            btn6         | f4(btn11,btn12,btn13)+(floating9,10)
        menu.select_widget(btn0)
        self.assertEqual(len(f2._widgets), 3)
        self.assertEqual(len(f3._widgets), 2)
        menu.remove_widget(f3)
        self.assertEqual(len(f2._widgets), 2)
        self.assertEqual(len(f3._widgets), 0)
        self.assertEqual(menu._test_widgets_status(), (
            (('Button-btn0',
              (0, 0, 0, 13, 82, 42, 28, 13, 237, 13, 82),
              (1, 0, 1, 1, 0, 0, 0)),
             ('Button-btn1',
              (0, 1, 1, 13, 110, 42, 28, 13, 265, 13, 110),
              (1, 0, 0, 1, 0, 0, 0)),
             ('Frame',
              (1, 0, 2, 84, 82, 200, 50, 84, 237, 84, 82),
              (0, 0, 0, 1, 0, 0, 0),
              (3, 6)),
             ('Button-btn2 ',
              (1, 0, 3, 84, 82, 47, 28, 84, 237, 84, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn3 ',
              (1, 0, 4, 131, 82, 47, 28, 131, 237, 131, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn4 ',
              (1, 0, 5, 178, 82, 47, 28, 178, 237, 178, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn5 ',
              (1, 0, 6, 225, 82, 47, 28, 225, 237, 225, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn6',
              (1, 1, 7, 163, 132, 42, 28, 163, 287, 163, 132),
              (1, 0, 0, 1, 0, 0, 0)),
             ('Frame',
              (2, 0, 8, 351, 82, 200, 132, 351, 237, 351, 82),
              (0, 0, 0, 1, 0, 0, 0),
              (9, 10)),
             ('Button-btn7',
              (2, 0, 9, 430, 82, 42, 28, 430, 237, 430, 82),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn8',
              (2, 0, 10, 430, 110, 42, 28, 430, 265, 430, 110),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Frame',
              (2, 1, 11, 321, 214, 260, 50, 321, 369, 321, 214),
              (0, 0, 0, 1, 0, 0, 0),
              (12, 14)),
             ('Button-btn11 ',
              (2, 1, 12, 321, 214, 58, 28, 321, 369, 321, 214),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn12 ',
              (2, 1, 13, 379, 214, 58, 28, 379, 369, 379, 214),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn13',
              (2, 1, 14, 437, 214, 53, 28, 437, 369, 437, 214),
              (1, 0, 0, 1, 0, 1, 1)),
             ('Button-btn9 ',
              (2, 0, 15, 427, 82, 47, 28, 427, 237, 427, 82),
              (1, 1, 0, 1, 0, 0, 0)),
             ('Button-btn10',
              (2, 0, 16, 424, 82, 53, 28, 424, 237, 424, 82),
              (1, 1, 0, 1, 0, 0, 0)))
        ))

        menu.select_widget(btn0)
        for i in range(14):
            menu.update(PygameEventUtils.key(KEY_MOVE_UP, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn0)
        for i in range(14):
            menu.update(PygameEventUtils.key(KEY_MOVE_DOWN, keydown=True))
        self.assertEqual(menu.get_selected_widget(), btn0)

    def test_mouseover(self) -> None:
        """
        Test frame mouse support.
        """
        menu = MenuUtils.generic_menu()
        reset_widgets_over()
        self.assertEqual(WIDGET_MOUSEOVER, [None, []])

        f1 = menu.add.frame_v(500, 500, background_color='red',
                              cursor=pygame_menu.locals.CURSOR_HAND, frame_id='f1')
        menu.add.vertical_margin(100, margin_id='vbottom')
        f1.pack(menu.add.vertical_margin(100, margin_id='vtop'))

        f2 = menu.add.frame_v(400, 300, background_color='blue',
                              cursor=pygame_menu.locals.CURSOR_HAND, frame_id='f2')
        b1 = f1.pack(menu.add.button('1', button_id='b1', cursor=pygame_menu.locals.CURSOR_ARROW))
        f1.pack(f2)
        b2 = f2.pack(menu.add.button('2', button_id='b2', cursor=pygame_menu.locals.CURSOR_ARROW))

        f3 = f2.pack(menu.add.frame_v(100, 100, background_color='green',
                                      cursor=pygame_menu.locals.CURSOR_HAND, frame_id='f3'))
        b3 = f3.pack(menu.add.button('3', button_id='b3', cursor=pygame_menu.locals.CURSOR_ARROW))

        f1._id__repr__ = True
        f2._id__repr__ = True
        f3._id__repr__ = True

        # Get cursors
        cur_none = pygame.mouse.get_cursor()
        if PYGAME_V2:
            pygame.mouse.set_cursor(pygame_menu.locals.CURSOR_ARROW)
        cur_arrow = pygame.mouse.get_cursor()
        if PYGAME_V2:
            pygame.mouse.set_cursor(pygame_menu.locals.CURSOR_HAND)
        cur_hand = pygame.mouse.get_cursor()
        if PYGAME_V2:
            pygame.mouse.set_cursor(cur_none)

        if PYGAME_V2:
            self.assertEqual(menu._test_widgets_status(), (
                (('Frame',
                  (0, 0, 0, 50, 1, 500, 500, 50, 155, 50, 1),
                  (0, 0, 0, 1, 0, 0, 0),
                  (2, 3)),
                 ('VMargin', (0, 0, 1, 0, 0, 0, 100, 0, 0, 0, 0), (0, 0, 0, 1, 0, 1, 1)),
                 ('Button-1',
                  (0, 0, 2, 58, 105, 33, 49, 58, 197, 58, 105),
                  (1, 0, 1, 1, 0, 1, 1)),
                 ('Frame',
                  (0, 0, 3, 58, 154, 400, 300, 58, 246, 58, 154),
                  (0, 0, 0, 1, 0, 1, 1),
                  (4, 5)),
                 ('Button-2',
                  (0, 0, 4, 66, 158, 33, 49, 66, 250, 66, 158),
                  (1, 0, 0, 1, 0, 1, 2)),
                 ('Frame',
                  (0, 0, 5, 66, 207, 100, 100, 66, 299, 66, 207),
                  (0, 0, 0, 1, 0, 1, 2),
                  (6, 6)),
                 ('Button-3',
                  (0, 0, 6, 74, 211, 33, 49, 74, 303, 74, 211),
                  (1, 0, 0, 1, 0, 1, 3)),
                 ('VMargin', (0, 1, 7, 0, 0, 0, 100, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0)))
            ))

        # Setup
        self.assertTrue(b1.is_selected())
        self.assertFalse(menu._mouse_motion_selection)
        menu._test_print_widgets()

        test = [False, False, False, False, False, False]  # f1, b1, f2, b2, f3, b3
        print_events = True

        def onf1(widget, _) -> None:
            """
            f1 event.
            """
            self.assertEqual(widget, f1)
            test[0] = not test[0]
            if print_events:
                print('{0} f1'.format('Enter' if test[0] else 'Leave'))

        def onb1(widget, _) -> None:
            """
            b1 event.
            """
            self.assertEqual(widget, b1)
            test[1] = not test[1]
            if print_events:
                print('{0} b1'.format('Enter' if test[1] else 'Leave'))

        def onf2(widget, _) -> None:
            """
            f2 event.
            """
            self.assertEqual(widget, f2)
            test[2] = not test[2]
            if print_events:
                print('{0} f2'.format('Enter' if test[2] else 'Leave'))

        def onb2(widget, _) -> None:
            """
            b2 event.
            """
            self.assertEqual(widget, b2)
            test[3] = not test[3]
            if print_events:
                print('{0} b2'.format('Enter' if test[3] else 'Leave'))

        def onf3(widget, _) -> None:
            """
            f3 event.
            """
            self.assertEqual(widget, f3)
            test[4] = not test[4]
            if print_events:
                print('{0} f3'.format('Enter' if test[4] else 'Leave'))

        def onb3(widget, _) -> None:
            """
            b3 event.
            """
            self.assertEqual(widget, b3)
            test[5] = not test[5]
            if print_events:
                print('{0} b3'.format('Enter' if test[5] else 'Leave'))

        f1.set_onmouseover(onf1)
        f1.set_onmouseleave(onf1)
        b1.set_onmouseover(onb1)
        b1.set_onmouseleave(onb1)

        f2.set_onmouseover(onf2)
        f2.set_onmouseleave(onf2)
        b2.set_onmouseover(onb2)
        b2.set_onmouseleave(onb2)

        f3.set_onmouseover(onf3)
        f3.set_onmouseleave(onf3)
        b3.set_onmouseover(onb3)
        b3.set_onmouseleave(onb3)

        # Start moving mouse
        #
        # .------------f1-----------.
        # | vop <100px>             |
        # | b1                      |
        # | .----------f2---------. |
        # | | b2                  | |
        # | | .--------f3-------. | |
        # | | | b3              | | |
        # | | .-----------------. | |
        # | .---------------------. |
        # .-------------------------.
        # vbottom <100px>
        self.assertEqual(pygame.mouse.get_cursor(), cur_none)
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(f1))
        self.assertEqual(test, [True, False, False, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [f1, [f1, cur_none, []]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_hand)

        # Move to b1 inside f1
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b1))
        self.assertEqual(test, [True, True, False, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [b1, [b1, cur_hand, [f1, cur_none, []]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

        # Move to f2, inside f1
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(f2))
        self.assertEqual(test, [True, False, True, False, False, False])  # out from b1
        self.assertEqual(WIDGET_MOUSEOVER, [f2, [f2, cur_hand, [f1, cur_none, []]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_hand)

        # Move to b2, inside f2+f1
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b2))
        self.assertEqual(test, [True, False, True, True, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [b2, [b2, cur_hand, [f2, cur_hand, [f1, cur_none, []]]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

        # Move to f3
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(f3))
        self.assertEqual(test, [True, False, True, False, True, False])  # out from b2
        self.assertEqual(WIDGET_MOUSEOVER, [f3, [f3, cur_hand, [f2, cur_hand, [f1, cur_none, []]]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_hand)

        # Move to b3, inside f3+f2+f1
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b3))
        self.assertEqual(test, [True, False, True, False, True, True])
        self.assertEqual(WIDGET_MOUSEOVER, [b3, [b3, cur_hand, [f3, cur_hand, [f2, cur_hand, [f1, cur_none, []]]]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

        # From b3, move mouse out from window
        menu.update(PygameEventUtils.leave_window())
        self.assertEqual(test, [False, False, False, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [None, []])
        self.assertEqual(pygame.mouse.get_cursor(), cur_none)

        # Move from out to inner widget (b3), this should call f1->f2->f3->b3
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b3))
        self.assertEqual(test, [True, False, True, False, True, True])
        self.assertEqual(WIDGET_MOUSEOVER, [b3, [b3, cur_hand, [f3, cur_hand, [f2, cur_hand, [f1, cur_none, []]]]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

        # Move from b3->f2, this should call b3, f3 but not call f2 as this is actually over
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(f2))
        self.assertEqual(test, [True, False, True, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [f2, [f2, cur_hand, [f1, cur_none, []]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_hand)

        # Move from f2->b1, this should call f2
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b1))
        self.assertEqual(test, [True, True, False, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [b1, [b1, cur_hand, [f1, cur_none, []]]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

        # Move from b1 to outside the menu
        menu.update(PygameEventUtils.topleft_rect_mouse_motion((1, 1)))
        self.assertEqual(test, [False, False, False, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [None, []])
        self.assertEqual(pygame.mouse.get_cursor(), cur_none)

        # Move from out to b2, this should call f1->f2->b2
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b2))
        self.assertEqual(test, [True, False, True, True, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [b2, [b2, cur_hand, [f2, cur_hand, [f1, cur_none, []]]]])
        self.assertEqual(menu.get_mouseover_widget(), b2)
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

        # Unpack b2
        f2.unpack(b2)
        self.assertEqual(test, [False, False, False, False, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [None, []])
        self.assertEqual(pygame.mouse.get_cursor(), cur_none)

        # Check b2
        menu.scroll_to_widget(b2)
        menu.update(PygameEventUtils.topleft_rect_mouse_motion(b2))
        self.assertEqual(test, [False, False, False, True, False, False])
        self.assertEqual(WIDGET_MOUSEOVER, [b2, [b2, cur_none, []]])
        self.assertEqual(pygame.mouse.get_cursor(), cur_arrow)

    def test_title(self) -> None:
        """
        Test frame title.
        """
        menu = MenuUtils.generic_menu()

        pad = 10
        frame = menu.add.frame_v(300, 200, background_color=(170, 170, 170), padding=pad)

        # self.assertRaises(ValueError, lambda: frame.get_title())
        frame._accepts_title = False
        self.assertRaises(pygame_menu.widgets.widget.frame._FrameDoNotAcceptTitle, lambda: frame.set_title('title'))
        frame._accepts_title = True
        self.assertEqual(frame.get_size(), (300, 200))
        self.assertEqual(frame.get_title(), '')

        # Add a title
        self.assertNotIn(frame, menu._scrollable_frames)
        frame.set_title('epic', padding_outer=3, title_font_size=20, padding_inner=(0, 3), title_font_color='white',
                        title_alignment=pygame_menu.locals.ALIGN_CENTER)
        self.assertIn(frame, menu._scrollable_frames)
        self.assertEqual(frame.get_size(), (300, 234))
        self.assertEqual(frame.get_position(), (150 + pad, 73 + pad))
        self.assertEqual(len(frame._frame_title.get_widgets()), 1)  # The title itself
        self.assertEqual(frame._frame_title.get_widgets()[0].get_size(), (38, 28))
        self.assertEqual(frame._frame_title.get_widgets()[0].get_title(), 'epic')
        self.assertEqual(frame.get_title(), 'epic')
        self.assertEqual(frame._title_height(), 34)
        self.assertEqual(frame.get_position(), (150 + pad, 73 + pad))
        self.assertEqual(frame._frame_title.get_position(), (156, 76))
        menu.render()
        self.assertEqual(frame.get_position(), (150 + pad, 56 + pad))
        self.assertEqual(frame._frame_title.get_position(), (156, 59))
        frame.pack(menu.add.button('Button'))

        # Add button to title
        test = [False]

        def click_button(**kwargs) -> None:
            """
            Click button.
            """
            f = kwargs.pop('frame')
            b = kwargs.pop('button')
            self.assertEqual(f, frame)
            self.assertIsInstance(b, Button)
            test[0] = not test[0]

        btn = frame.add_title_button(pygame_menu.widgets.FRAME_TITLE_BUTTON_CLOSE, click_button)


        menu.mainloop(surface)
