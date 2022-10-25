
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "LM20BIM7"
    hexID = "SZKSENTEMPERATURELM2BIM7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM20BIM7', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm20.pdf', 'kicadSymbolki_keywords': 'temperature sensor thermistor', 'kicadSymbolki_description': 'Precision Temperature Sensor, Accuracy at 30°C ±1.5°C to ±4°C Maximum, SC70', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Sensor_Temperature : LM20BIM7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

