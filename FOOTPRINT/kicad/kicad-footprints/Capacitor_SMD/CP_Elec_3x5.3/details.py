
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "CP_Elec_3x5.3"
    hexID = "FZKCAPACITORSMCPELEC3X53"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Elec_3x5.3', 'description': 'SMT capacitor, aluminium electrolytic, 3x5.3, Cornell Dubilier Electronics ', 'tags': 'Capacitor Electrolytic', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/CP_Elec_3x5.3.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_SMD : CP_Elec_3x5.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

