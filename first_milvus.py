#
# small tool that creates a Milvus DB and does some insert/search/queries on it
# taken from the milvus tutorial
#
from pymilvus import MilvusClient
import random

client = MilvusClient("./milvus_demo.db")

client.create_collection(
    collection_name="demo_collection",
    dimension=384  # The vectors we will use in this demo has 384 dimensions
)

# Text strings to search from.
docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

# For illustration, here we use fake vectors with random numbers (384 dimension).
vectors = [[ random.uniform(-1, 1) for _ in range(384) ] for _ in range(len(docs)) ]
data = [ {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"} for i in range(len(vectors)) ]

print("=== CREATE COLLECTION ===")
res = client.insert(
    collection_name="demo_collection",
    data=data
)
print(res)


# Insert more docs in another subject.
docs = [
    "Machine learning has been used for drug design.",
    "Computational synthesis with AI algorithms predicts molecular properties.",
    "DDR1 is involved in cancers and fibrosis.",
]
vectors = [[ random.uniform(-1, 1) for _ in range(384) ] for _ in range(len(docs)) ]
data = [ {"id": 3 + i, "vector": vectors[i], "text": docs[i], "subject": "biology"} for i in range(len(vectors)) ]

print("=== UPDATE COLLECTION ===")
res = client.insert(
    collection_name="demo_collection",
    data=data
)
print(res)


print("=== SEARCH ===")
# This will exclude any text in "history" subject despite close to the query vector.
res = client.search(
    collection_name="demo_collection",
    data=[vectors[0]],
    filter="subject == 'biology'",
    limit=2,
    output_fields=["text", "subject"],
)
print(res)

print("=== QUERY ===")
# a query that retrieves all entities matching filter expressions.
res = client.query(
    collection_name="demo_collection",
    filter="subject == 'history'",
    output_fields=["text", "subject"],
)
print(res)

print("=== DELETE ===")
# delete
res = client.delete(
    collection_name="demo_collection",
    filter="subject == 'history'",
)
print(res)

print("=== DROP ===")
# delete
res = client.drop_collection(collection_name="demo_collection")
print(res)

