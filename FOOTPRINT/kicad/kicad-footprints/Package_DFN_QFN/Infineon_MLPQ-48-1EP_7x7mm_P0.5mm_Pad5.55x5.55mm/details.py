
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm"
    hexID = "FZKDFNINFINEONMLPQ481EP7X7P5PAD555X555"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm', 'description': 'MLPQ 48 leads, 7x7mm (https://www.infineon.com/dgdl/irs2093mpbf.pdf?fileId=5546d462533600a401535675fb892793)', 'tags': 'mlpq 32 7x7mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

