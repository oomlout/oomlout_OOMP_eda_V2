
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "SIMCom_SIM900"
    hexID = "FZKGSMSIMCOMSIM9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SIMCom_SIM900', 'description': 'Quad-Band GSM/GPRS module, 24x24x3mm, http://simcom.ee/documents/SIM900/SIM900_Hardware%20Design_V2.05.pdf', 'tags': 'GSM Module SIM900', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/SIMCom_SIM900.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('RF_GSM : SIMCom_SIM900')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

