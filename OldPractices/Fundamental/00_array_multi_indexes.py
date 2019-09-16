"""Bài tập: Cho trước một số tự nhiên n. 
Tạo một mảng có n phần tử mà các phần tử có chỉ số chẵn (bắt đầu từ 0)
là một cấp số cộng bắt đầu từ 2, công sai bằng -0.5; 
các phần tử có chỉ số lẻ bằng -1.
Ví dụ:
Với n=4, kết quả trả về là mảng [ 2. -1. 1.5 -1. ]. 
Với n=5, kết quả trả về là mảng [ 2. -1. 1.5 -1. 1. ]."""

import numpy as np

def myfunc(n):
    '''
  type: n - a positive integer 
  rtype: a numpy array
  '''
    ## TODO
    a = np.arange(2, -(n - 2 *4) * .25, -.25)

    #return array with odd index elements
    a[1::2] = -1
    return a
    ## --- end TODO ---

print(myfunc(12))