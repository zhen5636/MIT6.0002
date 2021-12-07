#CLASS REPRESENTATION OF OBJECTS IN MENU
#计算 食物最优 卡露里
class Food(object): #食物类   食物名 、 质量 value 、 热量 calories 
    def __init__(self, n, v , w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):  
        """ 密度"""
        return self.getValue()/self.getCost()  

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

# FUNCTION RESPONSIBLE FOR BUILDING MENU
#
# 产生一个 食物菜单  List
def buildMenu(names, values, calories):  
    """ 食物 价格 卡露里"""
    #食物名称清单 、 价格清单 、卡露里值清单
    """names, values, calories lists of same length.
    name a list of strings
    values and calories lists of numbers
    returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i])) #收集 Foods

    return menu

# IMPLEMENTATION OF FLEXIBLE GREEDY

def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
    keyFunstion maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    # sorting from best to worst by value of keyFunction

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)): 
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])         # 收集
            totalCost += itemsCopy[i].getCost()  # 累积 costs 
            totalValue += itemsCopy[i].getValue() #累积卡露里值清单

    return (result, totalValue)

# USING GREEDY

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print(' ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    # it is passing function; that's why there is no () at the end

    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    #lambda is used to make anonymous functions, with no name

    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
