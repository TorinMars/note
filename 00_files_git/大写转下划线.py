strs = '''
            tsv.gmt_create createDateTime,
            tsv.customer_order_no,
            tsv.customer_name,
            tsv.customer_no ,
            tsv.receiver_name receiverName,
            tsv.receiver_phone receiverPhone,
            tsv.receiver_province_code provinceCode,
            tsv.receiver_city_code cityCode,
            tsv.receiver_district_code areaCode,
            tsv.receiver_town_code townCode,
            tsv.receiver_province provinceName,
            tsv.receiver_city cityName,
            tsv.receiver_district areaName,
            tsv.receiver_town townName,
            tsv.sap_order_no orderNo,
            tsvi.so_item_no itemNo,
            tsvi.materiel materialNo,
            tsvi.sap_material_name materialName,
            tsvi.quantity materialCount,
            tsvi.quantity_unit saleUnit,
            tsvi.unit_price taxInPrice,
            tsvi.remark'''

import re
for i in strs.split("\n"):
    print(re.sub("[A-Z]", lambda x : "_" + str.lower(x.group(0)), i))