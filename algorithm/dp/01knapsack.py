# item[]
    # price[]
    # weight[]
# weight capacity
# dp[][]

# recurrence relation
# not include
    # dp[i-1][w]
# include
    # dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + p[i])
                # not included = previous maximum price
                # included = previous maximum price of possible capacity + current price

w_limit = 8
item_num = 4
p = [0, 1, 2, 5, 6]
w = [0, 2, 3, 4, 5]
dp = [[0] * (w_limit + 1) for _ in range(item_num + 1)]


def _01knapsack():
    for i in range(1, item_num+1):
        for j in range(1, w_limit+1):
            if j - w[i] < 0: # not possible capacity -> not included
                dp[i][j] = dp[i-1][j]
            else: # possible capacity -> compare between not included vs. included
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + p[i])

def get_selected_item():
    result = [0 for _ in range(item_num)]
    target = dp[item_num][w_limit]
    j = w_limit
    for i in range(item_num, 0, -1):
        if dp[i-1][j] != target: # if previous row has different value from target, that means the item is optimal
            result[i-1] = 1
            target -= p[i] # subtract price
            j -= w[i] # subtract weight
    return result

_01knapsack()
for i in dp:
    print(i)
print(get_selected_item())