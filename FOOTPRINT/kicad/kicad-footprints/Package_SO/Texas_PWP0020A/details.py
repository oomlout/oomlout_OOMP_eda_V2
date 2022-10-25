
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Texas_PWP0020A"
    hexID = "FZKSOTEXASPWP2A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_PWP0020A', 'description': '20-Pin Thermally Enhanced Thin Shrink Small-Outline Package, Body 4.4x6.5x1.1mm, Pad 3.0x4.2mm, Texas Instruments (see http://www.ti.com/lit/ds/symlink/lm5118.pdf)', 'tags': 'PWP HTSSOP 0.65mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Texas_PWP0020A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Texas_PWP0020A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

