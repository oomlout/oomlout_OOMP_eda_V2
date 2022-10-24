
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "Senseair_S8_Down"
    hexID = "FZKSENSENSEAIRS8DOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Senseair_S8_Down', 'description': 'Sensair S8 Series CO2 sensor, 1kHz PWM output, Modbus, THT', 'tags': 'co2 gas sensor pwm modbus', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Senseair_S8_Down.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor : Senseair_S8_Down')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

