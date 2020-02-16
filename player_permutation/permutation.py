class Permutation(object):
    def __init__(self):
        self.n = 11

        self.preference = []
        for i in range(self.n + 1):
            self.preference.append([0] * self.n)
        self.output_file = open("outputPS7.txt", "a")
        pass

    def read_file(self, inputfile):
        """
        Reads inputfile and parses the data to form preference array
        :param inputfile:
        :return: None
        """
        row_num = 0
        with open(inputfile) as fp:
            for line in fp.readlines():
                data = line.strip().split("/")
                for i in range(len(data)):
                    data[i] = data[i].strip()
                column_list = data[1:]
                # Set bit to 1 for preferred position denoted by columns
                for col in column_list:
                    self.preference[row_num][int(col) - 1] = 1
                row_num += 1

    def assign(self):
        """
        calculate the total number of unique batting charts such that every player gets
        exactly one batting position from their list of positions and no two players are
        given the same batting position in one batting chart.
        :return: None
        """
        mx = 1 << self.n

        """
            Set dp array for implementing dynamic programming
                player = number of bits set in integer i 
                dp[i] = the number of ways of assigning batting position to player Pn 
      
                If jth bit of integer i is set, it means that the position j is  already 
                assigned to player 1 .. p-1 
                and it cannot be assigned to player p.
        """
        dp = [0] * mx
        dp[mx - 1] = 1

        # Proceeding in bottom up manner
        mask = mx - 1
        while mask >= 0:

            # Now, to find the player
            j = mask
            p = 0

            # Count number of bits set to 1 in mask
            try:
                while j:
                    p += (j & 1)
                    j = int(j / 2)
            except Exception as e:
                print("Error in counting set bits: ", e, file=self.output_file)
                raise e

            # So, calculate the state for player p
            for i in range(self.n):
                try:
                    if self.preference[p][i] and not (mask & (1 << i)):
                        dp[mask] += dp[mask | (1 << i)]
                except Exception as e:
                    print("Error while calculating state of player P{}: {}".format(p, e),
                          file=self.output_file)
                    raise e
            mask -= 1

        # Write the result to output file
        print("The total number of allocations possible is: {}".format(dp[0]),
              file=self.output_file)
        self.output_file.close()
