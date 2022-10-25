
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_TracoPower_TCK-141"
    hexID = "FZKINDUCTORSMLTRACOPOWERTCK141"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_TracoPower_TCK-141', 'description': 'Choke, SMD, 4.0x4.0mm 2.1mm height, https://www.tracopower.com/products/tck141.pdf', 'tags': 'Choke SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_TracoPower_TCK-141.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_TracoPower_TCK-141')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

