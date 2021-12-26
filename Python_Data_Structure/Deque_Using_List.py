#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Deque(object):
    # initialize list to store deque
    def __init__(self):
        self.items = []

    # check if deque is empty
    def isEmpty(self):
        return self.items == []

    # add element to deque front
    def addFront(self, *args):
        for i in args:
            self.items.append(i)

    # add element to deque rear
    def addRear(self, *args):
        for i in args:
            self.items.insert(0, i)

    # remove element from deque front
    def removeFront(self):
        if self.isEmpty():
            return 'nothing in Deque to remove'
        else:
            return self.items.pop()

    # remove element from deque rear
    def removeRear(self):
        if self.isEmpty():
            return 'nothing in Deque to remove'
        else:
            return self.items.pop(0)

    # check the deque front element
    def peekFront(self):
        if self.isEmpty():
            return 'Nothin in Deque!'
        else:
            return self.items[-1]

    # check the deque rear element
    def peekRear(self):
        if self.isEmpty():
            return 'Nothin in Deque!'
        else:
            return self.items[0]

    # check current size of Deque
    def size(self):
        return len(self.items)

    # display all element of Deque from front
    def displayFront(self):
        c = 0
        print("Deque elements from front")
        if self.isEmpty():
            print('Deque is empty')
        else:
            for i in self.items:
                c += 1
                print(c, i)
        return

        # display all element of Deque from rear

    def displayRear(self):
        c = 0
        print("Deque elements from rear")
        if self.isEmpty():
            print('Deque is empty')
        else:
            for i in self.items[::-1]:
                c += 1
                print(c, i)
        return

    # While providing element for Deque always seperate elements using ','


# In[16]:


# Lets Play Deque
D = Deque()


def options():
    print('''
    Choose your operation
    check : to check is Deque empty
    addfront : to add element to Deque front
    addfear : to add element to Deque rear
    removefront : to remove an element from Deque front
    removerear : to remove an element from Deque rear
    front : see the Deque front 
    rear : see the Deque rear
    size : to get the Deque size
    fshow : to see all elements of Deque from front
    rshow : to see all elements of Deque from rear
    done : to end the operations
    clear : to empty Deque
    ''')
    return


options()
while (1):
    print('choose any option to proceed and to see the options choose \'options\'')
    a = input().lower()
    if (a == 'check'):
        if D.isEmpty():
            print("Deque is empty you can stat adding.")
        else:
            print('there are {} elements in Deque.'.format(D.size()))

    elif (a == 'addfront'):
        print("please enter your data, use comma to seperate multiple elements")
        a = input().split(',')
        for i in a:
            D.addFront(i)

    elif (a == 'addrear'):
        print("please enter your data, use comma to seperate multiple elements")
        a = input().split(',')
        for i in a:
            D.addRear(i)

    elif (a == 'removefront'):
        print("removed from front :", D.removeFront())

    elif (a == 'removerear'):
        print("removed from Rear :", D.removeRear())

    elif (a == 'front'):
        print('Deque front is pointing: {}'.format(D.peekFront()))

    elif (a == 'rear'):
        print('Deque rear is pointing: {}'.format(D.peekRear()))

    elif (a == 'size'):
        print('your Deque size is: {}'.format(D.size()))

    elif (a == 'fshow'):
        D.displayFront()

    elif (a == 'rshow'):
        D.displayRear()

    elif (a == 'clear'):
        x = D.size()
        for i in range(x):
            D.removeFront()
        print('Deque cleared!')

    elif (a == 'options'):
        options()

    elif (a == 'done'):
        break
    else:
        print('Please choose a valid operation!')
        options()

# In[ ]:
