
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSSOP-44_4.4x11.2mm_P0.5mm"
    hexID = "FZKSOTSS4444X112P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSSOP-44_4.4x11.2mm_P0.5mm', 'description': 'TSSOP44: plastic thin shrink small outline package; 44 leads; body width 4.4 mm (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot510-1_po.pdf)', 'tags': 'SSOP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-44_4.4x11.2mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TSSOP-44_4.4x11.2mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

