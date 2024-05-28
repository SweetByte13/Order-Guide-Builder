from models.__init__ import CURSOR, CONN
from models.proveyer import Proveyer


class Proveyer_Item:
    all = {}
    
    def __init__(self, name, proveyer_id, price, case_size):
        self.name = name
        self.proveyer_id = proveyer_id
        self.price = price
        self.case_size = case_size
        
    def __repr__(self):
        return f"<Proveyer item {self.id}: {self.name}, {self.proveyer_id}, {self.price}, {self.case_size}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if  isinstance (name, str) and not hasattr(self, 'new_name'):
            self._name = name
        else:
            raise TypeError(f'{name} is not a string.')
        
    @property
    def proveyer_id(self):
        return self._proveyer_id
    
    @proveyer_id.setter
    def proveyer_id(self, proveyer_id):
        if  isinstance (proveyer_id, int) and Proveyer.find_by_id(proveyer_id):
            self._proveyer_id = proveyer_id
        else:
            raise TypeError(f'{proveyer_id} is not a integer, Proveyer_Item must have a proveyer ID')
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if  isinstance (new_price, int):
            self._price= new_price
        else:
            raise TypeError(f'{new_price} is not a integer, Proveyer_Item must have a price')
        
    @property
    def case_size(self):
        return self._case_size
    
    @case_size.setter
    def case_size(self, new_case_size):
        if  isinstance (new_case_size, int):
            self._case_size= new_case_size
        else:
            raise TypeError(f'{new_case_size} is not a integer, Proveyer_Item must have a case size')
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS proveyer_item (
            id INTEGER,
            name TEXT,
            proveyer_id INTEGER,
            price INTEGER,
            case_size INTEGER,
            FOREIGN KEY (proveyer_id) REFERENCES proveyer(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
            
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS proveyer_item;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO proveyer_item (name, proveyer_id, price, case_size)
                VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.proveyer_id, self.price, self.case_size))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE proveyer_item
            SET name = ?, proveyer_id = ?, price = ?, case_size = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.proveyer_id, self.price,
                             self.case_size, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM proveyer_item
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, proveyer_id, price, case_size):
        proveyer_item = cls(name, int(proveyer_id), price, case_size)
        proveyer_item.save()
        return proveyer_item

    @classmethod
    def instance_from_db(cls, row):
        proveyer_item = cls.all.get(row[0])
        if proveyer_item:
            proveyer_item.id=row[0]
            proveyer_item.name=row[1]
            proveyer_item.proveyer_id = row[2]
            proveyer_item.price = row[3]
            proveyer_item.case_size = row[4]
        else:
            proveyer_item = cls(row[1], row[2], row[3], row[4])
            proveyer_item.id = row[0]
            cls.all[proveyer_item.id] = proveyer_item
        return proveyer_item

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM proveyer_item
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM proveyer_item
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_proveyer_id(cls, proveyer_id):
        sql = """
            SELECT *
            FROM proveyer_item
            WHERE proveyer_id is ?
        """

        row = CURSOR.execute(sql, (proveyer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None