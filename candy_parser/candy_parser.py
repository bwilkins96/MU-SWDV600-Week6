# Parses candy data from a file and prints the
# chocolate candy with the lowest sugar percentile

class Candy:
    def __init__(self, name, is_chocolate, sugar_pctile, win_pct):
        self.name = name

        if is_chocolate == '1':
            self.is_chocolate = True
        else:
            self.is_chocolate = False

        self.sugar_pctile = sugar_pctile
        self.win_pct = win_pct

    def get_name(self):
        return self.name
    
    def get_is_chocolate(self):
        return self.is_chocolate
    
    def get_sugar_pctile(self):
        return self.sugar_pctile
    
    def get_win_pct(self):
        return self.win_pct

def parse_candy_data(line):
    name, is_chocolate, sugar_pctile, win_pct = line.split('\t')
    return Candy(name, is_chocolate, sugar_pctile, win_pct)
    
def main():
    candy_data = open('candy-data.txt', 'r')
    lowest_choc = None

    for line in candy_data:
        current_candy = parse_candy_data(line)

        if current_candy.get_is_chocolate():
            if (lowest_choc == None) or (current_candy.get_sugar_pctile() < lowest_choc.get_sugar_pctile()):
                lowest_choc = current_candy

    candy_data.close()     
    print(lowest_choc.get_name(), lowest_choc.get_sugar_pctile())

main()
