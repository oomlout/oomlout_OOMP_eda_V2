
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "RAK811"
    hexID = "FZKRFMORAK811"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RAK811', 'description': 'RAK811 LPWAN Module https://downloads.rakwireless.com/LoRa/RAK811/Hardware_Specification/RAK811_LoRa_Module_Datasheet_V1.4.pdf', 'tags': 'LoRa LoRaWAN RAK811', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/RAK811.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : RAK811')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

