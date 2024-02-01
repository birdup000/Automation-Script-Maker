
from nicegui import ui

with ui.header().classes(replace='row items-center bg-gray-900 text-white') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs().classes('bg-gray-900') as tabs:
        ui.tab('Script Maker')
        ui.tab('Documentation')

with ui.footer(value=False).classes('bg-gray-900 text-white') as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-900 text-white') as left_drawer:
    ui.label('Script Maker').classes('text-2xl font-bold p-4')
    ui.button(on_click=lambda: left_drawer.toggle(), icon='home').props('flat color=blue')

with ui.tab_panels(tabs, value='A').classes('w-full bg-gray-900 text-white'):
    with ui.tab_panel('Script Maker'):
        ui.label('Content of A')
    with ui.tab_panel('Documentation'):
        ui.label('Content of B')

ui.run()