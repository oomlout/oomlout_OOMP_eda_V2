
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm"
    hexID = "FZKLLD18W18H24HORIZONTALO381Z16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm', 'description': 'LED, ,  diameter 1.8mm size 1.8x2.4mm^2 z-position of LED center 1.6mm, 2 pins,  diameter 1.8mm size 1.8x2.4mm^2 z-position of LED center 1.6mm, 2 pins', 'tags': 'LED   diameter 1.8mm size 1.8x2.4mm^2 z-position of LED center 1.6mm 2 pins  diameter 1.8mm size 1.8x2.4mm^2 z-position of LED center 1.6mm 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

