
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_Rectangular_W3.9mm_H1.9mm"
    hexID = "FZKLLRW39H19"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Rectangular_W3.9mm_H1.9mm', 'description': 'LED_Rectangular, Rectangular,  Rectangular size 3.9x1.9mm^2, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-144GDT(Ver.14B).pdf', 'tags': 'LED_Rectangular Rectangular  Rectangular size 3.9x1.9mm^2 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_Rectangular_W3.9mm_H1.9mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_Rectangular_W3.9mm_H1.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

