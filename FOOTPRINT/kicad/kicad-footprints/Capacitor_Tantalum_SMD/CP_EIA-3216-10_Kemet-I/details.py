
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_Tantalum_SMD"
    oIndex = "CP_EIA-3216-10_Kemet-I"
    hexID = "FZKCAPACITORTANTALUMSMCPEIA32161KEMETI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_EIA-3216-10_Kemet-I', 'description': 'Tantalum Capacitor SMD Kemet-I (3216-10 Metric), IPC_7351 nominal, (Body size from: http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor tantalum', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-3216-10_Kemet-I.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_Tantalum_SMD : CP_EIA-3216-10_Kemet-I')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

