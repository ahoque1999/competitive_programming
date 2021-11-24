list_of_handles = []
max_length_of_each_handle_chain = []

for iteration in range(int(input())):
    repost_inputs = input().split()
    reposter = repost_inputs[0].lower()
    repostee = repost_inputs[2].lower()

    if reposter not in list_of_handles:
        list_of_handles.append(reposter)
        max_length_of_each_handle_chain.append(1)
    
    if repostee not in list_of_handles:
        list_of_handles.append(repostee)
        max_length_of_each_handle_chain.append(1)
    
    repostee_name_index = list_of_handles.index(repostee)
    repostee_length = max_length_of_each_handle_chain[repostee_name_index]

    reposter_name_index = list_of_handles.index(reposter)
    reposter_length = max([max_length_of_each_handle_chain[reposter_name_index], repostee_length + 1]) 
    max_length_of_each_handle_chain[reposter_name_index] = reposter_length

print(max(max_length_of_each_handle_chain))    