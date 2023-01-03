
import os


## cloud related variables
API_KEY = os.getenv('API_KEY',None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
#API_KEY="CZEAP7XBLSR7XK6K"
#API_SECRET_KEY="r8JFUw9+bzg6ec9BbjnfMPcA8GXu86HVnZ2oh3MMurcViWDTT/z+gwEQ/iukPFEz"
#BOOTSTRAP_SERVER="pkc-41p56.asia-south1.gcp.confluent.cloud:9092"

## Authentication related variables
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SECURITY_PROTOCOL="SASL_SSL"
# SSL_MACHENISM="PLAIN"

# schema related variables
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
#SCHEMA_REGISTRY_API_KEY="EOH5DQVNRENQ2UGG"
#SCHEMA_REGISTRY_API_SECRET="iXoOevC3RaZsE23H7ckbVa7+oO1DyNxqsEG58RJEXpJXXAAAC7CTS/v0qEc4MNyN"
#ENDPOINT_SCHEMA_URL="https://psrc-10dzz.ap-southeast-2.aws.confluent.cloud"

def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

