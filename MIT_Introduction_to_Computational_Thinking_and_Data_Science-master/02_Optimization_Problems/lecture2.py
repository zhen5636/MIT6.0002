
#计算 食物最优 卡露里
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'
# 产生一个 食物菜单  List
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

# bettes  最好 什么最好 背包问题
#贪婪 算法
# 效率 如何 nlog n n=len() 10K*log 10k
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of Items to numbers"""
         # KEY Function 映射到 数字 为每个元素 
          # 找出最优 Bettes
          #找 最优与最差 与 元素有关排序，
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True) #排序 条件 ，最优
    result = []
    totalValue, totalCost = 0.0, 0.0
    # 计算 累积

    for i in range(len(itemsCopy)):  # 遍历 序列
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])         # 收集
            totalCost += itemsCopy[i].getCost()  #+= 累积卡露里值清单
            totalValue += itemsCopy[i].getValue() # 累积 costs 
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')

    testGreedy(foods, maxUnits, Food.getValue) #确定优先 排序条件 Food.GtValue
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)

# 原理：二叉树 分枝   Take and  dnot take 
# 目的：从items序列中，找出最优组合 ，最大价值（背包问题，空间装载，最大价值）
# 二叉枝算法： 降低时间复杂度 优化代码 
 # 返回： 最大价值序列， 价值
  #参数： toconsider 是Item序列  avail累加value
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem（背包问题） and the items of that solution"""
    """ avail 重量上限 """   

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        # 递归  向右分枝
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        # 左分枝 不包含 上一个结点
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
         # 右分枝 包含 上一个结点
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
       
        #Choose better branch
        # 选择 最优分枝
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


# 测试 背包 优化算法
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print('')
testMaxVal(foods, 750)

import random
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

#for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
#    print('Try a menu with', numItems, 'items')
#    items = buildLargeMenu(numItems, 90, 250)
#    testMaxVal(items, 750, False)  

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#for i in range(121):
#    print('fib(' + str(i) + ') =', fib(i))


def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

#for i in range(121):
#    print('fib(' + str(i) + ') =', fastFib(i))

def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
        #Check if similar problem was already solved. If it was take the solution.
    elif toConsider == [] or avail == 0:
        result = (0, ())
        #If list of elements to consider is empty or we don't have any more space we can not add any more elements.
    elif toConsider[0].getCost() > avail:
        #If the cost of element is to big we wxplore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)
          
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
   items = buildLargeMenu(numItems, 90, 250)
   testMaxVal(items, 750, fastMaxVal, True)
