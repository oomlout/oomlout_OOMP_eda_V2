
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "A3214ELHLT-T"
    hexID = "SZKSENMAGNETICA3214ELHLTT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1301KLHLT-T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A3214ELHLT-T', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23W', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A3213-4-Datasheet.ashx', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'Linear Hall Effect Sensor, SOT-23W', 'kicadSymbolki_fp_filters': 'SOT?23W*'}])
    newPart['name'].append('Sensor_Magnetic : A3214ELHLT-T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

