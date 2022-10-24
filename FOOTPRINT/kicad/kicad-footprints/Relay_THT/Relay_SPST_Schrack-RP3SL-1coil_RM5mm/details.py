
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_Schrack-RP3SL-1coil_RM5mm"
    hexID = "FZKRELRELAYSPSTSCHRACKRP3SL1COILRM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_Schrack-RP3SL-1coil_RM5mm', 'description': 'Relay SPST Schrack-RP3SL, 1-coil-version, RM5mm 16A 250V AC Form A http://www.alliedelec.com/m/d/543c6bed18bf23a83ae5238947033ee0.pdf', 'tags': 'Relay SPST Schrack-RP3SL RM5mm 16A 250V AC Relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_Schrack-RP3SL-1coil_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_SPST_Schrack-RP3SL-1coil_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

