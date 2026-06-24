from rag import retrieve_context


query = "What is supervised learning?"

context = retrieve_context(query)

print("\nRetrieved Context:\n")
print(context)