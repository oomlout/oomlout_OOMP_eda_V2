
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Panasonic_HSON-8_8x8mm_P2.00mm"
    hexID = "FZKDFNPHSON88X8P2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Panasonic_HSON-8_8x8mm_P2.00mm', 'description': 'Panasonic HSON-8, 8x8x1.25mm (https://industrial.panasonic.com/content/data/SC/ds/ds7/c0/PKG_HSON008-A-0808XXI_EN.pdf)', 'tags': 'panasonic hson', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Panasonic_HSON-8_8x8mm_P2.00mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Panasonic_HSON-8_8x8mm_P2.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

