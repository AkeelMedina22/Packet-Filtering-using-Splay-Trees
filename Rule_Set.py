class Rule_Set:

    def __init__(self):
        """Creates a single rule set for IP2 packets based on 10 fields.

        Args:
        - self: this index, the one to create. mandatory object reference.

        Returns:
        None.
        """

        self.source_IP = {}
        self.dest_IP = {}
        self.source_Port = {}
        self.dest_Port = {}
        self.protocol = {}

        self.count = 0

    def get_rules(self, filepath):

        with open(filepath) as file:

            for iteration, line in enumerate(file):

                line = line.split()

                self.handle_Source_IP(line[0], iteration)
                self.handle_Dest_IP(line[1], iteration)

                self.handle_Source_Port(line[2]+line[3]+line[4], iteration)
                self.handle_Dest_Port(line[5]+line[6]+line[7], iteration)

                self.handle_protocol(line[8], iteration)

                self.count = iteration

    def handle_Source_IP(self, IP, iteration):

        a, b, c, temp = IP[1:].split('.')

        temp = temp.split('/')
        d = temp[0]
        x = temp[1]

        IP = self.get_IP_int(int(a), int(b), int(c), int(d))

        IP_bounds = self.get_IP_Bounds(IP, int(x))

        self.source_IP[iteration] = [IP_bounds[0], IP_bounds[1]]

    def handle_Dest_IP(self, IP, iteration):

        a, b, c, temp = IP.split('.')

        temp = temp.split('/')
        d = temp[0]
        x = temp[1]

        IP = self.get_IP_int(int(a), int(b), int(c), int(d))

        IP_bounds = self.get_IP_Bounds(IP, int(x))

        self.dest_IP[iteration] = [IP_bounds[0], IP_bounds[1]]

    def handle_Source_Port(self, port, iteration):

        port = port.split(':')

        self.source_Port[iteration] = [int(port[0]), int(port[1])]

    def handle_Dest_Port(self, port, iteration):

        port = port.split(':')

        self.dest_Port[iteration] = [int(port[0]), int(port[1])]

    def handle_protocol(self, protocol, iteration):

        protocol = protocol.split('/')

        self.protocol[iteration] = [self.hex_to_int(
            protocol[0]), self.hex_to_int(protocol[1])]

    def get_IP_int(self, a, b, c, d):

        return d + (256 * c) + (65536 * b) + (16777216 * a)

    def get_IP_Bounds(self, value, x):

        LowerBound = value

        LowerBound = LowerBound >> (32 - x)
        LowerBound = LowerBound << (32 - x)

        Power = int(32 - x)

        UpperBound = LowerBound + pow(2, Power) - 1

        return [LowerBound, UpperBound]

    def hex_to_int(self, value):

        return int(value, 16)
