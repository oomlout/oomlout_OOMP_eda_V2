
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Sumida_CR75"
    hexID = "FZKINDUCTORSMLSUMIDACR75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Sumida_CR75', 'description': 'Inductor, Sumida, 8.1mm × 7.3mm × 5.5 mm, Unshielded, http://products.sumida.com/products/pdf/CR75.pdf', 'tags': 'Inductor SMD CR75 Unshielded', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Sumida_CR75.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_Sumida_CR75')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

