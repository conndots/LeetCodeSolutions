class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.kvs = {}
        self.capacity = capacity
        self.size = 0
        self.stamp = 0
        self.lhead = None
        self.ltail = None


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        target_node = self.kvs.get(key)
        if target_node == None:
            return -1

        self.stamp += 1
        target_node[2] = self.stamp
        if target_node != self.ltail:
            if target_node == self.lhead:
                self.lhead = target_node[4]
                self.lhead[3] = None
                self.ltail[4] = target_node
                target_node[4] = None
                target_node[3] = self.ltail
                self.ltail = target_node
            else:
                prevn = target_node[3]
                nextn = target_node[4]
                prevn[4] = nextn
                nextn[3] = prevn
                self.ltail[4] = target_node
                target_node[4] = None
                target_node[3] = self.ltail
                self.ltail = target_node
        return target_node[1]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.stamp += 1
        target_node = self.kvs.get(key)
        if self.lhead == None:
            self.lhead = [key, value, self.stamp, None, None]
            self.kvs[key] = self.lhead
            self.ltail = self.lhead
            self.size += 1
        elif self.size < self.capacity or target_node != None:
            if target_node == None:
                target_node = [key, value, self.stamp, self.ltail, None]
                self.ltail[4] = target_node
                self.ltail = target_node
                self.kvs[key] = target_node
                self.size += 1
            else:
                target_node[2] = self.stamp
                if target_node != self.ltail:
                    if target_node == self.lhead:
                        self.lhead = target_node[4]
                        self.lhead[3] = None
                        self.ltail[4] = target_node
                        target_node[4] = None
                        target_node[3] = self.ltail
                        self.ltail = target_node
                    else:
                        prevn = target_node[3]
                        nextn = target_node[4]
                        prevn[4] = nextn
                        nextn[3] = prevn
                        self.ltail[4] = target_node
                        target_node[4] = None
                        target_node[3] = self.ltail
                        self.ltail = target_node
            target_node[1] = value
        else:
            self.kvs.pop(self.lhead[0])
            self.lhead = self.lhead[4]
            target_node = [key, value, self.stamp, self.ltail, None]
            self.ltail[4] = target_node
            self.ltail = target_node
            self.kvs[key] = target_node

            if self.lhead != None:
                self.lhead[3] = None
            else:
                self.lhead = target_node

c = LRUCache(2)
print(c.get(2))
c.put(2, 6)
print(c.get(1))
c.put(1,5)
c.put(1,2)
print(c.get(1))
print(c.get(2))
