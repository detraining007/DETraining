def get_user_input():
    try:
        total_mangoes = int(input("Enter total number of mangoes: "))
        total_bags = int(input("Enter total number of bags: "))
        return total_mangoes, total_bags
    except ValueError:
        print("Please enter valid integers.")
        exit(1)

def distribute_mangoes(total, bags):
    base = total // bags
    remainder = total % bags
    
    # Create dictionary with base values===0h
    distribution = {f"Bag {i+1}": base for i in range(bags)}
    
    # Distribute remainder to first 'remainder' bags
    for i in range(remainder):
        bag_key = f"Bag {i+1}"
        distribution[bag_key] += 1
    
    return distribution

def print_distribution(distribution):
    print("\nMango distribution across bags:")
    for bag, count in distribution.items():
        print(f"{bag}: {count} mangoes")

def main():
    total_mangoes, total_bags = get_user_input()
    distribution = distribute_mangoes(total_mangoes, total_bags)
    print_distribution(distribution)

if __name__ == "__main__":
    main()
