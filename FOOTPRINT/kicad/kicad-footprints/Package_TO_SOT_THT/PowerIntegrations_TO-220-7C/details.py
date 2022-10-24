
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "PowerIntegrations_TO-220-7C"
    hexID = "FZKSOTPOWERINTEGRATIONSTO227C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_TO-220-7C', 'description': 'Non Isolated Modified TO-220 7pin Package, see http://www.farnell.com/datasheets/5793.pdf', 'tags': 'Power Integration Y Package', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/PowerIntegrations_TO-220-7C.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : PowerIntegrations_TO-220-7C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

