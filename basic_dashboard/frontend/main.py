from nicegui import ui

@ui.page("/show")
def show():
    with ui.header():

        ui.button(on_click=lambda: left_drawer.toggle()).props('flat color=white icon=menu')
        with ui.tabs() as tabs:
            ui.tab('Home', icon='home')
            ui.tab('About', icon='info')

    with ui.footer(value=False) as footer:
        ui.label('Footer')

    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        ui.label('Side menu')

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle).props('fab icon=contact_support')


    # the page content consists of multiple tab panels
    with ui.tab_panels(tabs, value='Home'):
        with ui.tab_panel('Home'):
            ui.label('This is the first tab')
        with ui.tab_panel('About'):
            ui.label('This is the second tab')

    with ui.button('Click me!', on_click=lambda: badge.set_text(str(int(badge.text) + 1))):
        badge = ui.badge('0', color='red').props('floating')

