# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def exchange(self, k_list, previous_node, head, k):
       # 헤드 노드일 경우 리스트를 역순으로 교환
        if previous_node == None:
            k_list[0].next = k_list[k - 1].next
            head = k_list[k - 1]
            temp_node = head
            # 여기서 문제가 됨. k가 적으면 실행이 안됨. ex) 2
            for i in range(len(k_list) - 2, -1, -1):
                temp_node.next = k_list[i]
                temp_node = temp_node.next
        else:
            k_list[0].next = k_list[k - 1].next
            previous_node.next = k_list[k - 1]
            temp_node = previous_node.next
            for i in range(len(k_list) - 2, -1, -1):
                temp_node.next = k_list[i]
                temp_node = temp_node.next
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k개의 리스트 노드를 가리키도록하는 리스트를 만들고
        # 연결리스트를 따라가다 k개가 되면 순서를 바꾸면 된다.

        k_list = [None] * k

        k_index = 0
        previous_node = None
        current_node = head
        k_list[0] = head
        while current_node.next != None:
            if k_list[k - 1] != None:
                self.exchange(k_list, previous_node, head, k)

                # 교환이 끝나면 초기화
                previous_node = k_list[0]   # 처음이 가장 마지막으로
                current_node = k_list[0]
                k_index = 0
                k_list = [None] * k

            # k_list가 다찰때까지 반복
            current_node = current_node.next
            k_index += 1
            k_list[k_index] = current_node

        # 마지막 재계산 시도
        if k_list[k - 1] != None:
            self.exchange(k_list, previous_node, head)

if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    k = 2

    # 리스트 -> 연결 리스트 변환
    dummy = ListNode(0)
    current = dummy

    for value in head:
        current.next = ListNode(value)
        current = current.next

    head_node = dummy.next

    def print_list(node):
        while node is not None:
            print(node.val, end="")

            if node.next is not None:
                print(" -> ", end="")

            node = node.next

        print()

    print("변경 전:")
    print_list(head_node)

    solution = Solution()
    result = solution.reverseKGroup(head_node, k)

    print("변경 후:")
    print_list(result)