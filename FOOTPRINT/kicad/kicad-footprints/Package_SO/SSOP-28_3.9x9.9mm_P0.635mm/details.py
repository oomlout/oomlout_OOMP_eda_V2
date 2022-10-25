
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-28_3.9x9.9mm_P0.635mm"
    hexID = "FZKSOSS2839X99P635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-28_3.9x9.9mm_P0.635mm', 'description': 'SSOP28: plastic shrink small outline package; 28 leads; body width 3.9 mm; lead pitch 0.635; (see http://cds.linear.com/docs/en/datasheet/38901fb.pdf)', 'tags': 'SSOP 0.635', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-28_3.9x9.9mm_P0.635mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-28_3.9x9.9mm_P0.635mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

