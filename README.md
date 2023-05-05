# post_formatter
```python
from normalizer import V2PostNormalizer
from elastic_formatter import PostFormatter

normalizer = V2PostNormalizer()
es_formatter = PostFormatter()

message = []
for post in posts:
    # Get id of post
    temp_post = {"id": post["_id"]["$oid"]}
    # Normalize content before forwarding it through model 
    temp_post['content'] = " ".join(normalizer.v2_normalize(post['content']))
    message.append(temp_post)
    
# Convert JSON type to string type
message = json.dumps(message)
result = stub.IntentSlotRecognize(intent_slot_service_pb2.IntentSlotRecognizeRequest(message=message))

# Convert string type to JSON type, After that, Call PostFormatter to format to Elastic Search standard.
print(es_formatter.get_activities(json.loads(result.message)))
```
