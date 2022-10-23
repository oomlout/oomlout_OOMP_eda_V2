
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "TSIC306-TO92"
    hexID = "SZKSENTEMPERATURETSIC36TO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSIC206-TO92', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSIC306-TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://shop.bb-sensors.com/out/media/Datasheet_Digital_Semiconductor_temperatur_sensor_TSIC.pdf', 'kicadSymbolki_keywords': 'temperature digital', 'kicadSymbolki_description': 'Digital temperature sensor, range -50 ... +150 °C, 0.3 K accuracy, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*Inline*Narrow*Oval*'}])
    newPart['name'].append('TSIC306-TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

