from pymilvus import MilvusClient

# Connect to a Milvus server instead of using lite
client = MilvusClient("http://localhost:19530")

if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
    print("Dropped collection demo_collection")

# client.create_collection(
#     collection_name="demo_collection",
#     dimension=768,  # The vectors we will use in this demo has 768 dimensions
# )

client.list_collections()
