
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "OnSemi_DFN-8_2x2mm_P0.5mm"
    hexID = "FZKDFNONSEMIDFN82X2P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OnSemi_DFN-8_2x2mm_P0.5mm', 'description': 'DFN8 2x2, 0.5P (https://www.onsemi.com/pub/Collateral/511AT.PDF)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_DFN-8_2x2mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : OnSemi_DFN-8_2x2mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

