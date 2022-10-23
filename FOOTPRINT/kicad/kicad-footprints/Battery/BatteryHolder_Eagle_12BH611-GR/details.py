
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Eagle_12BH611-GR"
    hexID = "FZKBATBATHOLDEREAGLE12BH611GR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Eagle_12BH611-GR', 'description': 'https://eu.mouser.com/datasheet/2/209/EPD-200766-1274481.pdf', 'tags': '9V Battery Holder', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Eagle_12BH611-GR.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Battery : BatteryHolder_Eagle_12BH611-GR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

