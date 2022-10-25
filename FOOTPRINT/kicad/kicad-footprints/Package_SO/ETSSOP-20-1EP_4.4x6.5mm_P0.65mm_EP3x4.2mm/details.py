
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "ETSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3x4.2mm"
    hexID = "FZKSOETSS21EP44X65P65EP3X42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ETSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3x4.2mm', 'description': '20-Lead Plastic Thin Shrink Small Outline (ST)-4.4 mm Body with Exposed Pad [eTSSOP] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'SSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/ETSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3x4.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : ETSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3x4.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

