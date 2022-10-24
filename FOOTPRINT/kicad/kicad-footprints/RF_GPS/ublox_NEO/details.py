
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GPS"
    oIndex = "ublox_NEO"
    hexID = "FZKGPSUBLOXNEO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ublox_NEO', 'description': 'ublox NEO 6/7/8, (https://www.u-blox.com/sites/default/files/NEO-8Q-NEO-M8-FW3_HardwareIntegrationManual_%28UBX-15029985%29_0.pdf)', 'tags': 'GPS ublox NEO 6/7/8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/ublox_NEO.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('RF_GPS : ublox_NEO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

