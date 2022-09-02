with open('contacts.csv', 'r') as f:
    data_csv = f.read()

# csv_lines = data_csv.split("\n")
# list_of_lists = []
# for line in csv_lines:
#     list_of_lists.append(line.split(','))
list_of_lists = [line.split(',') for line in data_csv.split('\n')]

keys = list_of_lists[0]
# contacts = []
# for row in list_of_lists[1::]:
#     row_dict = {}
#     # for i in range(len(row)):
#     #     row_dict[keys[i]] = row[i]
#     #     # row_dict['name'] = 'merritt'
#     #     # row_dict['favorite color'] = 'blue'
#     #     # row_dict['favorite fruit'] = 'apple'
#     for i, cell in enumerate(row):
#         row_dict[keys[i]] = cell
#     contacts.append(row_dict)

# print(list(zip(keys, list_of_lists[1])))
# print(dict(zip(keys, list_of_lists[1])))

# for i in range(1, len(list_of_lists)):
#     contacts.append(dict(zip(keys, list_of_lists[i])))

# for values in list_of_lists[1::]:
#     contacts.append(dict(zip(keys, values)))

contacts = [dict(zip(keys, values)) for values in list_of_lists[1::]]

# contacts = [dict(zip([line.split(',') for line in data_csv.split('\n')][0], values)) for values in [line.split(',') for line in data_csv.split('\n')][1::]]
        

def create_contact(data, keys):
    # new_contact = {}
    # for key in keys:
    #     new_contact[key] = input(f"What is your new contact's {key}? ")
    # data.append(new_contact)
    data.append({key: input(f"What is your new contact's {key}? ") for key in keys})

def read_contact(data, keys):
    # name = input("what is your contact's name? ")
    # for contact in data:
    #     if contact['name'] == name:
    #         for key in contact:
    #             print(f"{key}: {contact[key]}")
    #         return contact

    key_string = "\n" + "\n".join(keys) + "\n"
    key_input = input(f"What would you like to search by? Choose from: {key_string} ")
    contact_input = input("What is your search term? ")

    # data_results = []
    # for contact in data:
    #     if contact[key_input] == contact_input:
    #         data_results.append(contact)

    # data_results = [contact for contact in data if contact[key_input] == contact_input]
    # def filter_function(contact):
    #     return contact[key_input] == contact_input
    data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))

    print(data_results)

    return data_results


def update_contact(data, keys):
    # result = read_contact(data, keys)
    
    # key_to_update = input(f"What key would you like to update? {keys} ")
    # value_to_update = input(f"What do you want to change {key_to_update} to? ")
    # result[key_to_update] = value_to_update

    data_results = read_contact(data, keys)

    index_to_update = int(input(f"Which contact would you like to edit? (1-{len(data_results)}) ")) - 1
    key_to_update = input(f"What key would you like to update? {keys} ")
    value_to_update = input(f"What do you want to change {key_to_update} to? ")
    data_results[index_to_update][key_to_update] = value_to_update



def delete_contact(data, keys):
    # result = read_contact(data, keys)
    # confirmation = input(f"Are you sure you want to delete {result['name']}? ")
    # if confirmation.lower() in ['y', 'yes', 'true', 'go', 'do it']:
    #     data.remove(result)

    data_results = read_contact(data, keys)

    index_to_delete = int(input(f"Which contact would you like to delete? (1-{len(data_results)}) ")) - 1
    data.remove(data_results[index_to_delete])


while True:
    # print(contacts)
    user_input = input("What would you like to do? (c)reate, (r)ead, (u)pdate, (d)elete, (q)uit ")
    if user_input.lower() in ['q', 'quit', 'exit', 'stop']:
        break
    elif user_input == 'c':
        create_contact(contacts, keys)
    elif user_input == 'r':
        read_contact(contacts, keys)
    elif user_input == 'u':
        update_contact(contacts, keys)
    elif user_input == 'd':
        delete_contact(contacts, keys)
    
data_csv_out = []
data_csv_out.append(keys)
for contact in contacts:
    data_csv_out.append(list(contact.values()))

# data_csv_out = [list(contact.values()) for contact in contacts]
# data_csv_out.insert(0, keys)

# output = []
# for row in data_csv_out:
#     output.append(",".join(row))
# output_string = "\n".join(output)


data_csv_out = "\n".join([",".join(row) for row in data_csv_out])

with open('contacts.csv', 'w') as f:
    f.write(data_csv_out)
