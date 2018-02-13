def binary_array_to_number(arr):
  arraystr = ''.join(str(i) for i in arr)
  return int(arraystr, 2)
