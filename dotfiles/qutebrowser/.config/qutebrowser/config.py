# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova and Daniel Mulford
# Solarized Dark scheme by Ethan Schoonover (modified by aramisgithub)

Base03 = "#002b36"
Base02 = "#073642"
Base01 = "#586e75"
Base00 = "#657b83"
Base0 = "#839496"
Base1 = "#93a1a1"
Base2 = "#eee8d5"
Base3 = "#fdf6e3"
Red = "#dc322f"
Orange = "#cb4b16"
Yellow = "#b58900"
Green  = "#859900"
Cyan  = "#2aa198"
Blue  = "#268bd2"
Violet  = "#6c71c4"
Magenta  = "#d33682"

Hints = "#eac24b"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = Base1

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = Base03

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = Base03

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = Blue

# Background color of the completion widget category headers.
c.colors.completion.category.bg = Base03

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = Base03

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = Base03

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = Base03

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = Blue

# Top border color of the selected completion item
c.colors.completion.item.selected.border.top = Blue

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = Blue

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = Base03

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = Orange

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = Base1

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = Base03

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = Base03

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  Base1

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = Blue

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = Base03

# Background color for the download bar.
c.colors.downloads.bar.bg = Base03

# Color gradient start for download text.
c.colors.downloads.start.fg = Base03

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = Blue

# Color gradient end for download text.
c.colors.downloads.stop.fg = Base03

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = Cyan

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = Red

# Font color for hints.
c.colors.hints.fg = Base03

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = Hints

# Font color for the matched part of hints.
c.colors.hints.match.fg = Base1

# Text color for the keyhint widget.
c.colors.keyhint.fg = Base1

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = Base1

# Background color of the keyhint widget.
c.colors.keyhint.bg = Base03

# Foreground color of an error message.
c.colors.messages.error.fg = Base03

# Background color of an error message.
c.colors.messages.error.bg = Red

# Border color of an error message.
c.colors.messages.error.border = Red

# Foreground color of a warning message.
c.colors.messages.warning.fg = Base03

# Background color of a warning message.
c.colors.messages.warning.bg = Violet

# Border color of a warning message.
c.colors.messages.warning.border = Violet

# Foreground color of an info message.
c.colors.messages.info.fg = Base1

# Background color of an info message.
c.colors.messages.info.bg = Base03

# Border color of an info message.
c.colors.messages.info.border = Base03

# Foreground color for prompts.
c.colors.prompts.fg = Base1

# Border used around UI elements in prompts.
c.colors.prompts.border = Base03

# Background color for prompts.
c.colors.prompts.bg = Base03

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = Yellow

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = Base1

# Background color of the statusbar.
c.colors.statusbar.normal.bg = Base03

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = Blue

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = Base03

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = Yellow

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = Base03

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = Violet

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = Base03

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = Base0

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = Base02

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = Violet

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = Base02

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = Blue

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = Base03

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = Blue

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = Base03

# Background color of the progress bar.
c.colors.statusbar.progress.bg = Blue

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = Base1

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = Red

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = Orange

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = Green

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = Green

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = Violet

# Background color of the tab bar.
c.colors.tabs.bar.bg = Base03

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = Green

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = Green

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = Red

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = Base1

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = Base02

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = Base1

# Background color of unselected even tabs.
c.colors.tabs.even.bg = Base03

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = Green

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = Base03

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = Green

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = Base03

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = Blue

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = Base03

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = Blue

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = Base03

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = Base03

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = Blue

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = Base03

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = Blue

# Background color for webpages if unset (or empty to use the theme's
# color).
c.colors.webpage.bg = Base03


# %s/Base03/Base03/g
# %s/Base02/Base02/g
# %s/Base01/Base01/g
# %s/Base00/Base00/g
# %s/Base0/Base0/g
# %s/Base1/Base1/g
# %s/Base2/Base2/g
# %s/Base3/Base3/g
# %s/Red/Red/g
# %s/Orange/Orange/g
# %s/Yellow/Yellow/g
# %s/Green/Green/g
# %s/Cyan/Cyan/g
# %s/Blue/Blue/g
# %s/Violet/Violet/g
# %s/Magenta/Magenta/g
