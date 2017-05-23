#ActionGroup.py

class ActionGroup:
    def __init__(self, groupName = " "): # the name is optional
        self.groupName = groupName

    # reporting name
    def reportGroupName(self):
        return self.groupName

