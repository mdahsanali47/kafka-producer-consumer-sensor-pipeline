import os
if __name__ == '__main__':
     API_KEY = os.getenv('API_KEY',None)
     ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL')
     API_SECRET_KEY = os.getenv('API_SECRET_KEY')
     BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER')
     SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL')
     SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
     SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY')
     SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET')
     MONGO_DB_URL= os.getenv('MONGO_DB_URL')
     print(API_KEY)
     print(MONGO_DB_URL)



