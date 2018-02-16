import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


class Scrollbox(tkinter.Listbox):
    
    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan,**kwargs)  # Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):  # For accessing the server once.
    
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scrollbox.__init__(self, window, **kwargs)  # Python 2
        super(DataListBox, self).__init__(window, **kwargs)
        # super().__init__(window, **kwargs)  # Same results

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        # Constracting the SQL command to search the Database.
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value  # Store the ID, so we know the "master" record we're populated from
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)      # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)      # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    # Retrieve albums from the Artists
    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)  # TODO delete this line
            index = self.curselection()[0]  # This allows only one element to be selected [0].
            value = self.get(index),

            # get the ID from the database row
            # Make sure we're getting the correctone, by including the link_value if appropriate
            if self.link_value:
                value = value[0], self. link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"
          
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            # SELECT name, _id FROM albums WHERE name = 'Greatest Hits' => This would have had multiple results.
            self.linked_box.requery(link_id)


if __name__ == '__main__':
    conn = sqlite3.connect('music.sqlite')
    print("Connected to database")

    mainWindow = tkinter.Tk()
    mainWindow.title('Music DataBase Browser')
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)    # spacer column on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ===== labels =====
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ===== Artists Listbox =====
    # artistList = tkinter.Listbox(mainWindow)
    # artistList = Scrollbox(mainWindow, background='yellow')
    artistList = DataListBox(mainWindow, conn, "artists", "name", background='yellow')
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief='sunken')
    # ===== We implemented them in our Class =======
    # artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
    # artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
    # artistList['yscrollcommand'] = artistScroll.set

    # Make a query to display the results on the column (Artists). Removed after DataListBox Class.
    # for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     artistList.insert(tkinter.END, artist[0])

    artistList.requery()
    # artistList.bind('<<ListboxSelect>>', DataListBox.on_select)  # No need to bind anymore. Moved in Class


    # ===== Albums Listbox =====
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    # albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
    # albumList = Scrollbox(mainWindow, listvariable=albumLV)
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')
    #  ===== We implemented them in our Class Method =======
    # albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
    # albumScroll.grid(row=1, column=1, sticky='nse', rowspan=1)
    # albumList['yscrollcommand'] = albumScroll.set

    # albumList.requery(12)
    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")


    # ===== Songs Listbox =====
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    # songList = tkinter.Listbox(mainWindow, listvariable=songLV)
    # songList = Scrollbox(mainWindow, listvariable=songLV)
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    # songList.requery()

    albumList.link(songList, "album")

    # ===== Main loop =====
    # testList = range(0, 100)
    # albumLV.set(tuple(testList))
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()
