class Packet:

    def __init__(self):
        """Creates a class for all packets (IPC2 or ACL2) in the text file, with an added field for validity..

        Args:
        - self: this index, the one to create. mandatory object reference.

        Returns:
        None.
        """

        self.count = 0
        self.packets = []

    def get_packets(self, filepath):

        with open(filepath) as file:

            for iteration, line in enumerate(file):

                line = line.split()

                self.packets.append([iteration, int(line[0]), int(line[1]), int(
                    line[2]), int(line[3]), int(line[4]), int(line[5])])

                self.count = iteration
