from ArrayStack import ArrayStack

def checkBrackets(str):
    s=ArrayStack()
    for ch in str:
        if ch in {'[','(','{'}:
            s.push(ch)
        elif ch in {']','}',')'}:
            if s.isEmpty():
                return False
            else: 
                open=s.pop()
                if(ch==']'and open !='[') or (ch=='}'and open !='{') or (ch==')'and open !='('):
                    return False
                    
    return s.isEmpty()  #error1

print(checkBrackets(""))