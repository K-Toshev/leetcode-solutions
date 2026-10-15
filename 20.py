class Solution(object):
    def isValid(self, s):
        # ----------------------------------------- PROBLEM STATEMENT -----------------------------------------
        '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
            1) Open brackets must be closed by the same type of brackets.
            2) Open brackets must be closed in the correct order.
            3) Every close bracket has a corresponding open bracket of the same type.
        '''
        # -----------------------------------------------------------------------------------------------------


        # The approach here is as follows:
        #   We iterate through the parentheses, pushing open ones to a stack.
        #   If we find a closed one, we check whether or not it is in a valid position, and if it is, we pop the top of the stack off.
        #   If, when the iteration is done, the stack is empty, we know the string is valid.
        #   
        #   Time complexity: O(n)
        #   Space complexity: O(n)

        # This is a helper function that determines whether the character p1 "closes" p2.
        # In this context:
        #   ')' closes '('
        #   '}' closes '{'
        #   ']' closes '['
        # This is a constant time function.
        def closes(p1, p2):
            if p1 == ')' and p2 == '(': return True
            if p1 == '}' and p2 == '{': return True
            if p1 == ']' and p2 == '[': return True
            return False

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if closes(s[i], stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

        
        