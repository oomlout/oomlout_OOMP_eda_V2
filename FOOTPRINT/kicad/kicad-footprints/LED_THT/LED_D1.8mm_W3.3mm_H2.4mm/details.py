
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_D1.8mm_W3.3mm_H2.4mm"
    hexID = "FZKLLD18W33H24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_D1.8mm_W3.3mm_H2.4mm', 'description': 'LED, Round,  Rectangular size 3.3x2.4mm^2 diameter 1.8mm, 2 pins', 'tags': 'LED Round  Rectangular size 3.3x2.4mm^2 diameter 1.8mm 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D1.8mm_W3.3mm_H2.4mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_D1.8mm_W3.3mm_H2.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

