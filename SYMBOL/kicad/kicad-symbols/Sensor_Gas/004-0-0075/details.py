
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Gas"
    oIndex = "004-0-0075"
    hexID = "SZKSENGAS475"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '004-0-0013', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '004-0-0075', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP103.pdf', 'kicadSymbolki_keywords': 'Senseair co2 gas sensor pwm modbus', 'kicadSymbolki_description': 'S8 Commercial, CO2 sensor, 400-2000 PPM, 1kHz PWM output, Modbus, THT', 'kicadSymbolki_fp_filters': 'Senseair*S8*'}])
    newPart['name'].append('004-0-0075')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

