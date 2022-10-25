
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_Tantalum_SMD"
    oIndex = "CP_EIA-6032-20_AVX-F_Pad2.25x2.35mm_HandSolder"
    hexID = "FZKCAPACITORTANTALUMSMCPEIA6322AVXFPAD225X235HANDSOLDER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_EIA-6032-20_AVX-F_Pad2.25x2.35mm_HandSolder', 'description': 'Tantalum Capacitor SMD AVX-F (6032-20 Metric), IPC_7351 nominal, (Body size from: http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor tantalum', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-6032-20_AVX-F.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_Tantalum_SMD : CP_EIA-6032-20_AVX-F_Pad2.25x2.35mm_HandSolder')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

