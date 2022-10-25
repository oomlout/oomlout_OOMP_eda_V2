
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_Tantalum_SMD"
    oIndex = "CP_EIA-1608-08_AVX-J_Pad1.25x1.05mm_HandSolder"
    hexID = "FZKCAPACITORTANTALUMSMCPEIA1688AVXJPAD125X15HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_EIA-1608-08_AVX-J_Pad1.25x1.05mm_HandSolder', 'description': 'Tantalum Capacitor SMD AVX-J (1608-08 Metric), IPC_7351 nominal, (Body size from: https://www.vishay.com/docs/48064/_t58_vmn_pt0471_1601.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor tantalum', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-1608-08_AVX-J.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_Tantalum_SMD : CP_EIA-1608-08_AVX-J_Pad1.25x1.05mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

