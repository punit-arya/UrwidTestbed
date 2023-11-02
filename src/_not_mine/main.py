from inspect import currentframe
from inspect import getframeinfo
import urwid

def main():
	# http://urwid.org/tutorial/index.html

	# txt = urwid.Text("Hello World")
	#
	# fill = urwid.Filler(txt, "top")
	# loop = urwid.MainLoop(fill)
	#
	# loop.run()

	print("\n", "-" * 4, " ", getframeinfo(currentframe()).lineno, " ", "-" * 4, "\n", sep = "")

	def exit_on_q(key):
		if key in ("q", "Q"):
			raise urwid.ExitMainLoop()

	palette = [("banner", "black", "light gray"), ("streak", "black", "dark red"), ("bg", "black", "dark blue"), ]

	txt = urwid.Text(("banner", " Hello World "), align = "center")

	map1 = urwid.AttrMap(txt, "streak")
	fill = urwid.Filler(map1)

	map2 = urwid.AttrMap(fill, "bg")
	loop = urwid.MainLoop(map2, palette, unhandled_input = exit_on_q)

	loop.run()

	print("\n", "-" * 4, " ", getframeinfo(currentframe()).lineno, " ", "-" * 4, "\n", sep = "")

if __name__ == '__main__':
	main()
