
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Bulgin_BX0036_1xC"
    hexID = "FZKBATBATHOLDERBULGINBX361XC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Bulgin_BX0036_1xC', 'description': 'Bulgin Battery Holder, BX0036, Battery Type C (https://www.bulgin.com/products/pub/media/bulgin/data/Battery_holders.pdf)', 'tags': 'Bulgin BX0036', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Bulgin_BX0036_1xC.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Battery : BatteryHolder_Bulgin_BX0036_1xC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

