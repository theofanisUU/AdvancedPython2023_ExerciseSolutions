class Fish:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member harmless animals
        self.members = [ 'Salmon', 'Tuna']
        
    def printMembers(self):
        print('Printing members of the (harmless) Fish class')
        for member in self.members:
            print(f'\t{member} ' )
#end class