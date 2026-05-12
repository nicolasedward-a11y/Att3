from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    if head is None:
        return None

    seen = set()

    current = head
    prev = None

    while current:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current

        current = current.next

    return head
