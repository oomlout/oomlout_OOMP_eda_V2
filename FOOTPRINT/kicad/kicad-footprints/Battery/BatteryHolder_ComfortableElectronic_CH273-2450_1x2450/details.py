
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_ComfortableElectronic_CH273-2450_1x2450"
    hexID = "FZKBATBATHOLDERCOMFORTABLEELECTRONICCH2732451X245"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_ComfortableElectronic_CH273-2450_1x2450', 'description': 'Comfortable Electronic CR2450 battery holder, http://www.comf.com.tw/ProductDetail.asp?no=148', 'tags': 'Comfortable Electronic CR2450', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_ComfortableElectronic_CH273-2450_1x2450.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_ComfortableElectronic_CH273-2450_1x2450')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

