
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "ublox_SARA-G3_LGA-96"
    hexID = "FZKGSMUBLOXSARAG3LGA96"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ublox_SARA-G3_LGA-96', 'description': 'ublox Sara GSM/HSPA modem, https://www.u-blox.com/sites/default/files/SARA-G3-U2_SysIntegrManual_%28UBX-13000995%29.pdf, pag.162', 'tags': 'ublox SARA-G3 SARA-U2 GSM HSPA', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/ublox_SARA-G3_LGA-96.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_GSM : ublox_SARA-G3_LGA-96')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

