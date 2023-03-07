class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Monkey', 'Elephant', 'Dolphin']
    
    def printMembers(self): 
        print('Printing members of the (harmless) Mammals class')
        for member in self.members:
            print(f'\t{member} ' )
#end class            