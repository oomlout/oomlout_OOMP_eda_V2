
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "ST_MultiPowerSO-30"
    hexID = "FZKSOSTMULTIPOWERSO3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_MultiPowerSO-30', 'description': 'MultiPowerSO-30 3EP 16.0x17.2mm Pitch 1mm (http://www.st.com/resource/en/datasheet/vnh2sp30-e.pdf)', 'tags': 'MultiPowerSO-30 3EP 16.0x17.2mm Pitch 1mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/ST_MultiPowerSO-30.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : ST_MultiPowerSO-30')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

