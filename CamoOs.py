import tkinter
from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
import platform, os, time, psutil, sys

try:
    print('starting...')
    time.sleep(2)

    root = Tk()
    root.attributes('-fullscreen', True)
    root['bg'] = 'orange'
    root.option_add("*tearOff", FALSE)

    # TERMINAL
    def terminal():
        print('terminal')
        os.system('start terminal.py')

    # SHUTDOWN
    def shutdown():
        print('SHUTDOWN')
        time.sleep(1)
        root.destroy()

    # SETTINGS
    def settings():
        print('settings')
        settings_app = Tk()
        settings_app.title('settings')
        settings_app.geometry('1000x600')
        settings_app.resizable(width=False, height=False)
        settings_app.iconbitmap('pictures/settings.ico')


        settings_app.mainloop()

    # BACKGROUND COLOR | VIEW
    def red_bg():
        root['bg'] = 'red'

    def blue_bg():
        root['bg'] = 'blue'

    def white_bg():
        root['bg'] = 'white'

    def default_bg():
        root['bg'] = 'orange'

    # VIEW
    def view():
        print('view')
        view = Tk()
        view.title('view')
        view.geometry('1000x600')
        view.resizable(width=False, height=False)
        view.iconbitmap('pictures/view.ico')

        bg_view = Label(view, text='background color', font=('Arial', 20)).pack()

        red_bg_btn = Button(view, text='red', width=20, height=2, fg='black', bg='red', command=red_bg).place(x=50, y=80)

        blue_bg_btn = Button(view, text='blue', width=20, height=2, fg='black', bg='blue', command=blue_bg)
        blue_bg_btn.place(x=250, y=80)

        white_bg_btn = Button(view, text='white', width=20, height=2, fg='black', bg='white', command=white_bg)
        white_bg_btn.place(x=450, y=80)

        default_bg_btn = Button(view, text='default', width=20, height=2, fg='black', bg='white', command=default_bg)
        default_bg_btn.place(x=800, y=80)

        view.mainloop()

    def boot_bios():
        showerror(title='boot bios error', message='The BIOS is under development')

    # THE SCREEN OF DEATH
    def screen_death():
        print('THE SCREEN OF DEATH')
        root['bg'] = 'blue'
        main_label_sc = Label(root, text='Fatal error', font=('Arial', 30), fg='white', bg='blue').place(x=800, y=200)
        label1_cs = Label(root, text='a system error has occurred', font=('Arial', 20), fg='white', bg='blue').place(x=750, y=300)
        label2_cs = Label(root, text='But most likely this is a false or temporary error', fg='white', bg='blue', font=('Arial', 20)).place(x=750, y=350)
        label3_cs = Label(root, text='Restart the CamoOs', fg='white', bg='blue', font=('Arial', 20)).place(x=750, y=400)

        emergency_shutdown = Button(root, text='shutdown', fg='white', bg='blue', width=20, height=2, command=shutdown).place(x=10, y=1000)

        start_menu.config(Menu="")

    # APP MENU
    app_menu = Menu()
    app_menu.add_command(label='terminal', command=terminal)

    # SETTINGS MENU
    settings_menu = Menu()
    settings_menu.add_command(label='settings', command=settings)
    settings_menu.add_separator()
    settings_menu.add_command(label='boot (does not work)', command=boot_bios)

    # START MENU
    start_menu = Menu()
    shutdown_menu = Menu()
    shutdown_menu.add_command(label='shutdown', command=shutdown)

    start_menu.add_cascade(label='apps', menu=app_menu)
    start_menu.add_cascade(label='settings', menu=settings_menu)
    start_menu.add_cascade(label='shutdown', menu=shutdown_menu)

    root.config(menu=start_menu)

    # CREATE MENU
    create_menu = Menu()
    create_menu.add_command(label='folder')
    create_menu.add_separator()
    create_menu.add_command(label='text document')


    # RIGHT CLICK MENU
    menu_click = Menu()
    menu_click.add_cascade(label='view', command=view)
    menu_click.add_separator()
    menu_click.add_cascade(label='create (does not work)', menu=create_menu)

    def r_click(event):
        try:
            menu_click.tk_popup(event.x_root, event.y_root)
        finally:
            menu_click.grab_release()

    root.bind("<Button-3>", r_click)


    root.mainloop()
except:
    screen_death()
