
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Antenna"
    oIndex = "Abracon_APAES868R8060C16-T"
    hexID = "FZKRFABRACONAPAES868R86C16T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Abracon_APAES868R8060C16-T', 'description': 'Abracon RHCP ceramic patch antenna 854-882Mhz, 5dBi', 'tags': 'APAES patch antenna', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Antenna.3dshapes/Abracon_APAES868R8060C16-T.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('RF_Antenna : Abracon_APAES868R8060C16-T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

