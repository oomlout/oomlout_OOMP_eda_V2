
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_MPD_BA9VPC_1xPP3"
    hexID = "FZKBATBATHOLDERMPDBA9VPC1XPP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_MPD_BA9VPC_1xPP3', 'description': '1xPP3 (9V) battery holder, Memory Protection Devices P/N BA9VPC, http://www.memoryprotectiondevices.com/datasheets/BA9VPC-datasheet.pdf', 'tags': 'PP3 Battery Holder BA9VPC 9V', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_MPD_BA9VPC_1xPP3.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Battery : BatteryHolder_MPD_BA9VPC_1xPP3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

