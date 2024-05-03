import psycopg2
from psycopg2 import sql

class Campus:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def create_user_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                user_id VARCHAR(20) UNIQUE,
                role VARCHAR(20),
                image BYTEA
            )
        """)
        self.conn.commit()

    def add_user(self, user):
        sql_query = sql.SQL("""
            INSERT INTO users (name, user_id, role, image)
            VALUES (%s, %s, %s, %s)
        """)
        self.cur.execute(sql_query, (user.name, user.user_id, user.role, user.image))
        self.conn.commit()

    def remove_user(self, user_id):
        self.cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        self.conn.commit()

    def get_user_by_id(self, user_id):
        self.cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        row = self.cur.fetchone()
        if row:
            return row
        else:
            return None

    def list_users(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def list_users(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows

    def search_users(self, criteria):
       
        where_clause = []
        params = []
        for key, value in criteria.items():
            if key in ["name", "user_id", "role"]:
                where_clause.append(f"{key} LIKE %s")
                params.append(f"%{value}%")
        query = f"SELECT * FROM users WHERE {' AND '.join(where_clause)}"
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def update_user(self, user_id, updates):
        
        set_clause = []
        params = []
        for key, value in updates.items():
            if key in ["name", "role", "image"]:
                set_clause.append(f"{key} = %s")
                params.append(value)
        if not set_clause:
            return False
        query = f"UPDATE users SET {', '.join(set_clause)} WHERE user_id = %s"
        params.append(user_id)
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur.rowcount == 1 


    def get_list_of_activities(self):
        return "get_list_of_activities not implemented"
    
    def visualize_movements(self, start_time, end_time):
        movements_within_time = []
        for movement in self.movements:
            if start_time <= movement.time <= end_time:
                movements_within_time.append(movement)
        return movements_within_time

campus = Campus(dbname="test_db", user="root", password="root")

campus.create_user_table()
