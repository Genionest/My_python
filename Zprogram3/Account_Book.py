#会计学基础
from prettytable import PrettyTable #制表用的

#搜索 资产，负债，所有者权益 成本的子会计科目

def search(han):
    if han == "资产":
        property_list=['库存现金', '银行存款', '其他货币资金', '交易性金融资产', '应收票据', '应收账款', '预付账款', '应收股利', '应收利息', '其他应收款', '坏账准备', '代理业务资产', '材料采购', '在途物资', '原材料', '材料成本差异', '库存商品', '发出商品', '商品进销差价', '委托加工物资', '周转材料', '存货跌价准备', '持有至到期投资', '持有至到期投资减值准备', '可供出售金融资金', '长期股权投资', '长期股权投资减值准备', '投资性房地产', '长期应收款', '未实现融资收益', '固定资产', '累计折旧', '固定资产减值准备', '在建工程', '工程物资', '固定资产清理', '无形资产', '累计摊销', '无形资产减值准备', '商誉', '长期摊销费用', '递延所得税资产', '待处理财产损溢']
        print(property_list)
    return property_list
    if han == "负债":
        liabilities_list=['短期借款', '交易性金融负债', '应付票据', '应付账款', '预收账款', '应付职工薪酬', '应交税款', '应付利息', '应付股利', '其他应付款', '代理业务负债', '递延收益', '长期借款', '应付债券', '长期应付款', '未确认融资费用', '专项应付款', '预计负债', '递延所得税负债']
        print(liabilities_list)
    return liabilities_list
    if han == '所有者权益':
        Owners_equity_list=['实收资本', '资本公积', '盈余公积', '本年利润', '利润分配', '库存股']
        print(Owners_equity_list)
    return Owners_equity_list
    if han == '成本':
        cost_list=['生产成本', '制造费用', '劳务成本', '研发支出']
        print(cost_list)
    return cost_list
    if han == '方法':
        mothed_list=['straight_line直线法','double_declinging_balance双倍余额递减法',
                     'accout_entry会计分录(other)']
        print(mothed_list)
    
#直线法
def line(big,years,small,use=0):
    #big:期初净值,years:剩余使用年数,small:净残值,use:已使用年数
        depreciation = (big-small)/years
        l = ['年份','期初净值','年折旧额','期末净值']
        table = PrettyTable(l)
        for i in range(years):
            big -= depreciation
            #利用格式化字符串保留两位小数
            col = ["%d"%(i+1+use),"%.2f"%(big+depreciation),"%.2f"%depreciation,
                   "%.2f"%big]
            table.add_row(col)
            #table.add_row([str(i+1),str(big+depreciation),str(depreciation),
            #               str(big)])
        
        print(table)
    
    
#双倍余额递减法
def double(big,years,small=0):
    #big：固定资产期初净值，years：预计使用年数，small：预计净残值
    depreciation = 2/years #双倍直线折旧率
    year = years #剩余年数
    l = ['年份','期初净值','年折旧额','期末净值']
    table = PrettyTable(l)
    
    while(year>0): #计算每年的折旧额
        d_depreciation = depreciation*big #当年的年折旧额
        l_depreciation = (big-small)/year #计算直线法当年的折旧额
        if(d_depreciation>l_depreciation):
            big -= d_depreciation
            n = years-year+1
            col = ["%d"%n,"%.2f"%(big+d_depreciation),"%.2f"%d_depreciation,
                   "%.2f"%big]
    
            table.add_row(col)
            #table.add_row([str(n),str(big+d_depreciation),str(d_depreciation),
            #              str(big)])
            year -= 1
        else:
            print(table)
            print("第"+str(years-year+1)+"年采用直线法")
            line(big,year,small,n)
        break

                
            
            
        
    
