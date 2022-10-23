
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_Elec_8x5.4"
    hexID = "FZKCAPACITORSMCELEC8X54"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Elec_8x5.4', 'description': 'SMD capacitor, aluminum electrolytic nonpolar, 8.0x5.4mm', 'tags': 'capacitor electrolyic nonpolar', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Elec_8x5.4.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Capacitor_SMD : C_Elec_8x5.4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

