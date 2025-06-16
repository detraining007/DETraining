

def distribution(total_balls, total_chunk):
    chunks = [total_balls // total_chunk]*total_chunk
    # print(chunks)
    remaining = total_balls % total_chunk
    # print(remaining)
    for i in range(remaining):
        chunks[i] += 1

    print(chunks)
    return chunks

def finnal(chunks):
    print("balls distributed across:")
    for i in range(len(chunks)):
        print(f"chunk{i+1} : {chunks[i]} balls")



def user_inputs():
    total_balls = int(input("how many balls do you want: "))
    total_chunk = int(input("how many bages do you need :"))
    return total_balls,total_chunk


if __name__ == "__main__":
    total_balls,total_chunk = user_inputs()
    print(total_balls)
    chunks=distribution(total_balls,total_chunk)
    finnal(chunks)


     

