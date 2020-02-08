class Queue:
    def __init__(self):
        self.entries = []  # 表示队列内的参数
        self.length = 0  # 表示队列的长度
        self.front = 0  # 表示队列头部位置

    def enqueue(self, item):
        self.entries.append(item)  # 添加元素到队列里面
        self.length = self.length + 1  # 队列长度增加 1

    def dequeue(self):
        self.length = self.length - 1  # 队列的长度减少 1
        temp = self.entries[self.front]  # 缓存队首元素
        self.entries = self.entries[1:]  # 队列的元素更新为退队之后的队列
        return temp

    def peek(self):
        return self.entries[0]  # 直接返回队列的队首元素

    def print_queue(self):
        print('用数组实现的队列：')
        print(self.entries)

