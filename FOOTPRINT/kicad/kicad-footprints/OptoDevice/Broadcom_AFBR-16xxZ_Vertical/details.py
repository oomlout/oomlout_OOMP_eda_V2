
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Broadcom_AFBR-16xxZ_Vertical"
    hexID = "FZKOPBROADCOMAFBR16XXZVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Broadcom_AFBR-16xxZ_Vertical', 'description': 'Fiber Optic Transmitter and Receiver, https://docs.broadcom.com/docs/AV02-4369EN', 'tags': 'Fiber Optic Transmitter and Receiver', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Broadcom_AFBR-16xxZ_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('OptoDevice : Broadcom_AFBR-16xxZ_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

