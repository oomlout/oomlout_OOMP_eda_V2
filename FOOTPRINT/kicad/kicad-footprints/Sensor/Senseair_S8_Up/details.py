
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "Senseair_S8_Up"
    hexID = "FZKSENSENSEAIRS8UP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Senseair_S8_Up', 'description': 'Sensair S8 Series CO2 sensor, 1kHz PWM output, Modbus, THT', 'tags': 'co2 gas sensor pwm modbus', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Senseair_S8_Up.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor : Senseair_S8_Up')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

