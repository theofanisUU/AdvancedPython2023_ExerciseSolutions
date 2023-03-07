class Birds:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member dangerous animals
        self.members = ['Eagle']
        
    def printMembers(self):
        print('Printing members of the (dangerous) Birds class')
        for member in self.members:
            print(f'\t{member} ' )
#end class