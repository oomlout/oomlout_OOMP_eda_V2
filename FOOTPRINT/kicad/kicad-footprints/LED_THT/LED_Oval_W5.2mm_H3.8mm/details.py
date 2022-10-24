
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_Oval_W5.2mm_H3.8mm"
    hexID = "FZKLLOVALW52H38"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Oval_W5.2mm_H3.8mm', 'description': 'LED_Oval, Oval,  Oval size 5.2x3.8mm^2, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-5603QBC-D(Ver.12B).pdf', 'tags': 'LED_Oval Oval  Oval size 5.2x3.8mm^2 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_Oval_W5.2mm_H3.8mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_Oval_W5.2mm_H3.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

