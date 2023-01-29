import os.path
from configparser import ConfigParser

class Check:
    def __init__(self):
        self.admin_id : str = '258896976'
        self.adm_list = 'list/admin.list'
        self.not_list = 'list/notify.ini'
        self.readDataPaths()


    def createList(self, lists : list):
        with open(lists[0], 'w') as adm_list:
            adm_list.write(f'{self.admin_id}\n')
            adm_list.close()
        config = ConfigParser()
        config.add_section('users')
        config.set('users', f'{self.admin_id}','false')
        with open(lists[1], 'w') as config_file:
            config.write(config_file)


    def readDataPaths(self):
        if not os.path.exists(self.adm_list) and not os.path.exists(self.not_list):
            self.createList([self.adm_list,self.not_list])

