
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GPS"
    oIndex = "Sierra_XM11X0"
    hexID = "FZKGPSSIERRAXM11X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Sierra_XM11X0', 'description': 'QFN-20, Pitch 1.20 no EP, https://source.sierrawireless.com/resources/airprime/hardware_specs_user_guides/airprime_xm1100_product_technical_specification', 'tags': 'QFN-20 P1.20', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/Sierra_XM11X0.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_GPS : Sierra_XM11X0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

