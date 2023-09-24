import os
import inspect

class HanglingPath():
    # --------------------------------------------------
    def get_modules_path(self):
        dir_path = os.path.dirname(
            os.path.abspath(
                inspect.getfile(
                    inspect.currentframe())))
        return dir_path

    # --------------------------------------------------
    def get_invicoliqpy_path(self):
        dir_path = self.get_modules_path()
        dir_path = os.path.dirname(dir_path)
        return dir_path

    # --------------------------------------------------
    def get_src_path(self):
        dir_path = self.get_invicoliqpy_path()
        dir_path = os.path.dirname(dir_path)
        return dir_path

    # --------------------------------------------------
    def get_outside_path(self):
        dir_path = os.path.dirname(os.path.dirname(self.get_src_path()))
        return dir_path

    # --------------------------------------------------
    def get_db_path(self):
        self.db_path = (self.get_outside_path() 
                        + '/Python Output/SQLite Files')
        return self.db_path

    # --------------------------------------------------
    def get_update_path_input(self):
        dir_path = (self.get_outside_path() 
                    + '/invicoDB/Base de Datos')
        return dir_path