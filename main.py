from window import Window

if __name__ == '__main__':
    main_win = Window(500, 300, "Height Calculator",
                      "Enter your height:", True)
    main_win.create_widgets()
    main_win.run()
