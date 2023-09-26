from decouple import config

class Config():
  TOKEN_KEY = config('TOKEN')

class DevelopmentConfig():
  DEBUG = True

config = {
  'development':DevelopmentConfig
}