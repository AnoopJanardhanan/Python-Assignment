# # Topic :List Exercise Q1. Create a list of 5 random numbers and print the list.
# import random
# print([random.randint(1, 100) for i in range(5)])


# # Q2. Insert 3 new values to the list and print the updated list.
# import random
# random_numbers = [random.randint(1, 100) for i in range(5)]
# new_values = [10, 20, 30]
# random_numbers.extend(new_values)
# print(random_numbers)


# # Q3. Try to use a for loop to print each element in the list.
# import random
# random_numbers = [random.randint(1, 100) for i in range(5)]
# random_numbers += [10, 20, 30]
# for i in random_numbers:
#     print(i)


# # Topic: Dictionary Exercise Q1. Create a dictionary with keys 'name', 'age', and 'address' and
# # values 'John', 25, and 'New York' respectively.
# person = {'name': 'John', 'age': 25, 'address': 'New York'}
# print(person)



# # Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
# person = {'name': 'John', 'age': 25, 'address': 'Kerala'}
# person['phone'] = '9467987654'
# print(person)


# # Topic: Set Exercise Q1.Create a set with values 1, 2, 3, 4, and 5.
# m_set = {1, 2, 3, 4, 5}
# print(m_set)


# # Q2. Add the value 6 to the set created in Q1.
# m_set = {1, 2, 3, 4, 5}
# m_set.add(6)
# print(m_set)


# # Q3. Remove the value 3 from the set created in Q1.
# m_set = {1, 2, 3, 4, 5}
# m_set.remove(3)
# print(m_set)


# # Topic:Tuple Exercise Q1.Create a tuple with values 1, 2, 3, and 4
# m_tuple = (1, 2, 3, 4)
# print(m_tuple)


# # Q2. Print the length of the tuple created in Q1.
# m_tuple = (1, 2, 3, 4)
# print(len(m_tuple))








