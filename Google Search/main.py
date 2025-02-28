from googlesearch import search

query = input("Enter query Search: ")

num_results = 10

print(f"Result for search: {query}")
for result in search(query, num_results):
    print(result)
