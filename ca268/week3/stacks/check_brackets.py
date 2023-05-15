# A common application of stacks is to check for matching brackets.
# Write a function which takes a string parameter and returns a boolean value which indicates whether the brackets in the string match.

class Stack:
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

def check_brackets(word):
    s = Stack()
    for i in word:
        if i in "([{":
            s.push(i)
            print(f"pushed {i}")
        elif i in ")]}":
            if s.is_empty() == True:
                return False
            else:
                close = s.pop()
                if (i == ")" and close != "(") or (i == "}" and close != "{") or (i == "]" and close != "["):
                    return False
                print(f"popped {i}")
    return s.is_empty()

print(check_brackets("d({hello))"))