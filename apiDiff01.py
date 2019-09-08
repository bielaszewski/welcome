#!/usr/bin/python3

'''
Window parameters specific to the Web platform (web_start_browser=, web_port=)
are flagged as an error when code is run using the Tk Platform

1) run this program using the WEB platform as:  

	python3 apiDiff01.py --web

result? No problem


2) Run using the Tk platform:  
	
	python3 apiDiff01.py

result? 
   File "apiDiff01.py", line 33, in <module>
   window = sg.Window('CatalogQuerySG.py',  web_start_browser=False, web_port=8080).Layout(layout)
   TypeError: __init__() got an unexpected keyword argument 'web_port'


'''




import sys

if '--web' in sys.argv:
	import PySimpleGUIWeb as sg
else:
	import PySimpleGUI as sg

layout= [ [sg.T('foo')] ]

window = sg.Window('CatalogQuerySG.py',  web_start_browser=False, web_port=8080).Layout(layout)
window.Read(timeout=0)	
window.Close()