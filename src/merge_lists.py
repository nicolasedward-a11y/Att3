from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    if lista1 is None:
        return lista2

    if lista2 is None:
        return lista1

    if lista1.value < lista2.value:
        lista1.next = merge_lists(lista1.next, lista2)
        return lista1
    else:
        lista2.next = merge_lists(lista1, lista2.next)
        return lista2
    
        
