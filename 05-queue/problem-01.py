# Design a food ordering system where your python program will run two threads,
#   1. Place Order: This thread will be placing an order and inserting that 
#      into a queue. This thread places new order every 0.5 second. 
#      (hint: use time.sleep(0.5) function)
#   2. Serve Order: This thread will server the order. All you need to do is 
#      pop the order out of the queue and print it. This thread serves an 
#      order every 2 seconds. Also start this thread 1 second after place order 
#      thread is started.

from queue_using_deque import Queue
import time
import threading

def place_orders(order_queue, orders):
    for order in orders:
        order_queue.enqueue(order)
        print(order_queue)
        time.sleep(0.5)

def serve_orders(order_queue):
    while len(order_queue):
        time.sleep(1)
        print(order_queue.dequeue())

if __name__ == '__main__':
    order_queue = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    
    place_orders_thread = threading.Thread(target=place_orders, args=(order_queue, orders))
    serve_orders_thread = threading.Thread(target=serve_orders, args=(order_queue,))

    place_orders_thread.start()
    serve_orders_thread.start()

    place_orders_thread.join()
    serve_orders_thread.join()

    print(order_queue)
