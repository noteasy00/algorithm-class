# define Stack class with push, pop, peek is_empty, and size methods
#stack ADT
class Arraystack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1


    def is_empty(self):
        return self.top == -1
    
    #full
    def is_full(self):
        return self.top == self.capacity -1

#psuh 매개변수 item
    def push(self, item): 
        if not self. is_full():
            self.top += 1
            #         = self.top + 1
            self.array[self.top] = item
            print(f"PUSH: {item!r}) -> stack is now {self.array[:self.top +1]}")
            #print(f"Pushed {item} to stack.")
        else:
            raise OverflowError("Stack Overflow") # pass 쓰는 것 보단 raise가 더 나음
        

    #삭제 (교재랑 다르게 pass 대신에 raise 씀)
    def pop(self): 
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print(f"POP : {item!r}) -> stack is now {self.array[:self.top +1]}")
            return item
        else:
            raise IndexError("Stack underflow")
        
    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    
    def size(self):
        return self.top + 1
    
#Test The Stack class

def reverse_string(statement):
    print("\n[1] PUSH 단계 ----------------------------")
    st  = Arraystack(len(statement)) #len이 뭐지/ st == stack
    for char in statement :
        st.push(char)

    print("\n[2] POP 단계 ----------------------------")
    out = [] #list
    while not st. is_empty():
        out.append(st.pop())
    
    result = ''.join(out)
    print(f"\n[3] 최종결과 : {result}")
    return result

if __name__ == "__main__":
    statement = "안녕하세요, 반갑습니다!"
    reverse_string(statement)

