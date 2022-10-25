
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PWQFN-N20"
    hexID = "FZKDFNTEXASSPWQFNN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PWQFN-N20', 'description': '20-Pin Plastic Quad Flatpack No-Lead Package, Body 3.0x3.0x0.8mm, Texas Instruments (http://www.ti.com/lit/ds/symlink/tps22993.pdf)', 'tags': 'QFN 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N20.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PWQFN-N20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

