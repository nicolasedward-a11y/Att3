from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev
    
