import psycopg2

class DatabaseError(Exception):
    pass
class NotFoundError(Exception):
    pass


class Entity(object):
    db = None

    __delete_query    = 'DELETE FROM "{table}" WHERE {table}_id=%s'
    __insert_query    = 'INSERT INTO "{table}" ({columns}) VALUES ({placeholders})'
    __list_query      = 'SELECT * FROM "{table}"'
    __parent_query    = 'SELECT * FROM "{table}" WHERE {parent}_id=%s'
    __select_query    = 'SELECT * FROM "{table}" WHERE {table}_id=%s'
    __sibling_query   = 'SELECT * FROM "{sibling}" NATURAL JOIN "{join_table}" WHERE {table}_id=%s'
    __update_children = 'UPDATE "{table}" SET {parent}_id=%s WHERE {table}_id IN ({children})'
    __update_query    = 'UPDATE "{table}" SET {columns} WHERE {table}_id=%s'

    def __init__(self, id=None):
        self.__class__.db = psycopg2.connect( user='postgres', password = 'Vb094545');
        if self.__class__.db is None:
            raise DatabaseError()

        self.__cursor   = self.__class__.db.cursor()
        self.__fields   = {}
        self.__id       = id
        self.__loaded   = False 
        self.__modified = False
        self.__table    = self.__class__.__name__.lower()

    def __getattr__(self, name):
        # if self.__modified == True:
        #     raise DatabaseError()
        # # # check, if instance is modified and throw an exception
        # # # get corresponding data from database if needed
        # if self.__id is None:
        #     print "set id pls"
        #     return None
        # if self.__loaded == False:
        #     query = self.__class__.__select_query
        #     args = [self.__table]
        #     args.add(self.__table)
        #     self.__execute_query(query, args):
        #     try:
        #         self.__cursor.execute(self.__class__.__select_query.format(self.__table), self.__id)
        #         values = self.__cursor.fetchall()
        #         self.__cursor.execute('SELECT column_name FROM information_schema.columns WHERE table_name = '{}';'.format(self.__table))
        #         keys = self.__cursor.fetchall()
        #         counter = 0
        #         for key in keys:
        #             self.__fields[key[0]] = values[0][counter]
        #             counter += 1
        #         self.__loaded = True




        # check, if requested property name is in current class
        #    columns, parents, children or siblings and call corresponding
        #    getter with name as an argument
        # throw an exception, if attribute is unrecognized
        pass

    def __setattr__(self, name, value):
        # check, if requested property name is in current class
        if hasattr(self, name):
            self.__dict__['name'] = value
        else:
            super(Entity, self).__setattr__(name, value)

        #    columns, parents, children or siblings and call corresponding
        #    setter with name and value as arguments or use default implementation

    def __execute_query(self, query, args = None):
        # execute an sql statement and handle exceptions together with transactions
        try:
            if args is not None:
                self.__cursor.execute(query,args)
            else:
                self.__cursor.execute(query)
        except psycopg2.DatabaseError, e:
            print 'Error: %s' % e    
            sys.exit(1)
        finally:
            if con:
                self.__class__.db.commit()
                self.__class__.db.close()

    def __insert(self):
        # generate an insert query string from fields keys and values and execute it
        # use prepared statements
        # save an insert id
        pass

    def __load(self):
        pass

    def __update(self):
        # generate an update query string from fields keys and values and execute it
        # use prepared statements
        pass

    def _get_children(self, name):
        # return an array of child entity instances
        # each child instance must have an id and be filled with data
        pass

    def _get_column(self, name):
        # return value from fields array by <table>_<name> as a key
        pass

    def _get_parent(self, name):
        # get parent id from fields with <name>_id as a key
        # return an instance of parent entity class with an appropriate id
        pass

    def _get_siblings(self, name):
        # get parent id from fields with <name>_id as a key
        # return an array of sibling entity instances
        # each sibling instance must have an id and be filled with data
        pass

    def _set_column(self, name, value):
        # put new value into fields array with <table>_<name> as a key
        pass

    def _set_parent(self, name, value):
        # put new value into fields array with <name>_id as a key
        # value can be a number or an instance of Entity subclass
        pass

    @classmethod
    def all(cls):
        # get ALL rows with ALL columns from corrensponding table
        # for each row create an instance of appropriate class
        # each instance must be filled with column data, a correct id and MUST NOT query a database for own fields any more
        # return an array of istances
        pass

    def delete(self):
        # execute delete query with appropriate id
        pass

    @property
    def id(self):
        return self.__id

    @property
    def created(self):
        # try to guess yourself
        pass

    @property
    def updated(self):
        return self.__update

    def save(self):
        # execute either insert or update query, depending on instance id
        if self.__modified == True:
            columns_set = []
            for key in self.__fields.keys():
                tmp = str(key) + " = " + str(self.__fields[key])
                columns_set.append(tmp)
            columns = ", ".join(columns_set)
            updt_query = self.__class__.__update_query.format(columns)
            self.__execute_query(updt_query, self.__id)
        else:
            columns_set = []
            placeholders_set = []
            for value in self.__fields.values():
                placeholders_set.append(value)
            placeholders = ", ".join(placeholders_set)
            for key in self.__fields.keys():
                columns_set.append(key)
            columns = ", ".join(columns_set)
            save_query = self.__class__.__insert_query.format(self.__table, columns, placeholders)
            self.__execute_query(save_query)
        self.__loaded = True


first = Entity()
# print first.save()