
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "MPL3115A2"
    hexID = "SZKSENPRESSUREMPL3115A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPL3115A2', 'kicadSymbolFootprint': 'Package_LGA:NXP_LGA-8_3x5mm_P1.25mm_H1.1mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf', 'kicadSymbolki_keywords': 'pressure sensor altimetry', 'kicadSymbolki_description': 'I2C precision pressure sensor with altimetry, LGA-8', 'kicadSymbolki_fp_filters': 'NXP*LGA*3x5mm*P1.25mm*H1.1mm*'}])
    newPart['name'].append('MPL3115A2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

