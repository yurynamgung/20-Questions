#yury namgung
# cs black

tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))

"""takes input tree and returns new tree for 21 Q game"""
def play(tree):
    if leaf(tree):
        return playLeaf(tree)
    else: 
        root, yesChild, noChild = tree
        answer = input(root + ' ')
        if yes(answer):
            return (root, play(yesChild), noChild)
        else: return (root, yesChild, play(noChild))

"""returns whether or not the tree is a leaf"""
def leaf(tree):
    root, left, right = tree
    if left == None and right == None:
        return True
    else: return False

"""returns whether or not the answer is yes"""
def yes(answer):
    if answer == "Yes" or answer == 'yes': return True
    else: return False

"""checks if the program got the answer. If not, adds new tree
that's learned the right answer"""
def playLeaf(tree):
    root, right, left = tree #root is the leaf (the object)
    answer = input('Is it ' + root + '? ')
    if answer == 'yes' or answer == 'Yes': 
        print('I got it!')
        return tree
    else: 
        newLeaf = input("Drats! What was it? ")
        newQ = input("What's a question that distinguishes between " 
            + newLeaf + " and " + root + "? ")
        newAnswer = input("And what's the answer for " + newLeaf + "? ")
        if yes(newAnswer):
            return (newQ, (newLeaf, None, None), tree)
        else:
            return (newQ, tree, (newLeaf, None, None))

"""save tree into a file"""
def saveTree(tree, fileName):
    root, right, left = tree
    if leaf(tree):
        fileName.write(root + "\n"+"Leaf" + "\n")
    else:
        fileName.write(root + "\n"+ "Internal node" + "\n")
        saveTree(right, fileName)
        saveTree(left, fileName)
    return

"""builds tree of tuples from list format (from file)"""
def buildTreeHelper(treeList):
    if treeList == []:
        return ()
    elif treeList[1] == "Leaf":
        return (treeList[0], None, None)
    else: 
        if treeList[3] == "Internal node":
            return (treeList[0], buildTreeHelper(treeList[2:-2]), buildTreeHelper(treeList[-2:]))
        else: 
            return (treeList[0], buildTreeHelper(treeList[2:4]), buildTreeHelper(treeList[4:]))

"""takes in file and returns tree saved in file"""
def buildTree(fileName):
    fileHandle = open(fileName, 'r')
    list1 = fileHandle.readlines()
    fileHandle.close()
    cleanList1 = list(map(lambda x: x.strip("\n"), list1)) # strip off the \n symbols
    tree1 = buildTreeHelper(cleanList1)
    return tree1

def main():
    print("Welcome to 20 Questions!")
    loadFileQ = input("Would you like to load a tree from a file? ")
    if yes(loadFileQ):
        fileName = input("What's the name of the file? ")
        f1 = open(fileName, "r") #open file to write newTree into it
        tree = buildTree(fileName)
        f1.close()
    else:
        tree = input("Please enter a starter tree: ")
    while True:
        newTree = play(tree)
        tree = newTree
        playAgainQ = input("Would you like to play again? ")
        if yes(playAgainQ):
            continue
        else:
            break
    saveQ = input("Would you like to save this tree for later? ")
    if yes(saveQ):
        newFileName = input("Please enter a file name: ")
        nf = open(newFileName, "w")
        saveTree(tree, nf)
        nf.close()
        print("Thank you! The file has been saved.")
    print("Bye!")
    return