
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Infineon_PG-TO-220-7Lead_TabPin8"
    hexID = "FZKPACKAGETOSOTSMINFINEONPGTO227LEADTABPIN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-TO-220-7Lead_TabPin8', 'description': 'Infineon PG-TO-220-7, Tab as Pin 8, see e.g. https://www.infineon.com/dgdl/Infineon-BTS50055-1TMC-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aa9b0007235e9', 'tags': 'Infineon PG-TO-220-7', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Infineon_PG-TO-220-7Lead_TabPin8.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : Infineon_PG-TO-220-7Lead_TabPin8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

