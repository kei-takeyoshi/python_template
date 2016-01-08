# -*- coding:utf-8 -*-

import app.models.db as db
import app.models.pager as pager
import app.models.student as student
import sqlalchemy
import sqlalchemy.ext.declarative

class Manga:

    # ==========================================
    # 
    # Get manga list
    # 
    # ==========================================

    def load(self, page):

#        student.delete(db.session, 'test taro', 'kana test')
#        student.insert(db.session, 'test taro', 'kana test')
#        student.update(db.session, 'test taro', 'sample test')
#        result = student.select(db.session, 'reizei mako')
        results = student.select_all(db.session)
#        for result in results:
#            return result
        return results


    # ==========================================
    # 
    # Get manga only
    # 
    # ==========================================
    def edit(self, id):

        sql = "select * from manga where id = %s"
        db.con.execute(sql, (id))
        return db.con.fetchone()


    # ==========================================
    # 
    # if there is a del flag, execute delete. if not, execute update.
    # if there is no id, insert new one.
    # 
    # ==========================================
    def done(self, params):

        if params["id"]:

            if params["del"]:
                sql = "delete from manga where id = %s"
                db.con.execute(sql, (params["id"]))
            else:
                sql = "update manga set "
                sql += " num=%s"
                sql += ",name=%s"
                sql += ",kana=%s"
                sql += ",regdate=CURRENT_TIMESTAMP"
                sql += " where id = %s"
                db.con.execute(sql, (
                                    params["num"],
                                    params["name"],
                                    params["kana"],
                                    params["id"]
                                    ))

        else:

            sql = "insert into manga (num, name, kana, regdate) values (%s, %s, %s, CURRENT_TIMESTAMP)"
            db.con.execute(sql, (
                                params["num"],
                                params["name"],
                                params["kana"],
                                ))

        db.dbhandle.commit()
        return
