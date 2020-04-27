class TreeNode(object):
    def __int__(self,data):
        self.val = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""

# 创建树节点队列函数
def creatnodeQ(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q

# 给队列添加节点元素, 保证优先度
def addQ(queue, nodeNow):
    if len(queue) == 0:
        return [nodeNow]

    for i in range(len(queue)):
        if queue[i].priority >= nodeNow.priority:
            return queue[:i] + [nodeNow] + queue[i:]

    return queue + [nodeNow]

# 定义一个节点队列
class nodeQueue(object):
    def __init__(self,code):
        self.que = creatnodeQ(code)
        self.size = len(self.que)

    def addNode(self,node):
        self.que = addQ(self.que,node)
        self.size +=1

    def popNode(self):
        self.size -=1
        return self.que.pop(0)

# 统计字符在字符串中出现的次数, 计算出权重值, 即优先度
def freChar(string):
    d = {}
    for c in string:
        if c not in d:
            d[c] =1
        else:
            d[c] +=1
    return sorted(d.items(), key=  lambda  x :x[1])

def creatHuffmanTree(nodeQ):
    while nodeQ.size !=1:
        # 弹出辅助队列中, 权重最小的2个node
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()

        r = TreeNode([None, node1.priority+node2.priority])
        r.leftChild = node1
        r.rightChild = node2

        nodeQ.addNode(r)
    return nodeQ.popNode()


codeDic1 = {}
codeDic2 = {}

# 由哈夫曼树得到编码
def HuffmanCodeDic(head, x):
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftchild, x+'0')
        head.code +=x
        if head.val :


