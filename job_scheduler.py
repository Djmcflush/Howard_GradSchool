#DeMarcus Edwards
#Advanced Operating Systems

#Programming Assignment 1
# Task Description: Write a program that simulates the execution of a stream of interactive processes by a
# laptop with a very large memory, a quad-core processor and one hard drive (see instructions).
import time
import random
import collections

#function to run threads
def RunThread(th, parent, count):
    time.sleep(th.time_cost)
    print('PID : ' + parent + '_' + th.id + '_' + str(count) + ' Computed in : ' + str(th.time_cost) + ' seconds')
    print('PID : ' + parent + '_' + th.id + '_' + str(count) + ' Finished')
    return th.sum
#A process class
class Process(object):
    id 
    time_cost = 0
    sum
    has_children = []
    def __init__(self, id, time_cost, has_children):
        self.id = id
        self.time_cost = time_cost
        self.sum = 0
        self.has_children = has_children
    def Run_children(self):
        time.sleep(self.time_cost)
        count = 0
        for each in self.has_children:
            self.sum += RunThread(each, self.id, count)
            print('Updated Value : ' +  str(self.sum))
            count += 1 
        print('PID : ' + self.id + ' Finished')
        print('Final value ' + str(self.sum) + ' Bison')   
#randomly generates number of sub_threads and how long they take to run
def generate_Sub_process():
    num_P = random.randint(1,4)
    empty_list = []
    if(num_P >0):
        children = []
        for x in range(0, num_P):
            child = Process('child', random.randint(1,4),empty_list)
            child.sum = random.randint(0,20)
            children.append(child)
        return children
    else:
        return empty_list
def sortP(P_list):
    s = []
    p_dict = {}
    for each in P_list:
        s.append(each.time_cost)
        p_dict[each.time_cost] = each
    s.sort()
    s_ordered = collections.OrderedDict()
    for each in s:
        s_ordered[p_dict[each]] = each 
    return s_ordered

def scfs(P_list):
    shortest_first = sortP(P_list)
    for each in shortest_first:
        each.Run_children()
    print('Queue is Empty!!')
    


def main():
    P_list = []
    P_list1= generate_Sub_process()
    p1 = Process('p1',random.randint(2,6), P_list1)
    P_list2 = generate_Sub_process()
    p2 = Process('p2',random.randint(2,9), P_list2)
    P_list3 = generate_Sub_process()
    p3 = Process('p3',random.randint(2,8), P_list3)
    P_list.append(p1)
    P_list.append(p2)
    P_list.append(p3)

    scfs(P_list)

if __name__ == __name__:
    main()


    

