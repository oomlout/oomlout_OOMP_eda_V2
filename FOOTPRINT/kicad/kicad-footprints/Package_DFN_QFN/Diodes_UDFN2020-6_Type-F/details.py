
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Diodes_UDFN2020-6_Type-F"
    hexID = "FZKDFNDIODESUDFN226TYPEF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diodes_UDFN2020-6_Type-F', 'description': 'U-DFN2020-6 (Type F) (https://www.diodes.com/assets/Package-Files/U-DFN2020-6-Type-F.pdf) ', 'tags': 'U-DFN2020-6 (Type F)', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Diodes_UDFN2020-6_Type-F.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Diodes_UDFN2020-6_Type-F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

