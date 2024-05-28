from models.__init__ import CURSOR, CONN


class Catagory:
    all = {}
    
    def __init__(self, name, item_id):
        self.name = name
        self.item_id = item_id
        
    def __repr__(self):
        return f"<Catagory {self.id}: {self.name}, {self.item_id}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not a string.')

    @property
    def item_id(self):
        return self._item_id
    
    @item_id.setter
    def item_id(self, new_item_id):
        if isinstance (new_item_id, int):
            self._item_id = new_item_id
        else:
            raise TypeError(f'{new_item_id} is not a integer, Catagory must have a item ID')
 
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS catagories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            item_id INTEGER,
            FOREIGN KEY (item_id) REFERENCES item(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, par_id):
        catagory = cls(str(name), int(par_id))
        catagory.save()
        return catagory
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS catagories
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        catagory = cls.all.get(row[0])
        if catagory:
            catagory.name = row [1]
            catagory.item_id = row[2]
            
        else:
            catagory = cls(str(row[1]),  int(row[2]))
            catagory.id = row[0]
            cls.all[catagory.id] = catagory
        return catagory
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM catagories
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM catagories
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM catagories
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO catagories(name, item_id)
            VALUES (?,?)
        """    
        CURSOR.execute(sql, (self.name, self.item_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE catagories
            SET name=?, item_id=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM catagories
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       