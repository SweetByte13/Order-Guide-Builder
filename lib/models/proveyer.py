from models.__init__ import CURSOR, CONN

class Proveyer:
    all = {}
    
    def __init__(self, name, catagory, cut_off_time, order_min):
        self.name = name
        self.catagory = catagory
        self.cut_off_time = cut_off_time
        self.order_min = order_min
        self.proveyer_catagories = []
        self.proveyer_items = []
        
    def __repr__(self):
        return f"<Proveyer {self.id}: {self.name}, {self.catagory}, {self.cut_off_time}, {self.order_min}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and not hasattr(self, 'name'):
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not a string, Proveyers must have a name')
        
    @property
    def catagory(self):
        return self._catagory
    
    @catagory.setter
    def catagory(self, new_catagory):
        if isinstance (new_catagory, str) and not hasattr(self, 'catagory'):
            self._catagory = new_catagory
        else:
            raise TypeError(f'{new_catagory} is not a string, Proveyers must have a catagory')
        
    @property
    def cut_off_time(self):
        return self._cut_off_time
    
    @cut_off_time.setter
    def cut_off_time(self, new_cut_off_time):
        if isinstance (new_cut_off_time, int):
            self._cut_off_time = new_cut_off_time
        else:
            raise TypeError(f'{new_cut_off_time} is not a integer, Proveyers must have a cut off time')
        
    @property
    def order_min(self):
        return self._order_min
    
    @order_min.setter
    def order_min(self, new_order_min):
        if isinstance (new_order_min, int):
            self._order_min = new_order_min
        else:
            raise TypeError(f'{new_order_min} is not a integer, Proveyers must have a order minimum')    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS proveyers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            catagory TEXT,
            cut_off_time INTEGER,
            order_min INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, catagory, cut_off_time, order_min):
        proveyer = cls(str(name), str(catagory), int(cut_off_time), int(order_min))
        proveyer.save()
        return proveyer
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS proveyers
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        proveyer = cls.all.get(row[0])
        if proveyer:
            proveyer.cut_off_time = row[3]
            proveyer.order_min = row[4]
        else:
            proveyer = cls(str(row[1]), str(row[2]), int(row[3]), int(row[4]))
            proveyer.id = row[0]
            cls.all[proveyer.id] = proveyer
        return proveyer
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM proveyers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM proveyers
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM proveyers
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO proveyers(name, catagory, cut_off_time, order_min)
            VALUES (?,?,?,?)
        """    
        CURSOR.execute(sql, (self.name, self.catagory, self.cut_off_time, self.order_min))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE proveyers
            SET cut_off_time=?, order_min=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.cut_off_time, self.order_min, self.id))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM proveyers
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
        
    def get_items(self):
        # from models.proveyer_item import Proveyer_Item
        sql = """
            SELECT * FROM proveyer_item pi JOIN
            items i ON pi.item_id = i.id
            WHERE pi.proveyer_id=?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        # [id , name, item_id, proveyer_id, price, case_size  # id, name, par_id, catagory_id]
        items=[]
        for row in rows:
            items.append({(row[1], row[2], row[3], row[4], row[5], row[8], row[9])})
        return (items)
            
            
            
            