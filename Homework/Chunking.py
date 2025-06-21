def Chunking():
    n = int(input("Enter number of items: "))
    k = int(input("Enter number of chunks: "))        
    chunks = [[] for _ in range(k)]
    for i in range(1, n + 1):
        chunks[(i - 1) % k].append("Item {i}")
    
    for chunk_number in range(len(chunks)):
        print("Chunk", chunk_number + 1, ":", end=" ")
        for item in chunks[chunk_number]:
            print(item, end=", ")
        print()  

if __name__ == "__main__": 
    Chunking()