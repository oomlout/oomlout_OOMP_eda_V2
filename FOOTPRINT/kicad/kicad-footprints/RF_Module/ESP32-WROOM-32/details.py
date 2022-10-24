
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "ESP32-WROOM-32"
    hexID = "FZKRFMOESP32WROOM32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ESP32-WROOM-32', 'description': 'Single 2.4 GHz Wi-Fi and Bluetooth combo chip https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf', 'tags': 'Single 2.4 GHz Wi-Fi and Bluetooth combo  chip', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/ESP32-WROOM-32.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : ESP32-WROOM-32')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

