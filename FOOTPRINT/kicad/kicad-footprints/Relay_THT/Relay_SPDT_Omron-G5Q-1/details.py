
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPDT_Omron-G5Q-1"
    hexID = "FZKRELRELAYSPDTOMRONG5Q1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_Omron-G5Q-1', 'description': 'Relay SPDT Omron Serie G5Q, http://omronfs.omron.com/en_US/ecb/products/pdf/en-g5q.pdf', 'tags': 'Relay SPDT Omron Serie G5Q', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPDT_Omron-G5Q-1.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_SPDT_Omron-G5Q-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

