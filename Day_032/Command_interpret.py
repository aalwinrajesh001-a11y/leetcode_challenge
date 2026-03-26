class Solution:
    def interpret(self, command: str) -> str:
        out=""
        i=0
        while i<(len(command)):
            if command[i]=='('and command[i+1]==')':
                out+='o'
                i+=1
            elif command[i]=='(' and command[i+1]=='a':
                out+="al"
                i+=3
            else:
                out+='G'
            i+=1
        return out
