#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('Dbcheck.db')

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE [Users] (
	[idrowuser] integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	[IdUser] TEXT COLLATE NOCASE,
	[last_option] integer COLLATE NOCASE
);

""")



connection.commit()

cursor.execute("""

PRAGMA table_info(Users);

""")
ccc = cursor.fetchall()
print(ccc)



