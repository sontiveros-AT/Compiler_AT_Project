class Birds:
    def __init__(self):
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']

    def print_members(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)

