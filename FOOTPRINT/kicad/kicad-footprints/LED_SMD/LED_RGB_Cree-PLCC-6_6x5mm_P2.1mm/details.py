
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_RGB_Cree-PLCC-6_6x5mm_P2.1mm"
    hexID = "FZKLSMLRGBCREEPLCC66X5P21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_RGB_Cree-PLCC-6_6x5mm_P2.1mm', 'description': 'http://www.farnell.com/datasheets/2003905.pdf', 'tags': 'LED RGB PLCC-6 CLP6C-FBK', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_RGB_Cree-PLCC-6_6x5mm_P2.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_RGB_Cree-PLCC-6_6x5mm_P2.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

