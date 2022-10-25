
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_MPD_BC2003_1x2032"
    hexID = "FZKBATBATHOLDERMPDBC231X232"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_MPD_BC2003_1x2032', 'description': 'http://www.memoryprotectiondevices.com/datasheets/BC-2003-datasheet.pdf', 'tags': 'BC2003 CR2032 2032 Battery Holder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_MPD_BC2003_1x2032.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_MPD_BC2003_1x2032')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

