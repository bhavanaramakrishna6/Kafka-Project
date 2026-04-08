from kafka import KafkaConsumer
import json
from collections import defaultdict

consumer = KafkaConsumer(
    'clicks',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='debug-group'
)

counts = defaultdict(int)

print("Listening for clicks...\n")

for message in consumer:
    try:
        data = json.loads(message.value.decode('utf-8'))
        user = data.get('user')

        if user:
            counts[user] += 1

            print("Current Counts:")
            for u, c in counts.items():
                print(f"{u}: {c}")
            top_user = max(counts, key=counts.get)
            print(f"🔥 Top User: {top_user} ({counts[top_user]} clicks)")
            print("-" * 20)

    except:
        continue
