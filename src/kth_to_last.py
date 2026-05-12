from src.my_node import MyNode

def kth_to_last(head: MyNode, k: int) -> int:
    if head is None or k <= 0:  # k=0 inválido
        return -1

    slow = head
    fast = head

    for _ in range(k - 1):  # ← k-1 em vez de k
        fast = fast.next
        if fast is None:
            return -1

    while fast.next:  # ← fast.next em vez de fast
        slow = slow.next
        fast = fast.next

    return slow.value  
