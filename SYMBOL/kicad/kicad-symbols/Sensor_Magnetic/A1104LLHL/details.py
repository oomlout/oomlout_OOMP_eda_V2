
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "A1104LLHL"
    hexID = "SZKSENMAGNETICA114LLHL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1101ELHL', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1104LLHL', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23W', 'kicadSymbolDatasheet': 'https://www.allegromicro.com/-/media/files/datasheets/a110x-datasheet.ashx', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'Hall effect switch, unipolar, Bop=240G, Brp=200G, -40C to +125C, SOT-23W', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Sensor_Magnetic : A1104LLHL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

