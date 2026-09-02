class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LRUCache:
    # capacity 이하의 키 개수를 가지는 딕셔너리를 사용한다.
    # get과 put이 O(1)이어야 하므로 해시를 사용하는 딕셔너리가 적합하다. 또한 key, value쌍이므로 사용할 수 있다.
    # 키가 언제 사용되었는지를 저장하는 linked list가 필요하다
    # put도 사용되었다고 생각하면 저장할 수 있다.
    # 그러면 동일하게 설정된 우선순위는 없다.
    
    def __init__(self, capacity: int):
        self.head = None
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if self.head == None:
            return -1 
        
        # head가 찾는 키인경우 바꿀필요 없음
        if self.head.key == key:
            return self.head.value

        target_node = self.head
        previous_node = None
        is_find_key = False

        # 키 찾기 (head 다음부터 마지막 전까지)
        while target_node.next != None:
            if target_node.key == key:
                is_find_key = True
                break
            previous_node = target_node
            target_node = target_node.next

        # 마지막 노드 검사
        if target_node.key == key:
            is_find_key = True

        # 키를 찾은 경우
        # 이전 노드를 현재 노드의 next에 연결하고
        # 현재 노드는 head로 이동
        # 현재 노드의 다음 노드를 이전에 head에 연결되어있던 노드로
        if is_find_key:
            previous_node.next = target_node.next
            target_node.next = self.head
            self.head = target_node
            
            return target_node.value
        # 찾지 못한 경우
        else:
            return -1 
        
    def put(self, key: int, value: int) -> None:
        # 노드가 없는 경우
        new_node = Node(key, value)
        if self.head == None:
            self.head = new_node
            return

        # 키가 존재하는 경우
        if self.head.key == key:
            self.head.value = value
            return

        target_node = self.head
        is_find_key = False
        previous_node = None
        # 키 찾기 (head 다음부터 마지막 전까지)
        while target_node.next != None:
            if target_node.key == key:
                is_find_key = True
                break
            previous_node = target_node
            target_node = target_node.next

        # 마지막 노드 검사
        if target_node.key == key:
            is_find_key = True

        if is_find_key:
            previous_node.next = target_node.next
            target_node.next = self.head
            self.head = target_node
            target_node.value = value
            return
        else:
            # 키가존재하지 않는 경우


            # 전체 용량을 계산해 삽입및 삭제
            count = 1

            # 위치 삽입이 잘못됨. 끝이 아니라 처음에 넣어야 한다.
            # next가 None일때까지 가서 추가
            current_node = self.head
            previous_node = None
            while current_node.next != None:
                count += 1
                previous_node = current_node
                current_node = current_node.next

            
            # capaciy = 1, head
            if previous_node == None and self.capacity == 1:
                self.head = new_node
                return

            # capacity가 가득 참

            # 마지막 노드의 연결을 끊고 가장 처음에 삽입
            if count >= self.capacity and previous_node != None:
                previous_node.next = None
                new_node.next = self.head
                self.head = new_node
                return

            # capcity에 여유가 있는 경우
            # current_node.next = Node(key, value)
            new_node.next = self.head
            self.head = new_node
            return


        


if __name__ == "__main__":
    a = LRUCache(2)

    list1 =[[2,1],[1,1],[2,3],[4,1],[1],[2]]
    # s = "ABCCED"
    for op in list1:
        if len(op) > 1:
            a.put(op[0], op[1])
        else:
            a.get(op[0])

        c = a.head
        #print("[", c.key, ",", c.value, "]")
        while c and c.next != None:
            print("[", c.key, ",", c.value, "]")
            c = c.next
        if c:
            print("[", c.key, ",", c.value, "]")
        print("----")
    #print(a.calculate(list1))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)