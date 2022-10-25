
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-20_3.9x8.7mm_P0.635mm"
    hexID = "FZKSOSS239X87P635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-20_3.9x8.7mm_P0.635mm', 'description': 'SSOP20: plastic shrink small outline package; 24 leads; body width 3.9 mm; lead pitch 0.635; (see http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT231X.pdf)', 'tags': 'SSOP 0.635', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-20_3.9x8.7mm_P0.635mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-20_3.9x8.7mm_P0.635mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

