
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_1-Form-C_Schrack-RYII_RM3.2mm"
    hexID = "FZKRELRELAY1FORMCSCHRACKRYIIRM32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_1-Form-C_Schrack-RYII_RM3.2mm', 'description': 'Relay, 1-Form-C, Schrack-RYII, RM3.2mm, SPDT', 'tags': 'Relay 1-Form-C Schrack-RYII RM3.2mm SPDT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_1-Form-C_Schrack-RYII_RM3.2mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_1-Form-C_Schrack-RYII_RM3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

