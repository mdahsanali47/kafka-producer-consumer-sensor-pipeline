# confluent-kafka-python

## This repo is about how to publish and consume data to and from kafka confluent in json format.

### Confluent Platform simplifies connecting data sources to Kafka, building streaming applications, as well as securing, monitoring, and managing your Kafka infrastructure


Here, we are not using any sensor data direct from sensor reading, instead we are streaming our own data:
 - first we will send the data (csv format stored in file "sample data") in json format to kafka producer.
 - then we will fetch the data from kafka consumer, and store it in mongodb
