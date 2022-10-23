
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Keystone_2466_1xAAA"
    hexID = "FZKBATBATHOLDERKEYSTONE24661XAAA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Keystone_2466_1xAAA', 'description': '1xAAA Battery Holder, Keystone, Plastic Case, http://www.keyelco.com/product-pdf.cfm?p=1031', 'tags': 'AAA battery holder Keystone', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_2466_1xAAA.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_Keystone_2466_1xAAA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

