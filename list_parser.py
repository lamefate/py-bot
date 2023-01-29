from configparser import ConfigParser

class Parser:
    def __init__(self):
        self.adm_list = 'list/admin.list'
        self.not_list = 'list/notify.ini'


    def newBotUser(self, uid):
        config = ConfigParser()
        config.read(self.not_list)
        config.set('users', f'{uid}', 'false')
        with open(self.not_list, 'w') as config_file:
            config.write(config_file)


    def updateNotifyList(self, uid):
        config = ConfigParser()
        config.read(self.not_list)
        notify_status = config.get('users', f'{uid}')
        if notify_status == 'true':
            config.set('users', f'{uid}', 'false')
        elif notify_status == 'false':
            config.set('users', f'{uid}', 'true')
        with open(self.not_list, 'w') as config_file:
            config.write(config_file)
        
        return notify_status
    
    def updateAdminList(self, uid):
        with open(self.adm_list, 'a+') as new_adm_list:
            new_adm_list.write(f'{uid}\n')
            new_adm_list.close()


#parser = Parser()
#parser.updateNotifyList()