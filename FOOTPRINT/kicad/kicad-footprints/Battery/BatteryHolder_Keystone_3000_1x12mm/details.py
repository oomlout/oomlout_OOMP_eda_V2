
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Keystone_3000_1x12mm"
    hexID = "FZKBATBATHOLDERKEYSTONE31X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Keystone_3000_1x12mm', 'description': 'http://www.keyelco.com/product-pdf.cfm?p=777', 'tags': 'Keystone type 3000 coin cell retainer', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_3000_1x12mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_Keystone_3000_1x12mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

