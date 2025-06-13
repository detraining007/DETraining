def get_user_input():
    try:
        total_mangoes = int(input("Enter total number of mangoes: "))
        total_chunks = int(input("Enter total number of chunks: "))
        return total_mangoes, total_chunks
    except ValueError:
        print("Please enter valid integers.")
        exit(1)


def distribute_mangoes(total_mangoes, total_chunks):
    chunks = [total_mangoes // total_chunks] * total_chunks
    remaining = total_mangoes % total_chunks
    for i in range(remaining):
        chunks[i] += 1
    return chunks


def print_distribution(chunks):
    print("Mango distribution across chunks:")
    for i, count in enumerate(chunks):
        print(f"Chunk {i+1}: {count} mangoes")


def main():
    total_mangoes, total_chunks = get_user_input()
    chunks = distribute_mangoes(total_mangoes, total_chunks)
    print_distribution(chunks)
    return chunks


if __name__ == "__main__":
    main()