strs = '''id
createDate
createTime
purchaseGroupName
materialGroupName
belongProject
customerReferenceNo
blocName
customerNumber
customerName
receiverName
receiverPhone
orderNo
provinceCode
cityCode
areaCode
itmeNo
materialNo
materialName
saleUnit
materialCount
taxInPrice
sellerId
sellerName
remark
profitShare
providerName
purchaseMethod
providerId
taxInRate
purchasePrice
deductionRage
vipPurchasePrice
vipDeductionRage
vipMsg
isLowProfit
status'''

import re
for i in strs.split("\n"):
    print(re.sub("[A-Z]", lambda x : "_" + str.lower(x.group(0)), i))