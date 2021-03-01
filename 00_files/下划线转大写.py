source = '''createDateTime
customer_order_no
customer_name
customer_no
receiverName
receiverPhone
provinceCode
cityCode
areaCode
townCode
provinceName
cityName
areaName
townName
orderNo'''

for i in source.split("\n"):
    sb = None
    for j in i.split("_"):
        if sb:
            sb += str.upper(j[0:1]) + j[1:]
        else:
            sb = j
    print(sb)




