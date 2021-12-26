#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Queue(object):
    # initialize list to store Queue
    def __init__(self):
        self.items = []

    # check if Queue is empty
    def isEmpty(self):
        return self.items == []

    # add element to Queue
    def enqueue(self, *args):
        for i in args:
            self.items.insert(0, i)

    # remove element from Queue
    def dequeue(self):
        if self.isEmpty():
            return 'nothing in queue to Dequeue'
        else:
            return self.items.pop()

    # check the queue first element
    def peek(self):
        if self.isEmpty():
            return 'Nothin in Queue!'
        else:
            return self.items[-1]

    # check current size of Queue
    def size(self):
        return len(self.items)

    # display all element of Queue
    def display(self):
        c = 0
        if self.isEmpty():
            print('Queue is empty')
        else:
            for i in self.items:
                c += 1
                print(c, i)
        return

    # While providing element for Queue always seperate elements using ','


# In[10]:


# Lets Play Queue
Q = Queue()


def options():
    print('''
    Choose your operation
    check : to check is Queue empty
    enqueue : to add element to Queue
    dequeue : to remove an element
    front : see the Queue top
    size : to get the Queue size
    show : to see all elements of Queue
    done : to end the operations
    ''')
    return


options()
while (1):
    print('choose any option to proceed and to see the options choose \'options\'')
    a = input().lower()
    if (a == 'check'):
        if Q.isEmpty():
            print("Queue is empty you can stat adding.")
        else:
            print('there are {} elements in Queue.'.format(Q.size()))

    elif (a == 'enqueue'):
        print("please enter your data, use comma to seperate multiple elements")
        a = input().split(',')
        for i in a:
            Q.enqueue(i)

    elif (a == 'dequeue'):
        print("dequeued :", Q.dequeue())

    elif (a == 'front'):
        print('Queue front is pointing: {}'.format(Q.peek()))

    elif (a == 'size'):
        print('your Queue size is: {}'.format(Q.size()))

    elif (a == 'show'):
        Q.display()

    elif (a == 'clear'):
        x = Q.size()
        for i in range(x):
            Q.dequeue()
        print('Queue cleared!')

    elif (a == 'options'):
        options()

    elif (a == 'done'):
        break
    else:
        print('Please choose a valid operation!')
        options()

# In[ ]:
