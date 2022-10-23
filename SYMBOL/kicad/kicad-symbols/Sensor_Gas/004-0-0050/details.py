
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Gas"
    oIndex = "004-0-0050"
    hexID = "SZKSENGAS45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '004-0-0013', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '004-0-0050', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://rmtplusstoragesenseair.blob.core.windows.net/docs/publicerat/PSP108.pdf', 'kicadSymbolki_keywords': 'Senseair co2 gas sensor pwm modbus', 'kicadSymbolki_description': 'S8 2%, CO2 sensor, 0.04-2% by volume, 1kHz PWM output, Modbus, THT', 'kicadSymbolki_fp_filters': 'Senseair*S8*'}])
    newPart['name'].append('004-0-0050')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

