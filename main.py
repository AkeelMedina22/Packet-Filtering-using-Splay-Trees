from Rule_Set import Rule_Set
from Packet import Packet
from Skip_List import SkipList
from splaytree import SplayTree
import matplotlib.pyplot as plt
import numpy as np
import time

# ACL2 IP Packets and Rule Set

rules = Rule_Set()
rules.get_rules("Data_set/acl2/acl2_8k/acl2-8k.txt")

packet_8k = Packet()
packet_8k.get_packets("Data_set/acl2/acl2_8k/acl8k_header8k/skewness 0.txt")

packet_32k = Packet()
packet_32k.get_packets("Data_set/acl2/acl2_8k/acl8k_header32k/skewness 0.txt")

packet_128k = Packet()
packet_128k.get_packets(
    "Data_set/acl2/acl2_8k/acl8k_header128/skewness 0.txt")

# ICP2 IP Packets and Rule Set

# rules = Rule_Set()
# rules.get_rules("Data_set/ip2/ipc2_8k/ipc2-8k.txt")

# packet_8k = Packet()
# packet_8k.get_packets("Data_set/ip2/ipc2_8k/ipc8k_header8k/skewness 0.txt")

# packet_32k = Packet()
# packet_32k.get_packets("Data_set/ip2/ipc2_8k/ipc8k_header32k/skewness 0.txt")

# packet_128k = Packet()
# packet_128k.get_packets(
#     "Data_set/ip2/ipc2_8k/ipc8k_header128k/skewness 0.txt")


# ##########################################################################################

# Start of Protocol Search Packet

print("Protocol Search: ")
print()

# Skip List

skip_rules = SkipList()

for i, j in rules.protocol.items():
    skip_rules.insert(i, j)

skip_times = []


start = time.time()
output = []

for j in packet_8k.packets:

    if skip_rules.find(j[5]):
        output.append(j[0])

end = time.time()

skip_times.append(end-start)

print("Time 8k Skip List: ", end-start)

start = time.time()
output = []

for j in packet_32k.packets:

    if skip_rules.find(j[5]):
        output.append(j[0])

end = time.time()

skip_times.append(end-start)

print("Time 32k Skip List: ", end-start)

start = time.time()
output = []

for j in packet_128k.packets:

    if skip_rules.find(j[5]):
        output.append(j[0])

end = time.time()

skip_times.append(end-start)

print("Time 128k Skip List: ", end-start)
print()

plt.scatter([8, 32, 128], skip_times, color='red')
plt.plot([8, 32, 128], skip_times, color='red')


# ##################################################################################

# Splay Tree Protocol Search

splay_rules = SplayTree()

for i, j in rules.protocol.items():
    splay_rules.insert(i, j)

splay_times = []

start = time.time()
output = []

for j in packet_8k.packets:

    if splay_rules.find(j[5]):
        output.append(j[0])

end = time.time()

splay_times.append(end-start)

print("Time 8k Splay tree: ", end-start)

start = time.time()
output = []

for j in packet_32k.packets:

    if splay_rules.find(j[5]):
        output.append(j[0])

end = time.time()

splay_times.append(end-start)

print("Time 32k splay tree: ", end-start)

start = time.time()
output = []

for j in packet_128k.packets:

    if isinstance(splay_rules.find(j[5]), int):
        output.append(j[0])

end = time.time()

splay_times.append(end-start)

print("Time 128k splay tree: ", end-start)
print()

plt.scatter([8, 32, 128], splay_times, color='blue')
plt.plot([8, 32, 128], splay_times, color='blue')

labels = ['Skip List', 'Splay Tree']
plt.legend(labels=labels)

plt.ylabel("Time")
plt.xlabel("Number of Packets")
plt.title("Protocol Search")

plt.show()

##################################################################################

# Start of IP Packet Search

print("IP Packet Search: ")
print()

# Skip List

source_IP_skip_rules = SkipList()
dest_IP_skip_rules = SkipList()
source_Port_skip_rules = SkipList()
dest_Port_skip_rules = SkipList()
protocol_skip_rules = SkipList()


for i, j in rules.source_IP.items():
    source_IP_skip_rules.insert(int(i), j)
for i, j in rules.dest_IP.items():
    dest_IP_skip_rules.insert(int(i), j)
for i, j in rules.source_Port.items():
    source_Port_skip_rules.insert(int(i), j)
for i, j in rules.dest_Port.items():
    dest_Port_skip_rules.insert(int(i), j)
for i, j in rules.protocol.items():
    protocol_skip_rules.insert(int(i), j)


start = time.time()
output = []

skip_times = []

for j in packet_8k.packets:

    if source_IP_skip_rules.find(j[1]) and dest_IP_skip_rules.find(j[2]) and \
       source_Port_skip_rules.find(j[3]) and dest_Port_skip_rules.find(j[4]) and \
       protocol_skip_rules.find(j[5]):

        output.append(j[0])

end = time.time()
skip_times.append(end-start)

print("Time 8k Skip List: ", end-start)

try:
    file = open("Data_set/acl2/acl2_8k/acl8k_header8k/SkipListFilter.txt", "x")
except:
    file = open("Data_set/acl2/acl2_8k/acl8k_header8k/SkipListFilter.txt", "w")

for element in output:
    packet = [str(i) for i in packet_8k.packets[element][1:]]
    file.write(" ".join(packet) + "\n")
file.close()


