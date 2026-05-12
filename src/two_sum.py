from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    seen = {}
    
    for i in range(len(array)):
        complement = target - array[i]
        
        if complement in seen:
            return (seen[complement],i)
        
        seen[array[i]] =i
    
    return (-1, -1)
