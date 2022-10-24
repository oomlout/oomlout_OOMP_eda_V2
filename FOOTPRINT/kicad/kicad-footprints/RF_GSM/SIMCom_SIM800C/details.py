
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "SIMCom_SIM800C"
    hexID = "FZKGSMSIMCOMSIM8C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SIMCom_SIM800C', 'description': 'Quad-Band GSM/GPRS module, 17.6x15.7x2.3mm, http://simcom.ee/documents/SIM800C/SIM800C_Hardware_Design_V1.05.pdf', 'tags': 'GSM Module SIM800C', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/SIMCom_SIM800C.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('RF_GSM : SIMCom_SIM800C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

