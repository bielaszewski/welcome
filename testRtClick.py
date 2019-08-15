'''
Demonstrate (mis)behavior of clickright menus for items in a listbox

github user: bielaszewski
aka reddit user: mtcabeza

Aug 15, 2019
'''

from __future__ import print_function
import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Layout is a Listbox containing 3 items. key is 'listBox_1'
# Listbox events are enabled.  A right click menu is defined containing 2 menu items.
layout = [
 
	[sg.Listbox( 
		values=['listItemA', 'listItemB', 'listItemC'],
		size=(20,3),
		enable_events=True, 
		key='listBox_1', 
		right_click_menu=['unused', ['MenuItem1', 'MenuItem2']] )
	]
]

	
window = sg.Window('').Layout(layout)

while True:
	event,values= window.Read()
	if not event: 
		break	
	print( 'event=', event,  'values=', values)
#
window.Close()
