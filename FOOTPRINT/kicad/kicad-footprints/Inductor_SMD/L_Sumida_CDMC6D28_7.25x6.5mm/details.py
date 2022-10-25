
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Sumida_CDMC6D28_7.25x6.5mm"
    hexID = "FZKINDUCTORSMLSUMIDACDMC6D28725X65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Sumida_CDMC6D28_7.25x6.5mm', 'description': 'SMD Power Inductor (http://products.sumida.com/products/pdf/CDMC6D28.pdf)', 'tags': 'Inductor Sumida SMD CDMC6D28', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Sumida_CDMC6D28_7.25x6.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Sumida_CDMC6D28_7.25x6.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

