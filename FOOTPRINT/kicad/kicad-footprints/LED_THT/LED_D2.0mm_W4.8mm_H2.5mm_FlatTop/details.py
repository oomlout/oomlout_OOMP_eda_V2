
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_D2.0mm_W4.8mm_H2.5mm_FlatTop"
    hexID = "FZKLLD2W48H25FLATTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_D2.0mm_W4.8mm_H2.5mm_FlatTop', 'description': 'LED, Round, FlatTop,  Rectangular size 4.8x2.5mm^2 diameter 2.0mm, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-13GD(Ver.11B).pdf', 'tags': 'LED Round FlatTop  Rectangular size 4.8x2.5mm^2 diameter 2.0mm 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D2.0mm_W4.8mm_H2.5mm_FlatTop.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_D2.0mm_W4.8mm_H2.5mm_FlatTop')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

