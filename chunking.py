def chunk_list(lst, chunk_size):
    """Yield successive chunks from lst of size chunk_size."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for chunk in chunk_list(my_list, 5):
    print(chunk)