from data_structure.queue import Node
from data_structure.queue import Queue
from data_structure.queue_arr import Queue as QueueArr

queue = Queue()
queue_arr = QueueArr()

queue.enqueue(21)
queue.enqueue(35)
queue.enqueue(58)
queue.enqueue(13)
queue.print_queue()

queue_arr.enqueue(21)
queue_arr.enqueue(35)
queue_arr.enqueue(58)
queue_arr.enqueue(13)
queue_arr.print_queue()

print('分别输出头部元素')
print(queue.peek())
print(queue_arr.peek())
print('分别删除头部元素')
print(queue.dequeue())
print(queue_arr.dequeue())
print('再次分别输出头部元素')
print(queue.peek())
print(queue_arr.peek())
print('分别打印列表')
queue.print_queue()
queue_arr.print_queue()

