from os import environ


#clases principales para las etapa de desarrollo 

class Development(BaseConfig):
    ''' Development config. '''

    DEBUG = True
    ENV = 'dev'


class Staging(BaseConfig):
    ''' Staging config. '''

    DEBUG = True
    ENV = 'staging'


class Production(BaseConfig):
    ''' Production config '''

    DEBUG = False
    ENV = 'production'


config = {
    'development': Development,
    'staging': Staging,
    'production': Production,
}