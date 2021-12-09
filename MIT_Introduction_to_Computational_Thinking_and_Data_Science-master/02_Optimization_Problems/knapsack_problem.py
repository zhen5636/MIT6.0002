# 原理：二叉树 分枝   Take and  dnot take 
# 目的：从items序列中，找出最优组合,最大价值（0/1背包问题，人的有限负重，最大价值）
#  算法：二叉枝 Take/dont take , 降低时间复杂度 优化代码 
    # 返回：最大价值序列， 价值
    #参数： toconsider 是Item序列  avail累加value
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem（背包问题） and the items of that solution"""
    """ avail 期望值 """   

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only 
        # 递归   向右分枝：for consider[0] 太大不能选入
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        # 左分枝  take  "NextItem"
          # avail 值 减去
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())

        withVal += nextItem.getValue()
        #Explore right branch
         # 右分枝  Dont take  "NextItem"
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


# 测试 背包 优化算法


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)


testMaxVal(foods, 750)