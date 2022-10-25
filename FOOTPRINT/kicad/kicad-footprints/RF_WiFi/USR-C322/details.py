
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_WiFi"
    oIndex = "USR-C322"
    hexID = "FZKRFUSRC322"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USR-C322', 'description': 'https://www.usriot.com/download/WIFI/USR-C322-Hardware-Manual_V1.2.01.pdf', 'tags': 'WiFi IEEE802.11 b/g/n', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_WiFi.3dshapes/USR-C322.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_WiFi : USR-C322')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

