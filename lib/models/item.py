from models.__init__ import CURSOR, CONN

class Item:

    all = {}
    
    def __init__(self, name, proveyer_id, par_id, catagory_id):
        self.name = name
        self.proveyer_id = proveyer_id
        self.par_id = par_id
        self.catagory_id = catagory_id
        
    def __repr__(self):
        return f"<Item {self.id}: {self.name}, {self.proveyer_id}, {self.par_id}, {self.catagory_id}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and not hasattr(self, 'name'):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not a string, Item must have a name')
        
    @property
    def proveyer_id(self):
        return self._proveyer_id
    
    @proveyer_id.setter
    def proveyer_id(self, new_proveyer_id):
        if isinstance (new_proveyer_id, int):
            self._proveyer_id = new_proveyer_id
        else:
            raise TypeError(f'{new_proveyer_id} is not a integer, Items must have a proveyer ID')
        
    @property
    def par_id(self):
        return self._par_id
    
    @par_id.setter
    def par_id(self, new_par_id):
        if isinstance (new_par_id, int) and not hasattr(self, 'par_id'):
            self._par_id = new_par_id
        else:
            raise TypeError(f'{new_par_id} is not a integer, Items must have a par ID')
        
    @property
    def catagory_id(self):
        return self._catagory_id
    
    @catagory_id.setter
    def catagory_id(self, new_catagory_id):
        if isinstance (new_catagory_id, int) and not hasattr(self, 'catagory_id'):
            self._catagory_id = new_catagory_id
        else:
            raise TypeError(f'{new_catagory_id} is not a integer, Items must have a catagory ID')    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT,
            proveyer_id INTEGER,
            par_id INTEGER,
            catagory_id INTEGER,
            FOREIGN KEY (proveyer_id) REFERENCES proveyer(id),
            FOREIGN KEY (par_id) REFERENCES par(id),
            FOREIGN KEY (catagory_id) REFERENCES catagory(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, proveyer_id, par_id, catagory_id):
        item = cls(str(name), int(proveyer_id), int(par_id), int(catagory_id))
        item.save()
        return item
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS items
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.proveyer_id = row[2]

        else:
            item = cls(str(row[1]),  int(row[2]), int(row[3]), int(row[4]))
            item.id = row[0]
            cls.all[item.id] = item
        return item
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM items
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM items
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM items
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO items(name, proveyer_id, par_id, catagory_id)
            VALUES (?,?,?,?)
        """    
        CURSOR.execute(sql, (self.name, self.proveyer_id, self.par_id, self.catagory_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE items
            SET name=?, proveyer_id=?, par_id=?, catagory_id=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM items
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       