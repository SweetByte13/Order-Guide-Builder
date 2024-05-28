from models.__init__ import CURSOR, CONN


class Department:
    all = {}
    
    def __init__(self, name, par_id):
        self.name = name
        self.par_id = par_id
        
    def __repr__(self):
        return f"<Par {self.id}: {self.name}, {self.par_id}>"
    
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
    def par_id(self):
        return self._par_id
    
    @par_id.setter
    def par_id(self, new_par_id):
        if isinstance (new_par_id, int):
            self._par_id = new_par_id
        else:
            raise TypeError(f'{new_par_id} is not a integer, Department must have a par ID')
 
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            par_id INTEGER,
            FOREIGN KEY (par_id) REFERENCES par(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, par_id):
        department = cls(str(name), int(par_id))
        department.save()
        return department
    
    @classmethod    
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.name = row [1]
            department.par_id = row[2]
            
        else:
            department = cls(str(row[1]),  str(row[2]))
            department.id = row[0]
            cls.all[department.id] = department
        return department
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM departments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM departments
            WHERE id=?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def save(self):
        sql = """
            INSERT INTO departments(name, par_id)
            VALUES (?,?)
        """    
        CURSOR.execute(sql, (self.name, self.par_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE department
            SET name=?, par_id=?
            WHERE id=?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM department
            WHERE id=?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        self.id=None
       