def numOfSubarrays(arr, k, threshold):
    # Calcula el umbral de suma requerida para la comparacion
    threshold_sum = k * threshold
    current_sum = sum(arr[:k])
    count = 0
    
    # Revisa la primera ventana
    if current_sum >= threshold_sum:
        count += 1
    
    # Arrastra la ventana atravez del arreglo
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        if current_sum >= threshold_sum:
            count += 1
    
    return count

# Ejemplo 1
arr1 = [2, 2, 2, 2, 5, 5, 5, 8]
k1, threshold1 = 3, 4
result1 = numOfSubarrays(arr1, k1, threshold1)
print(f"Example 1 Result: {result1}")

# Ejemplo 2
arr2 = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k2, threshold2 = 3, 5
result2 = numOfSubarrays(arr2, k2, threshold2)
print(f"Example 2 Result: {result2}")
