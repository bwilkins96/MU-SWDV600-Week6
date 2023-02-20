# Email class

class Email:
    def __init__(self, sender, receiver, priority, message):
        self.sender = sender
        self.receiver = receiver
        self.priority = priority
        self.message = message

        if priority > 3:
            self.priority = 3
        elif priority < 1:
            self.priority = 1

    def print_out(self):
        print(f'TO: {self.receiver}')
        print(f'FROM: {self.sender}')
        print(f'Priority: {self.priority}')
        print('---------------------')
        print(f'"{self.message}"')

def main():
    test = Email("sender@them.com","you@recipient.com", 3, "Who is Keyser Soze?")
    test.print_out()

if __name__ == '__main__': main()       
        