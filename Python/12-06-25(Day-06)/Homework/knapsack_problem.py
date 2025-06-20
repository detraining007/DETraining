#To solve a b balls in n bags problem problem

# bags=int(input("Enter number of bags: "))
# balls=int(input("Enter number of balls: "))
# chunk=balls//bags
# remaining_balls=balls%bags

# chunks_lst=[]
# def bag_list():
#     if bags<balls:

#         for i in range(bags):
#             if i<remaining_balls:
#                 chunks_lst.append(chunk+1)
#             else:
#                 chunks_lst.append(chunk)



# if __name__=="__main__":
#     bag_list()
#     print(chunks_lst)



def distribute_balls(bags, balls):
    if bags <= 0 or balls <= 0:
        return []

    
    used_bags = min(bags, balls)

    
    distribution = [1] * used_bags


    remaining = balls - used_bags
    i = 0
    while remaining > 0:
        distribution[i % used_bags] += 1
        remaining -= 1
        i += 1

    return distribution


if __name__ == "__main__":
    try:
        bags = int(input("Enter number of bags: "))
        balls = int(input("Enter number of balls: "))

        distribution = distribute_balls(bags, balls)
        if not distribution:
            print("No distribution possible.")
        else:
            print("Balls in used bags:", distribution)
            print("Balls in Unused bags:", bags - len(distribution))
            print("Number of unused bags: ",bags- )

    except ValueError:
        print("Please enter valid integers.")



    

