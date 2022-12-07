with open('day6_input.txt') as f:
    data = f.readlines()

data = data[0][:-1] # we consider only the first (and only) line and we drop \n

pm_dim = 4 # length of packet starting code
packet_marker = []
packet_found = False

mm_dim = 14 # length of message starting code
message_marker = []

for i, val in enumerate(data):
    # check for starting packet token, 4 different digits
    if not packet_found:
        packet_marker.append(val)
        # we convert to a set: since sets can only contain only one element
        # per kind, we have len(set) = len(list) if and only if list contains
        # only different elements
        if len(set(packet_marker)) == pm_dim:
            # enumerate starts from 0, but we want positions à la MatLab
            pm_pos = i+1
            packet_found = True # stops the search for packet stating sequence
        elif len(packet_marker) >= pm_dim:
            # the first element of the analyzed block is dropped to create
            # space for the next character and have a list of dimension 4 all
            # the time
            packet_marker = packet_marker[1:]

    # check for start message token, 14 different digits
    message_marker.append(val)
    # we convert to a set: since sets can only contain only one element
    # per kind, we have len(set) = len(list) if and only if list contains
    # only different elements
    if len(set(message_marker)) == mm_dim:
        # enumerate starts from 0, but we want positions à la MatLab
        mm_pos = i+1
        # message marker strictly contains packet marker, thus we stop
        # our search algorithm
        break
    elif len(message_marker) >= mm_dim:
        # the first element of the analyzed block is dropped to create
        # space for the next character and have a list of dimension 14 all
        # the time
        message_marker = message_marker[1:]

print(f'the packet marker is at position {pm_pos}')
print(f'the message marker is at position {mm_pos}')
