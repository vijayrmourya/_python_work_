#!/usr/bin/env python
# coding: utf-8

# In[10]:


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

    # While providing element for stack always seperate elements using ','


# In[11]:


# Lets Play Stack
st = Stack()


def options():
    print('''
    Choose your operation
    check : to check is stack empty
    push : to add element to stack
    pop : to remove an element
    top : see the stack top
    size : to get the stack size
    show : to see all elements of stack
    done : to end the operations
    clear : to empty stack
    ''')
    return


options()
while (1):
    print('choose any option to proceed and to see the options choose \'options\'')
    a = input().lower()
    if (a == 'check'):
        if st.IsEmpty():
            print("Stack is empty you can stat adding.")
        else:
            print('there are {} elements in stack.'.format(st.size()))

    elif (a == 'push'):
        print("please enter your data, use comma to seperate multiple elements")
        a = input().split(',')
        for i in a:
            st.push(i)

    elif (a == 'pop'):
        print("popped :", st.pop())

    elif (a == 'top'):
        print('stack top is pointing: {}'.format(st.peek()))

    elif (a == 'size'):
        print('your stack size is: {}'.format(st.size()))

    elif (a == 'show'):
        st.display()

    elif (a == 'clear'):
        x = st.size()
        for i in range(x):
            st.pop()
        print('stack cleared!')

    elif (a == 'options'):
        options()

    elif (a == 'done'):
        break
    else:
        print('Please choose a valid operation!')
        options()

# In[ ]:
