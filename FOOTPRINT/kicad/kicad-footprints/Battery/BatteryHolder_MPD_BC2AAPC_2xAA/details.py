
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_MPD_BC2AAPC_2xAA"
    hexID = "FZKBATBATHOLDERMPDBC2AAPC2XAA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_MPD_BC2AAPC_2xAA', 'description': '2xAA cell battery holder, Memory Protection Devices P/N BC2AAPC, http://www.memoryprotectiondevices.com/datasheets/BC2AAPC-datasheet.pdf', 'tags': 'AA battery cell holder', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_MPD_BC2AAPC_2xAA.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Battery : BatteryHolder_MPD_BC2AAPC_2xAA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

