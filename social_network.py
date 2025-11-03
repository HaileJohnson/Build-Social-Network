class Person:
    def __init__(self, name:str):
        self.name = name
        self.friends = []\
        
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def __repr__(self):
        friend_names = [f.name for f in self.friends]
        return f"{self.name}: {', '.join(friend_names) if friend_names else 'No Friends'}"
    


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name:str):
        if name not in self.people:
            self.people[name] = Person(name)
        else: 
            print(f"Error: {name} already exists in Network")

    def add_friendships(self, name1: str, name2: str):
        if name1 not in self.people:
            print (f"Error: {name1} does not exist in Network")
            return
        
        if name2 not in self.people:
            print (f"Error: {name2} does not exist in Network")
            return
        
        person1 = self.people[name1]
        person2 = self.people[name2]

        person1.add_friend(person2)
        person2.add_friend(person1)
    

    def print_network(self):
        for person in self.people.values():
            print(person)


# Test your code here
network = SocialNetwork()
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")

network.add_friendships("Alex", "Jordan")
network.add_friendships("Alex", "Morgan")
network.add_friendships("Jordan", "Taylor")  # Error

network.print_network()

# Why is a graph the right structure to represent a social network?
# A graph is ideal becuase it can represent each person as a node and each friendship
# as an edge, allowing multiple, bidirectional connections. This mirrors how real social
# networks work, where one person can have many friends and relationships go both ways.

# Why wouldn’t a list or tree work as well for this?
# Lists are linear, so they can only store simple sequences and do not efficiently represent
# multiple relationships. Trees are hierarchical, which makes it difficult to model the many 
# non-hierarchical connections in social networks.

# What performance or structural trade-offs did you notice when adding friends or printing the network?
# Adding friends requires checjing for duplicates in each person's friends list, which can become slower
# as the network grows. Printing the network is straightforward but take time proportional to the number of
# people and friendships. erall, the graph sturcture is flexible but requires careful management to maintain data integrity.
