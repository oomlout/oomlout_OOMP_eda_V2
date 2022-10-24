
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_Rectangular_W7.62mm_H4.55mm_P5.08mm_R3"
    hexID = "FZKLLRW762H455P58R3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Rectangular_W7.62mm_H4.55mm_P5.08mm_R3', 'description': 'Datasheet can be found at https://www.gme.cz/data/attachments/dsh.511-795.1.pdf', 'tags': 'LED automotive super flux 7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_Rectangular_W7.62mm_H4.55mm_P5.08mm_R3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_Rectangular_W7.62mm_H4.55mm_P5.08mm_R3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

