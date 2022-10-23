
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_Tantalum_SMD"
    oIndex = "CP_EIA-7361-38_AVX-V"
    hexID = "FZKCAPACITORTANTALUMSMCPEIA736138AVXV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_EIA-7361-38_AVX-V', 'description': 'Tantalum Capacitor SMD AVX-V (7361-38 Metric), IPC_7351 nominal, (Body size from: http://datasheets.avx.com/NOS.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor tantalum', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-7361-38_AVX-V.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_Tantalum_SMD : CP_EIA-7361-38_AVX-V')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

