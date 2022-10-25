
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "VSO-56_11.1x21.5mm_P0.75mm"
    hexID = "FZKSOVSO56111X215P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VSO-56_11.1x21.5mm_P0.75mm', 'description': 'VSO56: plastic very small outline package; 56 leads (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot190-1_po.pdf)', 'tags': 'SSOP 0.75', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/VSO-56_11.1x21.5mm_P0.75mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : VSO-56_11.1x21.5mm_P0.75mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

