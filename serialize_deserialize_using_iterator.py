class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinaryTree:
    def treeCreate(self, nums):
        if not nums:
            return None
        def helper(left, right):
            if left<=right:
                mid = left+(right-left)//2
                root = TreeNode(nums[mid])
                root.left = helper(left, mid-1)
                root.right = helper(mid+1, right)
                return root
        return helper(0, len(nums)-1)
    
    def serialize(self, root):
        ans = []
        def encode(root):
            nonlocal ans
            if root:
                ans.append(str(root.val))
                encode(root.left)
                encode(root.right)
            else:
                ans.append("#")
                
        encode(root)
        return ans
    
    def deserialize(self, arr):
        def decode(vals):
            #Iterator object will return data, one element at a time.
            val = next(vals)
            if val == "#":
                return None
            else:
                root = TreeNode(int(val))
                root.left = self.deserialize(vals)
                root.right = self.deserialize(vals)
                return root
        #Iterators are objects that can be iterated upon.
        return decode(iter(arr))

obj = BinaryTree()
root = obj.treeCreate([1,2,3,4,7,8,9])
arr = obj.serialize(root)
root = obj.deserialize(arr)



