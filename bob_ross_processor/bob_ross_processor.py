# Reads through a file and prints all bob ross episodes 
# that included a painting of a beach and a cliff

class BobRossEpisode:
    def __init__(self, episode, title, beach, cliff, tree):
        self.episode = episode
        self.title = title
        self.beach = self.__true_or_false(beach)
        self.cliff = self.__true_or_false(cliff)
        self.tree = self.__true_or_false(tree)

    def __true_or_false(self, num_str):
        if num_str == '1':
            return True
        else:
            return False

    def get_episode(self):
        return self.episode
    
    def get_title(self):
        return self.title
    
    def has_beach(self):
        return self.beach

    def has_cliff(self):
        return self.cliff

    def has_tree(self):
        return self.tree

    def print_self(self):
        print(f'{self.episode}: "{self.title.title()}"')

def parse_episode_data(line):
    episode, title, beach, cliff, tree = line.split(',')
    return BobRossEpisode(episode, title, beach, cliff, tree)

def main():
    bob_ross_data = open('bob-ross-elements.csv', 'r')
    next(bob_ross_data)
    print()

    for line in bob_ross_data:
        episode = parse_episode_data(line)

        if episode.has_beach() and episode.has_cliff():
            episode.print_self()

    bob_ross_data.close()
    print()

main()