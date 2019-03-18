import time

def factorial(n):
    """
    Returns the factorial of a given number

    Param:
        n (int) - expects an integer >= 0

    Return:
        (int) - returns the factorial of the input: n
    """

    # if n == 0, return 1
    if n == 0:
        return 1
    # else if n > 0
    else:
        #make recursive call on n-1
        return n * factorial(n-1)
# end factorial

def factorial_memoization(n, memo):
    """
    Returns the factorial of a given number, employs memoization

    Param:
        n (int)     - expects an integer >= 0
        memo ( dict() ) - stores prev results

    Return:
        (int) - returns the factorial of the input: n

    Note:
        stores the results of previous calls to speedup calc at the cost of using more memory
    """

    # if n == 0, return 1
    if n == 0:
        return 1
    # else if n > 0
    else:
        # if result is in memo:
        if memo[n] != None:
            return memo[n]
        # else make recursive call on n-1
        else:
            #calc result
            result = n * factorial_memoization(n-1, memo)
            #store result
            memo[n] = result
            #return resul
            return result
# end factorial_memoization()

print
print '** START PROGRAM ** '
print
print 'test the performance boost of memoization w/ factorials'
print

nums = [
    20,
    3,  # 6
    5,  # 120
    7,  # 5040
    2,  # 2
    1,  # 1
    4,  # 24
    0,  # 1
    10, # 3628800
    8,  # 40320
    9,  # 362880
    6,  # 720
    12, # 479001600
    15, # 87178291200
]
print
print "-- TEST 1 --"
print 'small set of numbers (n < 15, @ x <= 30)'
print
#run factorial()
start_fact = time.time()
for x in nums:
    factorial(x)
end_fact = time.time()

# run factorial_memoization()
start_fact_mem = time.time()
#create a list to hold the results of fact_mem calls
memo = []
#set up memo to hold blanks
for i in range(max(nums)+1):
    memo.append(None)
# go thru nums
for x in nums:
    factorial_memoization(x, memo)
end_fact_mem = time.time()

print 'Runtime fact'
fact_time = end_fact - start_fact
print fact_time
factX = fact_time*100000
print '*100,000:', factX
print ""

print 'Runtime fact_mem'
mem_time = end_fact_mem - start_fact_mem
print mem_time
memX = mem_time*100000
print '*100,000:', memX
print ""

print 'raw diff'
diff_time = fact_time - mem_time
print diff_time
print '% performance boost'
print '( (slower-faster)/slower ) * 100'
diffX = factX - memX
print "%d percent faster" % ((diffX / factX) * 100)
print

print "-- Test 1 Results --"
print 'the tests above arent consistent, it isnt obvious that memoization is useful and effective for such a small data set'
print
print

print '-- Test 2 --'
print 'increase data set (100 nums in ascending order)'
print

#populate list of numbers, from 0 - 99
large = []
for i in range(100):
    large.append(i)

# w/o memoization
# run factorial()
start_fact = time.time()
for x in large:
    factorial(x)
end_fact = time.time()

# with memoization
# run factorial_memoization()
start_fact_mem = time.time()
# create a list to hold the results of fact_mem calls
memo2 = []
# set up memo to hold blanks
for i in range(len(large)+1):
    memo2.append(None)
# go thru nums
for x in large:
    factorial_memoization(x, memo2)
end_fact_mem = time.time()

print 'Runtime fact'
fact_time = end_fact - start_fact
print fact_time
factX = fact_time*100000
print '*100,000:', factX
print

print 'Runtime fact_mem'
mem_time = end_fact_mem - start_fact_mem
print mem_time
memX = mem_time*100000
print '*100,000:', memX
print

print 'raw diff'
diff_time = fact_time - mem_time
print diff_time
print '% performance boost'
print '( (slower-faster)/slower ) * 100'
diffX = factX - memX
print "%d percent faster" % ((diffX / factX) * 100)
print

print "-- Test 2 Results --"
print 'the tests above are consistent, using memoization on a larger set (ex: 100 numbers) has a definite performance boost'
print 'on avg: 93% performance boost'
print
print
