
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_Tantalum_SMD"
    oIndex = "CP_EIA-1608-10_AVX-L_Pad1.25x1.05mm_HandSolder"
    hexID = "FZKCAPACITORTANTALUMSMCPEIA1681AVXLPAD125X15HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_EIA-1608-10_AVX-L_Pad1.25x1.05mm_HandSolder', 'description': 'Tantalum Capacitor SMD AVX-L (1608-10 Metric), IPC_7351 nominal, (Body size from: https://www.vishay.com/docs/48064/_t58_vmn_pt0471_1601.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor tantalum', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-1608-10_AVX-L.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_Tantalum_SMD : CP_EIA-1608-10_AVX-L_Pad1.25x1.05mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

