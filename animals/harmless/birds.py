class Birds:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member harmless animals
        self.members = ['Sparrow', 'Robin', 'Duck']
        
    def printMembers(self):
        print('Printing members of the (harmless) Birds class')
        for member in self.members:
            print(f'\t{member} ' )
#end class