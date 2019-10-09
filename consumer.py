from kafka import KafkaConsumer
consumer = KafkaConsumer('twitter-topic')
for msg in consumer:
    print (msg)