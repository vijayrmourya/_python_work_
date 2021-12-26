#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Stack(object):
    # initialize list to store stack
    def __init__(self):
        self.items = []

    # check if stack is empty
    def IsEmpty(self):
        return self.items == []

    # add element to stack
    def push(self, *args):
        for i in args:
            self.items.append(i)

    # remove element from stack
    def pop(self):
        if self.IsEmpty():
            return 'nothing to pop stack is empty'
        else:
            return self.items.pop()

    # check the stack top element
    def peek(self):
        if self.IsEmpty():
            return 'Nothin in stack!'
        else:
            return self.items[len(self.items) - 1]

    # check current size of stack
    def size(self):
        return len(self.items)

    # display all element of stack
    def display(self):
        c = 0
        if self.IsEmpty():
            print('stack is empty')
        else:
            for i in self.items:
                c += 1
                print(c, i)
        return

    # In[10]:


s1 = Stack()
s2 = Stack()


def Check():
    if s1.IsEmpty() and s2.IsEmpty():
        return "Queue is empty you can stat adding."
    else:
        return 'there are {} elements in Queue.'.format((s1.size()) + (s2.size()))


def Enqueue(a):
    if s2.IsEmpty():
        s1.push(a)
        return
    else:
        for i in range(s2.size()):
            s1.push(s2.pop())
        s1.push(a)
        return


def Dequeue():
    if s1.IsEmpty() and s2.IsEmpty():
        return "Queue is empty nothing to dequeue"
    else:
        for i in range(s1.size()):
            s2.push(s1.pop())
        return s2.pop()


def Front():
    if s1.IsEmpty() and s2.IsEmpty():
        return "Queue is empty nothing to point"
    else:
        for i in range(s1.size()):
            s2.push(s1.pop())
        return s2.peek()


def Size():
    return s1.size() + s2.size()


def Display():
    if s1.IsEmpty() and s2.IsEmpty():
        return "Queue is empty nothing to show"
    else:
        for i in range(s1.size()):
            s2.push(s1.pop())
        s2.display()
        return


def Clear():
    for i in range(s1.size()):
        s1.pop()
    for i in range(s2.size()):
        s2.pop()
    if s1.IsEmpty() and s2.IsEmpty():
        return
    else:
        Clear()


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


# In[ ]:


# Lets Play Queue
options()
while (1):
    print('choose any option to proceed and to see the options choose \'options\'')
    a = input().lower()
    if (a == 'check'):
        print(Check())

    elif (a == 'enqueue'):
        print("please enter your data, use comma to seperate multiple elements")
        a = input().split(',')
        for i in a:
            Enqueue(i)

    elif (a == 'dequeue'):
        print("dequeued :", Dequeue())

    elif (a == 'front'):
        print('Queue front is pointing: {}'.format(Front()))

    elif (a == 'size'):
        print('your Queue size is: {}'.format(Size()))

    elif (a == 'show'):
        print(Display())

    elif (a == 'clear'):
        Clear()
        print('Queue cleared!')

    elif (a == 'options'):
        options()

    elif (a == 'done'):
        break
    else:
        print('Please choose a valid operation!')
        options()

# In[ ]:
