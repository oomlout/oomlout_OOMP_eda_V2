
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_1-Form-A_Schrack-RYII_RM5mm"
    hexID = "FZKRELRELAY1FORMASCHRACKRYIIRM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_1-Form-A_Schrack-RYII_RM5mm', 'description': 'Relay, 1-Form-A, Schrack-RYII, RM5mm, SPST-NO', 'tags': 'Relay 1-Form-A Schrack-RYII RM5mm SPST-NO', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_1-Form-A_Schrack-RYII_RM5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_1-Form-A_Schrack-RYII_RM5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

