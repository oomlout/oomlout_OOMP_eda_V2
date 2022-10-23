
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "MPL115A1"
    hexID = "SZKSENPRESSUREMPL115A1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPL115A1', 'kicadSymbolFootprint': 'Package_LGA:NXP_LGA-8_3x5mm_P1.25mm_H1.2mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/assets/documents/data/en/data-sheets/MPL115A1.pdf', 'kicadSymbolki_keywords': 'spi barometer thermometer mems', 'kicadSymbolki_description': 'SPI Digital Barometer', 'kicadSymbolki_fp_filters': 'NXP*LGA*3x5mm*P1.25mm*H1.2mm*'}])
    newPart['name'].append('MPL115A1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

