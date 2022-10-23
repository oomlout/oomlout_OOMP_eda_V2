
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_Tantalum_SMD"
    oIndex = "CP_EIA-7132-20_AVX-U"
    hexID = "FZKCAPACITORTANTALUMSMCPEIA71322AVXU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_EIA-7132-20_AVX-U', 'description': 'Tantalum Capacitor SMD AVX-U (7132-20 Metric), IPC_7351 nominal, (Body size from: http://datasheets.avx.com/F72-F75.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor tantalum', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-7132-20_AVX-U.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_Tantalum_SMD : CP_EIA-7132-20_AVX-U')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

