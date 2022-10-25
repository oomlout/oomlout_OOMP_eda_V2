
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_Schrack-RP-II-1-FormA_RM5mm"
    hexID = "FZKRELRELAYSPSTSCHRACKRPII1FORMARM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_Schrack-RP-II-1-FormA_RM5mm', 'description': 'Relay SPST Schrack-RP-II/1 RM5mm 8A 250V AC Form A http://image.schrack.com/datenblaetter/h_rp810012-b.pdf', 'tags': 'Relay SPST Schrack-RP-II/1 RM5mm 8A 250V AC Relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_Schrack-RP-II-1-FormA_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_SPST_Schrack-RP-II-1-FormA_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

