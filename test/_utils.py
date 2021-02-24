"""
pygame-menu
https://github.com/ppizarror/pygame-menu

UTILS
Test suite utility functions and classes.

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

__all__ = [

    # Globals
    'PYGAME_V2',
    'TEST_THEME',
    'WIDGET_MOUSEOVER',
    'WINDOW_SIZE',

    # Methods
    'reset_widgets_over',
    'surface',
    'test_reset_surface',

    # Class utils (static)
    'PygameEventUtils',
    'MenuUtils'

]

import random

import pygame
import pygame_menu

from pygame_menu.font import FONT_EXAMPLES
from pygame_menu.locals import FINGERDOWN, FINGERMOTION, FINGERUP
from pygame_menu.utils import assert_vector, PYGAME_V2
from pygame_menu.widgets.core.widget import check_widget_mouseleave

# noinspection PyProtectedMember
from pygame_menu._types import NumberType, Union, List, Tuple, Optional, Tuple2IntType, EventType, \
    MenuColumnMaxWidthType, MenuColumnMinWidthType, Any, MenuRowsType, Tuple2NumberType, VectorIntType

EventListType = Union[EventType, List[EventType]]

# Constants
WINDOW_SIZE = (600, 600)  # Width, height

# Init pygame
pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)

TEST_THEME = pygame_menu.themes.THEME_DEFAULT.copy()
TEST_THEME.widget_margin = (0, 10)
TEST_THEME.widget_padding = 0
TEST_THEME.widget_selection_effect = pygame_menu.widgets.HighlightSelection()

WIDGET_MOUSEOVER = pygame_menu.widgets.core.widget.WIDGET_MOUSEOVER


def reset_widgets_over() -> None:
    """
    Reset widget over.

    :return: None
    """
    check_widget_mouseleave(force=True)


def test_reset_surface() -> None:
    """
    Reset test surface.

    :return: None
    """
    global surface
    surface = pygame.display.set_mode(WINDOW_SIZE)


class PygameEventUtils(object):
    """
    Event utils.
    """

    @staticmethod
    def joy_motion(
            x: NumberType = 0,
            y: NumberType = 0,
            inlist: bool = True,
            testmode: bool = True
    ) -> EventListType:
        """
        Create a pygame joy controller motion event.

        :param x: X-axis movement
        :param y: Y-axis movement
        :param inlist: Return event in a list
        :param testmode: Event is in test mode
        :return: Event
        """
        if x != 0 and y != 0:
            return [PygameEventUtils.joy_motion(x=x, inlist=False, testmode=testmode),
                    PygameEventUtils.joy_motion(y=y, inlist=False, testmode=testmode)]
        event_obj = None

        if x != 0:
            event_obj = pygame.event.Event(pygame.JOYAXISMOTION,
                                           {
                                               'value': x,
                                               'axis': pygame_menu.controls.JOY_AXIS_X,
                                               'test': testmode
                                           })
        if y != 0:
            event_obj = pygame.event.Event(pygame.JOYAXISMOTION,
                                           {
                                               'value': y,
                                               'axis': pygame_menu.controls.JOY_AXIS_Y,
                                               'test': testmode
                                           })

        if inlist:
            event_obj = [event_obj]
        return event_obj

    @staticmethod
    def center_joy(testmode: bool = True) -> List[EventType]:
        """
        Centers the joy.

        :param testmode: Event is in test mode
        :return: Center joy event
        """
        return [pygame.event.Event(pygame.JOYAXISMOTION,
                                   {
                                       'value': 0,
                                       'axis': pygame_menu.controls.JOY_AXIS_Y,
                                       'test': testmode
                                   })]

    @staticmethod
    def test_widget_key_press(
            widget: 'pygame_menu.widgets.Widget',
            testmode: bool = True
    ) -> None:
        """
        Test keypress widget.

        :param widget: Widget object
        :param testmode: Event is in test mode
        :return: None
        """
        widget.update(PygameEventUtils.key(pygame.K_BACKSPACE, keydown=True, testmode=testmode))
        widget.update(PygameEventUtils.key(pygame.K_DELETE, keydown=True, testmode=testmode))
        widget.update(PygameEventUtils.key(pygame.K_LEFT, keydown=True, testmode=testmode))
        widget.update(PygameEventUtils.key(pygame.K_RIGHT, keydown=True, testmode=testmode))
        widget.update(PygameEventUtils.key(pygame.K_END, keydown=True, testmode=testmode))
        widget.update(PygameEventUtils.key(pygame.K_HOME, keydown=True, testmode=testmode))

    @staticmethod
    def joy_key(
            key: Tuple[int, int],
            inlist: bool = True,
            testmode: bool = True
    ) -> EventListType:
        """
        Create a pygame joy controller key event.

        :param key: Key to press
        :param inlist: Return event in a list
        :param testmode: Event is in test mode
        :return: Event
        """
        event_obj = pygame.event.Event(pygame.JOYHATMOTION,
                                       {
                                           'value': key,
                                           'test': testmode
                                       })
        if inlist:
            event_obj = [event_obj]
        return event_obj

    @staticmethod
    def keydown_mod_ctrl(
            key: int,
            inlist: bool = True,
            testmode: bool = True
    ) -> EventListType:
        """
        Create a mod ctrl keydown event (Ctrl+Key).

        :param key: Key to press
        :param inlist: Return event in a list
        :param testmode: Event is in test mode
        :return: Event
        """
        # noinspection PyArgumentList
        pygame.key.set_mods(pygame.KMOD_CTRL)
        event_obj = pygame.event.Event(pygame.KEYDOWN,
                                       {
                                           'key': key,
                                           'test': testmode
                                       })
        if inlist:
            event_obj = [event_obj]
        return event_obj

    @staticmethod
    def keydown(key: Union[int, VectorIntType], testmode: bool = True) -> EventListType:
        """
        Keydown list.

        :param key: Key to press
        :param testmode: Event is in test mode
        :return: Event list
        """
        if isinstance(key, int):
            key = [key]
        ev = []
        for k in key:
            assert isinstance(k, int)
            ev.append(PygameEventUtils.key(k, keydown=True, inlist=False, testmode=testmode))
        return ev

    @staticmethod
    def key(
            key: int,
            char: str = ' ',
            inlist: bool = True,
            keydown: bool = False,
            keyup: bool = False,
            testmode: bool = True
    ) -> EventListType:
        """
        Create a keyboard event.

        :param key: Key to press
        :param char: Char representing the key
        :param inlist: Return event in a list
        :param keydown: Event is keydown
        :param keyup: Event is keyup
        :param testmode: Event is in test mode
        :return: Event
        """
        if keyup and keydown:
            raise ValueError('keyup and keydown cannot be active at the same time')
        if keydown == keyup and not keydown:
            raise ValueError('keyup and keydown cannot be false at the same time')
        event = -1
        if keydown:
            event = pygame.KEYDOWN
        if keyup:
            event = pygame.KEYUP
        event_obj = pygame.event.Event(event,
                                       {
                                           'key': key,
                                           'test': testmode
                                       })
        if len(char) == 1:
            event_obj.dict['unicode'] = char
        if inlist:
            event_obj = [event_obj]
        return event_obj

    @staticmethod
    def enter_window(inlist: bool = True, testmode: bool = True) -> EventListType:
        """
        Enter window event.

        :param inlist: Return event in a list
        :param testmode: Event is in test mode
        :return: Event
        """
        ev = pygame.event.Event(pygame.ACTIVEEVENT, {'gain': 1, 'test': testmode})
        if inlist:
            ev = [ev]
        return ev

    @staticmethod
    def leave_window(inlist: bool = True, testmode: bool = True) -> EventListType:
        """
        Leave window event.

        :param inlist: Return event in a list
        :param testmode: Event is in test mode
        :return: Event
        """
        ev = pygame.event.Event(pygame.ACTIVEEVENT, {'gain': 0, 'test': testmode})
        if inlist:
            ev = [ev]
        return ev

    @staticmethod
    def mouse_click(
            x: NumberType,
            y: NumberType,
            inlist: bool = True,
            evtype: int = pygame.MOUSEBUTTONUP,
            rel: Tuple2IntType = (0, 0),
            button: int = 3,
            testmode: bool = True,
            update_mouse: bool = False
    ) -> EventListType:
        """
        Generate a mouse click event.

        :param x: X coordinate (px)
        :param y: Y coordinate (px)
        :param inlist: Return event in a list
        :param evtype: event type, it can be MOUSEBUTTONUP or MOUSEBUTTONDOWN
        :param rel: Rel position (relative movement)
        :param button: Which button presses, ``1`` to ``3`` are the main buttons; ``4`` and ``5`` is the wheel
        :param testmode: Event is in test mode
        :param update_mouse: If ``True`` updates the mouse position
        :return: Event
        """
        assert isinstance(button, int) and button > 0
        assert_vector(rel, 2, int)
        event_obj = pygame.event.Event(evtype,
                                       {
                                           'button': button,
                                           'pos': (x, y),
                                           'rel': rel,
                                           'test': testmode
                                       })
        if update_mouse:
            print('set mouse position', (x, y))
            pygame.mouse.set_pos((x, y))
        if inlist:
            event_obj = [event_obj]
        return event_obj

    @staticmethod
    def touch_click(
            x: NumberType,
            y: NumberType,
            inlist: bool = True,
            evtype: int = FINGERUP,
            normalize: bool = True,
            menu: Union['pygame_menu.Menu', None] = None,
            testmode: bool = True
    ) -> EventListType:
        """
        Generate a mouse click event.

        :param x: X coordinate
        :param y: Y coordinate
        :param inlist: Return event in a list
        :param evtype: Event type, it can be FINGERUP, FINGERDOWN or FINGERMOTION
        :param normalize: Normalize event position
        :param menu: Menu reference
        :param testmode: Event is in test mode
        :return: Event
        """
        assert PYGAME_V2, 'function only available in pygame v2+'
        if normalize:
            assert menu is not None, 'menu reference must be provided if normalize is used'
            display_size = menu.get_window_size()
            x /= display_size[0]
            y /= display_size[1]
        event_obj = pygame.event.Event(evtype,
                                       {
                                           'test': testmode,
                                           'x': x,
                                           'y': y
                                       })
        if inlist:
            event_obj = [event_obj]
        return event_obj

    @staticmethod
    def topleft_rect_mouse_motion(
            rect: Union['pygame_menu.widgets.Widget', 'pygame.Rect', Tuple2NumberType],
            inlist: bool = True,
            delta: Tuple2IntType = (0, 0),
            testmode: bool = True,
            update_mouse: bool = False
    ) -> EventListType:
        """
        Mouse motion event.

        :param rect: Widget, Rect object, or Tuple
        :param inlist: If ``True`` return the event within a list
        :param delta: Add tuple to rect position
        :param testmode: Event is in test mode
        :param update_mouse: If ``True`` updates the mouse position
        :return: Event
        """
        if isinstance(rect, pygame_menu.widgets.Widget):
            x, y = rect.get_rect(to_real_position=True, render=True).topleft
        elif isinstance(rect, pygame.Rect):
            x, y = rect.topleft
        elif isinstance(rect, (tuple, list)):
            x, y = rect[0], rect[1]
        else:
            raise ValueError('unknown rect type')
        return PygameEventUtils.middle_rect_click(
            rect=(x, y),
            evtype=pygame.MOUSEMOTION,
            inlist=inlist,
            delta=delta,
            testmode=testmode,
            update_mouse=update_mouse
        )

    @staticmethod
    def middle_rect_mouse_motion(
            rect: Union['pygame_menu.widgets.Widget', 'pygame.Rect', Tuple2NumberType],
            inlist: bool = True,
            delta: Tuple2IntType = (0, 0),
            testmode: bool = True,
            update_mouse: bool = False
    ) -> EventListType:
        """
        Mouse motion event.

        :param rect: Widget, Rect object, or Tuple
        :param inlist: If ``True`` return the event within a list
        :param delta: Add tuple to rect position
        :param testmode: Event is in test mode
        :param update_mouse: If ``True`` updates the mouse position
        :return: Event
        """
        return PygameEventUtils.middle_rect_click(
            rect=rect,
            evtype=pygame.MOUSEMOTION,
            inlist=inlist,
            delta=delta,
            testmode=testmode,
            update_mouse=update_mouse
        )

    @staticmethod
    def middle_rect_click(
            rect: Union['pygame_menu.widgets.Widget', 'pygame.Rect', Tuple2NumberType],
            menu: Optional['pygame_menu.Menu'] = None,
            evtype: int = pygame.MOUSEBUTTONUP,
            inlist: bool = True,
            rel: Tuple2IntType = (0, 0),
            button: int = 3,
            delta: Tuple2IntType = (0, 0),
            testmode: bool = True,
            update_mouse: bool = False
    ) -> EventListType:
        """
        Return event clicking the middle of a given rect.

        :param rect: Widget, Rect object, or Tuple
        :param menu: Menu object
        :param evtype: event type, it can be MOUSEBUTTONUP,  MOUSEBUTTONDOWN, MOUSEMOTION, FINGERUP, FINGERDOWN, FINGERMOTION
        :param inlist: If ``True`` return the event within a list
        :param rel: Rel position (relative movement)
        :param button: Which button presses, ``1`` to ``3`` are the main buttons; ``4`` and ``5`` is the wheel
        :param delta: Add tuple to rect position
        :param testmode: Event is in test mode
        :param update_mouse: If ``True`` updates the mouse position
        :return: Event
        """
        assert isinstance(button, int) and button > 0
        assert_vector(rel, 2, int)
        assert_vector(delta, 2, int)
        if isinstance(rect, pygame_menu.widgets.Widget):
            x, y = rect.get_rect(to_real_position=True, render=True).center
            menu = rect.get_menu()
        elif isinstance(rect, pygame.Rect):
            x, y = rect.center
        elif isinstance(rect, (tuple, list)):
            x, y = rect[0], rect[1]
        else:
            raise ValueError('unknown rect type')
        if evtype == FINGERDOWN or evtype == FINGERUP or evtype == FINGERMOTION:
            assert menu is not None, \
                'menu cannot be none if FINGERDOWN, FINGERUP, or FINGERMOTION'
            display = menu.get_window_size()
            evt = pygame.event.Event(evtype,
                                     {
                                         'button': button,
                                         'rel': rel,
                                         'test': testmode,
                                         'x': (x + delta[0]) / display[0],
                                         'y': (y + delta[1]) / display[1]
                                     })
            if inlist:
                evt = [evt]
            return evt
        return PygameEventUtils.mouse_click(
            x=x + delta[0],
            y=y + delta[1],
            inlist=inlist,
            evtype=evtype,
            rel=rel,
            button=button,
            testmode=testmode,
            update_mouse=update_mouse
        )


class MenuUtils(object):
    """
    Static class for utility pygame-menu methods.
    """

    @staticmethod
    def get_font(name: str, size: int) -> 'pygame.font.Font':
        """
        Returns a font.

        :param name: Font name
        :param size: Font size
        :return: Font
        """
        return pygame_menu.font.get_font(name, size)

    @staticmethod
    def random_font() -> str:
        """
        Return a random font from the library.

        :return: Font file
        """
        opt = random.randrange(0, len(FONT_EXAMPLES))
        return FONT_EXAMPLES[opt]

    @staticmethod
    def load_font(font: str, size: int) -> 'pygame.font.Font':
        """
        Load font from file.

        :param font: Font name
        :param size: Font size
        :return: Font object
        """
        return pygame_menu.font.get_font(font, size)

    @staticmethod
    def random_system_font() -> str:
        """
        Return random system font.

        :return: System font name
        """
        fonts = pygame.font.get_fonts()
        fonts.sort()
        fonts.pop(0)
        return fonts[int(random.randrange(0, len(fonts)))]

    @staticmethod
    def generic_menu(
            center_content: bool = True,
            column_max_width: MenuColumnMaxWidthType = None,
            column_min_width: MenuColumnMinWidthType = 0,
            columns: int = 1,
            enabled: bool = True,
            height: NumberType = 400,
            mouse_motion_selection: bool = False,
            onclose: Any = None,
            onreset: Any = None,
            position_x: NumberType = 50,
            position_y: NumberType = 50,
            rows: MenuRowsType = None,
            theme: 'pygame_menu.themes.Theme' = pygame_menu.themes.THEME_DEFAULT,
            title: str = '',
            width: NumberType = 600,
            *args,
            **kwargs
    ) -> 'pygame_menu.Menu':
        """
        Generate a generic test menu.

        :param center_content: Center menu content
        :param column_max_width: List/Tuple representing the maximum width of each column in px, ``None`` equals no limit. For example ``column_max_width=500`` (each column width can be 500px max), or ``column_max_width=(400, 500)`` (first column 400px, second 500). If ``0` is given uses the menu width. This method does not resize the widgets, only determines the dynamic width of the column layout
        :param column_min_width: List/Tuple representing the minimum width of each column in px. For example ``column_min_width=500`` (each column width is 500px min), or ``column_max_width=(400, 500)`` (first column 400px, second 500). By default it's ``0``. Negative values are not accepted
        :param columns: Number of columns
        :param enabled: Menu is enabled. If ``False`` Menu cannot be drawn
        :param height: Menu height (px)
        :param mouse_motion_selection: Select widgets using mouse motion. If ``True`` menu draws a ``focus`` on the selected widget
        :param onclose: Event or function applied when closing the Menu
        :param onreset: Function executed when resetting the Menu
        :param position_x: X position of the menu
        :param position_y: Y position of the menu
        :param rows: Number of rows
        :param theme: Menu theme
        :param title: Menu title
        :param width: Menu width (px)
        :param args: Additional args
        :param kwargs: Optional keyword arguments
        :return: Menu
        """
        return pygame_menu.Menu(
            center_content=center_content,
            column_max_width=column_max_width,
            column_min_width=column_min_width,
            columns=columns,
            enabled=enabled,
            height=height,
            mouse_motion_selection=mouse_motion_selection,
            onclose=onclose,
            onreset=onreset,
            position=(position_x, position_y),
            rows=rows,
            theme=theme,
            title=title,
            width=width,
            *args,
            **kwargs
        )
