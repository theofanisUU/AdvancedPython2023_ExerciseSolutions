class Fish:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = [ 'Shark']
        
    def printMembers(self):
        print('Printing members of the (dangerous) Fish class')
        for member in self.members:
            print(f'\t{member} ' )
#end class