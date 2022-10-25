
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm"
    hexID = "FZKDFNSTUQFN6L15X17PITCH5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm', 'description': 'ST UQFN 6 pin 0.5mm Pitch http://www.st.com/resource/en/datasheet/ecmf02-2amx6.pdf', 'tags': 'UQFN DFN 0.5 ST', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

