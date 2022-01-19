import time

X = 1#USED FOR SLEEP

# allow user to enter list of numbers ?
# use 3 selectible algorithms to order them
#ALLOW UPLOAD OF DATA FILE 
# add UI maybe
def bubbleSort(nts):
 
    nts_len = len(nts)
 
    for i in range(nts_len):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]: # change to < for descending
                nts[p], nts[p + 1] = nts[p + 1], nts[p]
    return nts
                                
                

def selectionSort(nts): #https://stackabuse.com/selection-sort-in-python/ CODE FOR THIS ALGO FROM HERE COULDNT FIND AN EXAMPLE ON TEAMS SO I TOOK THIS I WAS GOING TO MAKE MY OWN BUT THIS IS REALLY HARD
    # i indicates how many items were sorted
    for i in range(len(nts)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(nts)-1):
            # Update the min_index if the element at j is lower than it
            if nts[j] < nts[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        nts[i], nts[min_index] = nts[min_index], nts[i]

def insertionSort(nts):
 
    print("Just used insertion sort")
 
    for i in range(1, len(nts)):
        current_num = nts[i]
        p = i - 1
 
        while p >= 0 and nts[p] > current_num:
            nts[p + 1] = nts[p]
            p -= 1
 
        nts[p + 1] = current_num
    return nts
    


#THIS IS PROBABLY NOT NEEDED ANYMORE
def list_maker(): #THIS MAKES USER INPUT INTO A LIST SO ITS EASIER TO WORK WITH, IT ALSO REMOVES THE  COMMAS
    list = nts.split(",")
    print(list)
    pass
#THIS IS PROBABLY NOT NEEDED ANYMORE    



print("ENTER DATA LIKE THIS: 10,13,123,1234,45454")
time.sleep(X)#SLEEPS FOR X SECONDS MAKES THE USER HAVE TO READ LOL
nts = input("ENTER DATA TO BE SORTED ")
#nts.append(data)
#print(nts)

f = open("unsorted.txt","w")#OPENS THE TXT FILE IN WRITE 
f.write(nts)#WRITES THE DATA TO THE FILES
f.close()#CLOSES IT

time.sleep(X)#SLEEPS FOR X SECONDS MAKES THE USER HAVE TO READ LOL
#list_maker()#THIS MAKES USER INPUT INTO A LIST SO ITS EASIER TO WORK WITH, IT ALSO REMOVES THE  COMMAS

print("1 = Bubble")
print("2 = Select")
print("3 = Insertion")
time.sleep(X)

choice = input("WHAT ALGO WILL BE USED? ")

if choice == "1":
    #BUBBLE SORT
    my_list_of_string_integers = nts.split(",")
    my_list_of_ints = [ int(val)  for val in my_list_of_string_integers]
    nts = bubbleSort(my_list_of_ints)

    
elif "2":
    #select
    my_list_of_string_integers = nts.split(",")
    my_list_of_ints = [ int(val)  for val in my_list_of_string_integers]
    nts = bubbleSort(my_list_of_ints)
    selectionSort(nts)
    print(nts)


elif "3":
    #insertionSort()
    my_list_of_string_integers = nts.split(",")
    my_list_of_ints = [ int(val)  for val in my_list_of_string_integers]
    nts = insertionSort(my_list_of_ints)
    insertionSort(nts)
    print(nts)

print(F"Sorted output = {nts}")
print("Done!")


# CODED BY NEO WITH A LITTLE HELP FROM FAMILY.
