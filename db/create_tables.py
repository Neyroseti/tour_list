from pg8000 import Cursor

tables = {
    'direction': "CREATE TABLE IF NOT EXISTS direction (direction_id serial PRIMARY KEY, direction_price money);",
    'strings': '''CREATE TABLE Strings (
                    id serial NOT NULL PRIMARY KEY,
	                touristcard_fk int NOT NULL,
	                direction_fk int,
	                manager_fk int,
	                date1 date,
	                FOREIGN KEY(touristcard_fk) REFERENCES Tourist(touristcard_id),
	                FOREIGN KEY(direction_fk) REFERENCES Direction(direction_id),
	                FOREIGN KEY(manager_fk) REFERENCES Manager(manager_id));''',
    'tourist_card': '''CREATE TABLE Tourist_card(
	                touristcard_id serial primary key,
	                fio varchar(32),
	                category_fk int,
	                phone_number int,
	                foreign key(category_fk) references Category (category_id));''',
    'category': 'CREATE TABLE Category ( category_id serial primary key, category varchar(16), discount numeric);',
    'manager': 'CREATE TABLE Manager (manager_id serial primary key, manager varchar(16));'
}


def check_tables(cursor: Cursor) -> dict:
    """ Функция, которая проверяет, созданы ли таблицы.
    На вход принимает курсор
    На выходе возвращает словарь с ответами """

    def response(table):
        query = f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table}');"
        cursor.execute(query)
        return cursor.fetchone()[0]

    check = {
        'manager': response('manager'),
        'category': response('category'),
        'direction': response('direction'),
        'tourist_card': response('tourist_card'),
        'strings': response('strings'),
    }

    return check


def create_tables(cursor: Cursor) -> None:
    response = check_tables(cursor)
    for key, value in response.items():
        if not value:
            global tables
            cursor.execute(tables[key])


