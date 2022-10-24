
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_Omron-G5Q-1A"
    hexID = "FZKRELRELAYSPSTOMRONG5Q1A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_Omron-G5Q-1A', 'description': 'Relay SPST-NO Omron Serie G5Q, http://omronfs.omron.com/en_US/ecb/products/pdf/en-g5q.pdf', 'tags': 'Relay SPST-NO Omron Serie G5Q', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_Omron-G5Q-1A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_SPST_Omron-G5Q-1A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

