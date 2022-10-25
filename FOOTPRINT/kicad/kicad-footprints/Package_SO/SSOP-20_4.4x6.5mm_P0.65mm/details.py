
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-20_4.4x6.5mm_P0.65mm"
    hexID = "FZKSOSS244X65P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-20_4.4x6.5mm_P0.65mm', 'description': 'SSOP20: plastic shrink small outline package; 20 leads; body width 4.4 mm; (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot266-1_po.pdf)', 'tags': 'SSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-20_4.4x6.5mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-20_4.4x6.5mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

