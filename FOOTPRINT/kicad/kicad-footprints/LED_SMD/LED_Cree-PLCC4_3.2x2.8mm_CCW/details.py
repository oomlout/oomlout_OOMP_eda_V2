
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Cree-PLCC4_3.2x2.8mm_CCW"
    hexID = "FZKLSMLCREEPLCC432X28CCW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Cree-PLCC4_3.2x2.8mm_CCW', 'description': '3.2mm x 2.8mm PLCC4 LED, http://www.cree.com/led-components/media/documents/CLV1AFKB(874).pdf', 'tags': 'LED Cree PLCC-4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-PLCC4_3.2x2.8mm_CCW.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Cree-PLCC4_3.2x2.8mm_CCW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

