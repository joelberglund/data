from kafka import KafkaConsumer
import json
consumer = KafkaConsumer('twitter-topic', group_id='my-group')

for msg in consumer:
    hej = json.loads(msg.value)['text']
    print (json.loads(msg.value)['text'])
