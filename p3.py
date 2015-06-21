class Library(object):

    def __init__(self):
        self.books = [ 1, 2, 3, 4 ] 

    def __getitem__(self, i):
        return self.books[i]

    def __repr__(self) :
        return '[%.5f, %.5f]'  % (self.books[2], self.books[3])

druuu = Library()

print druuu
x = druuu[1]*10
print x
