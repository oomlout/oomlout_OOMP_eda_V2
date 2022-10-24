
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Diodes_UDFN-10_1.0x2.5mm_P0.5mm"
    hexID = "FZKDFNDIODESUDFN11X25P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diodes_UDFN-10_1.0x2.5mm_P0.5mm', 'description': 'U-DFN2510-10 package used by Diodes Incorporated (https://www.diodes.com/assets/Package-Files/U-DFN2510-10-Type-CJ.pdf)', 'tags': 'UDFN-10 U-DFN2510-10 Diodes', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Diodes_UDFN-10_1.0x2.5mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Diodes_UDFN-10_1.0x2.5mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

