
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "LM75B"
    hexID = "SZKSENTEMPERATURELM75B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM75C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM75B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm75b.pdf', 'kicadSymbolki_keywords': 'Temperature sensor', 'kicadSymbolki_description': 'Digital Temperature Sensor & Thermal Watchdog with LP on I2C and bus fault timeout, SOIC-8 and VSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('LM75B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

