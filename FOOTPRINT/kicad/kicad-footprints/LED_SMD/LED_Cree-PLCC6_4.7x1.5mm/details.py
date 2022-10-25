
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Cree-PLCC6_4.7x1.5mm"
    hexID = "FZKLSMLCREEPLCC647X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Cree-PLCC6_4.7x1.5mm', 'description': '4.7mm x 1.5mm PLCC6 LED, http://www.cree.com/led-components/media/documents/1381-QLS6AFKW.pdf', 'tags': 'LED Cree PLCC-6', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-PLCC6_4.7x1.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Cree-PLCC6_4.7x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

