def chunking_items(items , no_boxes):
    boxes =[]

    for i in range(no_boxes):
        boxes.append([])

    for i in range(items):
        boxes[i%no_boxes].append(f"item {i+1}")

    return boxes

items = int(input("Enter No. of Items"))
no_boxes = int(input("Enter no. of boxes"))

result = chunking_items(items,no_boxes)

for row in result:
    print(row)