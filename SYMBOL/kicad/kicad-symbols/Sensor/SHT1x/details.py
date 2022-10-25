
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "SHT1x"
    hexID = "SZKSENSHT1X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SHT1x', 'kicadSymbolFootprint': 'Sensor:SHT1x', 'kicadSymbolDatasheet': 'https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/0_Datasheets/Humidity/Sensirion_Humidity_Sensors_SHT1x_Datasheet.pdf', 'kicadSymbolki_keywords': 'digital temperature humidity sensor', 'kicadSymbolki_description': 'Temperature and humidity module', 'kicadSymbolki_fp_filters': 'SHT1x*'}])
    newPart['name'].append('Sensor : SHT1x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

