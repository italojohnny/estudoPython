import ConfigParser

class Config (object):

    def __init__ (self, filePath="./myconfig.conf"):
        self.filePath = filePath
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.filePath)


    def __del__ (self):
        self.save()


    def save (self):
        with open(self.filePath, 'w') as fileConfig:
            self.config.write(fileConfig)


    def get (self, section, option):
        try:
            return self.config.get(section, option)

        except ConfigParser.NoSectionError:
            self.config.add_section(section)
            return self.get(section, option)

        except ConfigParser.NoOptionError:
            self.set(section, option, None)
            return self.get(section, option)


    def set (self, section, option, value):
        try:
            self.config.set(section, option, value)

        except ConfigParser.NoSectionError:
            self.config.add_section(section)
            self.set(section, option, value)


if __name__ == "__main__":
    a = Config()
    a.set('fruta', 'banana', 10)
    print a.get('fruta', 'banana')


    print a.get('frunta', 'maca')
    print a.get('legumes', 'batata')

    a.set('carne', 'porco', 5)
    a.set('carne', 'vaca', 4)
