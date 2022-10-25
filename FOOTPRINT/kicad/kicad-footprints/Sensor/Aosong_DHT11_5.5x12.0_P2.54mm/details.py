
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "Aosong_DHT11_5.5x12.0_P2.54mm"
    hexID = "FZKSENAOSONGDHT1155X12P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Aosong_DHT11_5.5x12.0_P2.54mm', 'description': 'Temperature and humidity module, http://akizukidenshi.com/download/ds/aosong/DHT11.pdf', 'tags': 'Temperature and humidity module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Aosong_DHT11_5.5x12.0_P2.54mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor : Aosong_DHT11_5.5x12.0_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

