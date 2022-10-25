
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Qorvo_DFN-8-1EP_2x2mm_P0.5mm"
    hexID = "FZKDFNQORVODFN81EP2X2P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Qorvo_DFN-8-1EP_2x2mm_P0.5mm', 'description': 'DFN 8 2x2mm, 0.5mm http://www.qorvo.com/products/d/da000896', 'tags': 'DFN 0.5 Qorvo 2x2mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Qorvo_DFN-8-1EP_2x2mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Qorvo_DFN-8-1EP_2x2mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

