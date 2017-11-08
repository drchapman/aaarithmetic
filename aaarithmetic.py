#!/usr/bin/env python3

import sqlite3
import getpass

class aaa_parser:

    def __init__(self, db):
        self.connect(db)
        self.user=getpass.getuser()

    def connect(self, db):
        self.dbc = sqlite3.connect(db)
        self.dbcurs = self.dbc.cursor()

    def get_categories(self):
        # Return a categoriesion
        query = "select category_id, category from categories"
        results = self.dbcurs.execute(query)
        return results.fetchall()

    def get_set_list(self, category_id):
        # Return a list of sets in a selected category
        query = "select set_id, question_set from sets where category_id = ?"
        results = self.dbcurs.execute(query, str(category_id))
        return(results.fetchall())

    def begin_session(self,set_id):
        # Create an entry in the session list
        query = "insert into sessions (set_id, user_name) values (?, ?)"
        results = self.dbcurs.execute(query, (str(set_id), self.user))
        self.dbc.commit()
        return(self.dbcurs.lastrowid)

    def get_set_questions(self, set_id):
        # Return the list of questions in a selected set
        query = '''select q.q_id, q.question_text
                    from set_questions as s, questions as q
                    where 1=1
                    and s.set_id = ?
                    and s.q_id = q.q_id'''
        results = self.dbcurs.execute(query, (str(set_id)))
        return(results.fetchall())

    def attempt_question(self,session_id,q_id,answer):
        query = '''insert into attempts
                    (session_id, q_id, attempt_answer)
                    values
                    (?, ?, ?)'''
        result = self.dbcurs.execute(query, (str(session_id), str(q_id), answer))
        self.dbc.commit()
        attempt_id = self.dbcurs.lastrowid
        print(type(attempt_id))
        query2 = "select correct from attempts where attempt_id = ?"
        results = self.dbcurs.execute(query2, [str(attempt_id)]) #specify parameters as a list literal
        result_list = results.fetchone()
        return([attempt_id,result_list[0]])
