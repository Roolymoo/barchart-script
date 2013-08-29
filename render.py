import pygame
from pygame.font import Font


def render_barchart(app, TITLE, PLOT_DATA):
    '''(App, str, list) -> NoneType
    Renders all of the barchart title, the axis and numeric grading of the
    axis, bars for the data and their titles, and some grid work with the
    axis.'''
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    PADDING = 10

    TITLE_SIZE = _render_title(app, TITLE, PADDING)

    VAXIS_MAX, HAXIS_MAX, MAX_PLOT = _render_axis(app, PLOT_DATA, TITLE_SIZE, PADDING)

    _render_bars(app, PLOT_DATA, VAXIS_MAX, HAXIS_MAX, MAX_PLOT, PADDING)

def _render_title(app, TITLE, PADDING):
    '''(App, str, int) -> int'''
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    TITLE_DEST = (0 + PADDING, 0 + PADDING)
    TITLE_SIZE = 30
    FONT_FAM = None # default
    ANTIALIAS = True
    app.window.blit(
            Font(FONT_FAM, TITLE_SIZE).render(TITLE, ANTIALIAS, BLACK, WHITE),
            TITLE_DEST)
    return TITLE_SIZE

def _render_axis(app, PLOT_DATA, TITLE_SIZE, PADDING):
    '''(App, list, int, int) -> list'''
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # axis
    VAXIS_MAX = app.height - (PADDING * 2 + TITLE_SIZE + PADDING)
    HAXIS_MAX = app.width - PADDING * 2

    # vert
    start_pos = (0 + PADDING, 0 + PADDING + TITLE_SIZE + PADDING)
    end_pos = (0 + PADDING, app.height - PADDING)
    pygame.draw.line(app.window, BLACK, start_pos, end_pos)
    # horiz
    start_pos = (0 + PADDING, app.height - PADDING)
    end_pos = (app.width - PADDING, app.height - PADDING)
    pygame.draw.line(app.window, BLACK, start_pos, end_pos)

    MAX_PLOT = max([float(p[1]) for p in PLOT_DATA])

    # axis values and addition horiz lines
    VAL_SIZE = 12
    POS_INCR = VAXIS_MAX / 4
    pos = 0 + PADDING
    TEXT_VAL_INCR = MAX_PLOT / 4
    text_val = 0.0
    while pos <= VAXIS_MAX + PADDING:
        # line
        start_pos = (0 + PADDING, app.height - pos)
        end_pos = (app.width - PADDING, app.height - pos)
        pygame.draw.line(app.window, BLACK, start_pos, end_pos)

        # text
        dest = (0, app.height - pos)
        val = "%.2f" % text_val
        app.window.blit(
                pygame.font.Font(None, VAL_SIZE).render(val, True, BLACK, WHITE),
                dest)

        pos += POS_INCR
        text_val += TEXT_VAL_INCR

    return [VAXIS_MAX, HAXIS_MAX, MAX_PLOT]

def _render_bars(app, PLOT_DATA, VAXIS_MAX, HAXIS_MAX, MAX_PLOT, PADDING):
    '''(App, list, float, float, float, int) -> NoneType'''
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    UNIT_HEIGHT = VAXIS_MAX / MAX_PLOT
    UNIT_WIDTH = (HAXIS_MAX - (len(PLOT_DATA) - 1) * PADDING) / len(PLOT_DATA)

    i = 0
    for plot in PLOT_DATA:
        title, val = plot

        # title
        title_dest = (0 + (i + 1) * PADDING + i * UNIT_WIDTH + 0.5 * UNIT_WIDTH,
                app.height - PADDING)
        title_size = 12
        font_fam = None # default
        antialias = True
        app.window.blit(
                Font(font_fam, title_size).render(title, antialias, BLACK, WHITE),
                title_dest)

        # draw the rect
        if val != 0:
            left = (i + 1) * PADDING + i * UNIT_WIDTH
            top = app.height - (PADDING + val * UNIT_HEIGHT)
            width = UNIT_WIDTH
            height = val * UNIT_HEIGHT
            rect = pygame.Rect(left, top, width, height)
            pygame.draw.rect(app.window, BLACK, rect)
            # fill the rect in
            app.window.fill(BLACK, rect)

        i += 1
