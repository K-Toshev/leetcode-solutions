class MinStack(object):
    
    # How long did this take me to solve? : 16 minutes and 12 seconds :)
    
    # We will construct MinStack via two separate stacks:
    # - items: This will store the actual items on the stack
    # - min_indices: This will store the indices of specific elements of items. An index will be in min_indices only if
    #                its corresponding element in items is less than or equal to all of the elements below it.
    # We can achieve O(1) time complexity for getMin() because of min_indices, since checking the top
    # of a stack is a constant_time operation. To maintain this property of min_indices, we need to update
    # it any time we perform an operation which modifies the stack size, be it push or pop.
    def __init__(self):
        self.items = []
        self.min_indices = []
    
    # This function pushes value to the top of the item stack in all cases.
    # Once complete, it checks whether the current item is smaller than that
    # pointed to by the index at the top of min_indices, pushing its index if true.
    # Time complexity: O(1) amortized, since we add to the end of a list, and we do constant-time integer comparisons.
    # Space complexity: O(1), since we are only storing individual values here.
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.items.append(value)
        if len(self.min_indices) == 0:
            self.min_indices.append(len(self.items) - 1)
        else:
            if value <= self.items[self.min_indices[-1]]:
                self.min_indices.append(len(self.items) - 1)

    # This method first checks whether or not the element at the top of the 
    # is the one at the top of min_indices, popping from min_indices if it is.
    # Regardless of the result of that, we pop the item stack afterwards
    # Time complexity: O(1) because we only do integer comparisons and remove
    #                  from the end of a List, which never triggers a resize
    # Space complexity: O(1), because we are not storing any additional things here
    def pop(self):
        """
        :rtype: None
        """
        if len(self.items) - 1 == self.min_indices[-1]:
            self.min_indices.pop()
        self.items.pop()
        
    # This function simply returns the item at the top of the item stack
    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items) - 1]

    # This function returns the minimum item on the stack by returning the item specified by the index
    # at the top of min_indices.
    # Time complexity: O(1) because we are simply indexing into an array
    # Space complexity: O(1) because we are not storing anything additional here
    def getMin(self):
        """
        :rtype: int
        """
        return self.items[self.min_indices[-1]]