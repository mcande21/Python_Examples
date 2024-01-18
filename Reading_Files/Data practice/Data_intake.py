import my_queue

# Opening the file into an object

f = open("car_financing.csv")




# iterationg through first line to grab catagories
catagories = my_queue.Queue()

catagories.enqueue("A")
catagories.enqueue("B")
catagories.enqueue("C")
print(catagories)