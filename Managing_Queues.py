#DeMarcus Edwards
#Advanced Operating Systems
#Howard University


# Write a program that implements a distributed application for managing queues.
import time
import random
import collections

# This is going to be our interface
class queue ():
    q = collections.deque()
    length = 0
    def enqueue(self,data):
        self.q.append(data)
        #collections.deque.appendright(data)
        self.length += 1
    def dequeue(self):
        self.length -= 1
        return self.q.popleft()
        #dequeues from left
        
    def peak(self):
        p = self.q.popleft
        self.q.appendleft(p)
        return p

# This is our messages that will be passed from the Producer(s) to the Queue to be recieved by the consumer with a matching Consumer_id
class message():
    producer_id = ''
    data  = ''
    consumer_id = ''
    def __init__(self, producer_id, data, consumer_id):
        self.producer_id = producer_id
        self.data = data
        self.consumer_id = consumer_id
    def reclaimer(self):
        return self.consumer_id
    
# This is our Consumer Class, They recieve tasks(messages)
class consumer():
    consumer_id = ''
    def __init__(self,consumer_id):
        self.consumer_id = consumer_id
    def run_task(self,m):
        time.sleep(1)
        print(self.consumer_id + ' Running ' + m.data + ' From ' + m.producer_id)

# This is our producer they send out tasks(messages)
class producer():
    producer_id = ''
    def __init__(self, producer_id):
        self.producer_id = producer_id
    def sendMessage(self,text, c):
        sms  = message(self.producer_id, text, c.consumer_id )
        return sms
# Quickly build all of our tasks and messages with user help :)
def build(c_list, cms, d_queue):
    text_list= []
    magic_input = int(input('Enter Amount of Processes for system to allocate : '))
    
    text_list.append('System_Defined_Process')
    text_list.append('Application_defined_process')
    salt_list = ['_Update', '_Change_Dir', '_Shallow_Copy', 'Deep_Copy']
    for x in range(0,magic_input):
        
        sms_ = cms.sendMessage( text_list[random.randint(0,1)] + salt_list[random.randint(0,len(salt_list)-1)], c_list[random.randint(0,len(c_list)-1)])
        d_queue.enqueue(sms_)
    return d_queue
# Run the Distributed messanger service that is in charge of our cluster
def run_system(Distribute_messager_queue, c_list, cms):
    consumer_dictionary = {}
    for each in c_list:
        consumer_dictionary[each.consumer_id] = each
    while(Distribute_messager_queue.length > 0):
        m = Distribute_messager_queue.dequeue()
        consumer_dictionary[m.consumer_id].run_task(m)
        #cons.run_task(m)
    print('Queue is Empty')
    print('All Process have been Completed')

class main():
    Distribute_messager_queue = queue()
    
    cluster_1 = []

    c_1 = consumer('c_1')
    c_2 = consumer('c_2')
    c_3 = consumer('c_3')
    cluster_1.append(c_1)
    cluster_1.append(c_2)
    cluster_1.append(c_3)



    cluster_mangement_system = producer('c.m.s')
    Distribute_messager_queue = build(cluster_1,cluster_mangement_system,Distribute_messager_queue)
    run_system(Distribute_messager_queue, cluster_1, cluster_mangement_system)


if __name__ == __name__:
    main()

