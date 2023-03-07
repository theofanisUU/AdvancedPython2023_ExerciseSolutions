class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Wolf']
    
    def printMembers(self): 
        print('Printing members of the (dangerous) Mammals class')
        for member in self.members:
            print(f'\t{member} ' )
#end class            