#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscpython@gmail.com>
Purpose: SQL methods
"""

from PySide6.QtSql import QSqlQuery
class SQLUtils():
    "Some generals methods"

    # --------------------------------------------------
    def sqlite_is_unique(self, db_table: str, field: str,
                        search_value) -> bool:
        query = QSqlQuery()
        query.exec_('PRAGMA foreign_keys = ON')
        query.prepare(f'SELECT * FROM {db_table} ' +
                    f'WHERE {field} = ?')
        query.bindValue(0, search_value)
        result = query.exec_()
        if result and query.first():
            return False
        else:
            return True

    # --------------------------------------------------
    def sqlite_get_query(self, db_table: str, field: str,
                        search_value):
        query = QSqlQuery()
        query.prepare(f'SELECT * FROM {db_table} ' +
                    f'WHERE {field} = ?')
        query.bindValue(0, search_value)
        result = query.exec_()
        if result and query.first():
            return query
        else:
            return None
