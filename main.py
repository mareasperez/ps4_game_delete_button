import sqlite3

PSN_APPS = ['CUSA00219',
            'CUSA00568',
            'CUSA00572',
            'CUSA01000',
            'CUSA01697',
            'CUSA02012',
            'CUSA00001',
            'CUSA00960']
con = sqlite3.connect('Database/app.db')


def sql_fetch(con):
    cursor_obj = con.cursor()

    cursor_obj.execute('SELECT name from sqlite_master where type= "table" and name LIKE "%tbl_appb%"')

    # print(cursor_obj.fetchall())
    tablas = list(cursor_obj.fetchall())
    listajuegos = []
    for tabla in tablas:
        # print(tabla[0])
        cursor_obj.execute(f'SELECT titleName, titleId from {tabla[0]} where titleId LIKE "%CUSA%"')
        juegos = list(cursor_obj.fetchall())
        if listajuegos != juegos:
            listajuegos = juegos
            print('alerta')
    for juego in listajuegos:
        if juego[1] not in PSN_APPS:
            for tabla in tablas:
                print(f'Actualizando {juego[0]}.')
                cursor_obj.execute(f'UPDATE {tabla[0]} set canRemove = 1 where titleId = "{juego[1]}"')
        else:
            print(f'Se omitio el juego {juego[0]} con ID {juego[1]} porque esta en la lista de apps de PS.')

    con.commit()


sql_fetch(con)
