
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "Atmel_ATSAMR21G18-MR210UA_NoRFPads"
    hexID = "FZKRFMOATMELATSAMR21G18MR21UANORFPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Atmel_ATSAMR21G18-MR210UA_NoRFPads', 'description': 'http://ww1.microchip.com/downloads/en/devicedoc/atmel-42475-atsamr21g18-mr210ua_datasheet.pdf', 'tags': 'module wireless zigbee 802.15.4 flash crypto ATSAMR21G18 AT45DB041E  TECC508A U.Fi', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/Atmel_ATSAMR21G18-MR210UA_NoRFPads.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : Atmel_ATSAMR21G18-MR210UA_NoRFPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

