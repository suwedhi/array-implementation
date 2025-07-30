MAX_SIZE=5
stack=[]
top=-1
def push(book_title):
    global top
    if top>=MAX_SIZE-1:
        print("Stack overflow! Cannot push more books:")
    else:
        top+=1
        stack.append(book_title)
        print(f"Book{book_title}pushed into the stack")
def pop():
    global top
    if top==-1:
        print("Srack underflow! cannot pop any book")
    else:
        remove_book=stack.pop()
        print(f"Book popped from {remove_book} the stack")
        top-=1
def peek():
    if top==-1:
        print("Stack in empty.No bok to peek")
    else:
        print(f"Top book on the stack:{stack[top]}")
def display():
    if top==-1:
        print("stack is empty")
    else:
        print("Books in stack(top to bottom):")
        for i in range(top,-1,-1):
            print(f"{i+1}.{stack[i]}")
push("Harry potter")
push("ponniyin selvan")
push("1984")
push("To kill a morckingtuid")
push("The hobberlet")
display()
peek()
pop()
pop()
display()
peek()
    