start = time.time()
output = []

for j in packet_32k.packets:

    if source_IP_skip_rules.find(j[1]) and dest_IP_skip_rules.find(j[2]) and \
       source_Port_skip_rules.find(j[3]) and dest_Port_skip_rules.find(j[4]) and \
       protocol_skip_rules.find(j[5]):

        output.append(j[0])

end = time.time()

skip_times.append(end-start)

print("Time 32k Skip List: ", end-start)


try:
    file = open("Data_set/acl2/acl2_8k/acl8k_header32k/SkipListFilter.txt", "x")
except:
    file = open("Data_set/acl2/acl2_8k/acl8k_header32k/SkipListFilter.txt", "w")

for element in output:
    packet = [str(i) for i in packet_32k.packets[element][1:]]
    file.write(" ".join(packet) + "\n")
file.close()


start = time.time()
output = []

for j in packet_128k.packets:

    if source_IP_skip_rules.find(j[1]) and dest_IP_skip_rules.find(j[2]) and \
       source_Port_skip_rules.find(j[3]) and dest_Port_skip_rules.find(j[4]) and \
       protocol_skip_rules.find(j[5]):

        output.append(j[0])

end = time.time()

skip_times.append(end-start)

print("Time 128k Skip List: ", end-start)
print()

try:
    file = open("Data_set/acl2/acl2_8k/acl8k_header128/SkipListFilter.txt", "x")
except:
    file = open("Data_set/acl2/acl2_8k/acl8k_header128/SkipListFilter.txt", "w")

for element in output:
    packet = [str(i) for i in packet_128k.packets[element][1:]]
    file.write(" ".join(packet) + "\n")
file.close()

plt.scatter([8, 32, 128], skip_times, color='red')
plt.plot([8, 32, 128], skip_times, color='red')

##################################################################################

# Splay Tree

source_IP_splay_rules = SplayTree()
dest_IP_splay_rules = SplayTree()
source_Port_splay_rules = SplayTree()
dest_Port_splay_rules = SplayTree()
protocol_splay_rules = SplayTree()


for i, j in rules.source_IP.items():
    source_IP_splay_rules.insert(int(i), j)
for i, j in rules.dest_IP.items():
    dest_IP_splay_rules.insert(int(i), j)
for i, j in rules.source_Port.items():
    source_Port_splay_rules.insert(int(i), j)
for i, j in rules.dest_Port.items():
    dest_Port_splay_rules.insert(int(i), j)
for i, j in rules.protocol.items():
    protocol_splay_rules.insert(int(i), j)


start = time.time()
output = []

splay_times = []

for j in packet_8k.packets:

    if source_IP_splay_rules.find(j[1]) and dest_IP_splay_rules.find(j[2]) and \
       source_Port_splay_rules.find(j[3]) and dest_Port_splay_rules.find(j[4]) and \
       protocol_splay_rules.find(j[5]):

        output.append(j[0])

end = time.time()
splay_times.append(end-start)

print("Time 8k Splay tree: ", end-start)

try:
    file = open("Data_set/acl2/acl2_8k/acl8k_header8k/SplayTreeFilter.txt", "x")
except:
    file = open("Data_set/acl2/acl2_8k/acl8k_header8k/SplayTreeFilter.txt", "w")

for element in output:
    packet = [str(i) for i in packet_8k.packets[element][1:]]
    file.write(" ".join(packet) + "\n")
file.close()

start = time.time()
output = []

for j in packet_32k.packets:

    if source_IP_splay_rules.find(j[1]) and dest_IP_splay_rules.find(j[2]) and \
       source_Port_splay_rules.find(j[3]) and dest_Port_splay_rules.find(j[4]) and \
       protocol_splay_rules.find(j[5]):

        output.append(j[0])

end = time.time()

splay_times.append(end-start)

print("Time 32k splay tree: ", end-start)

try:
    file = open("Data_set/acl2/acl2_8k/acl8k_header32k/SplayTreeFilter.txt", "x")
except:
    file = open("Data_set/acl2/acl2_8k/acl8k_header32k/SplayTreeFilter.txt", "w")

for element in output:
    packet = [str(i) for i in packet_32k.packets[element][1:]]
    file.write(" ".join(packet) + "\n")
file.close()

start = time.time()
output = []

for j in packet_128k.packets:

    if source_IP_splay_rules.find(j[1]) and dest_IP_splay_rules.find(j[2]) and \
       source_Port_splay_rules.find(j[3]) and dest_Port_splay_rules.find(j[4]) and \
       protocol_splay_rules.find(j[5]):

        output.append(j[0])

end = time.time()

splay_times.append(end-start)

print("Time 128k splay tree: ", end-start)

try:
    file = open(
        "Data_set/acl2/acl2_8k/acl8k_header128/SplayTreeFilter.txt", "x")
except:
    file = open(
        "Data_set/acl2/acl2_8k/acl8k_header128/SplayTreeFilter.txt", "w")

for element in output:
    packet = [str(i) for i in packet_128k.packets[element][1:]]
    file.write(" ".join(packet) + "\n")
file.close()

plt.scatter([8, 32, 128], splay_times, color='blue')
plt.plot([8, 32, 128], splay_times, color='blue')

labels = ['Skip List', 'Splay Tree']
plt.legend(labels=labels)

plt.ylabel("Time")
plt.xlabel("Number of Packets")
plt.title("IP Packet Search")

plt.show()
