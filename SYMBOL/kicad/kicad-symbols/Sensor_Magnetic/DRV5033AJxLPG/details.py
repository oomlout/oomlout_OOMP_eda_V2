
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "DRV5033AJxLPG"
    hexID = "SZKSENMAGNETICDRV533AJXLPG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DRV5055A1xLPGxQ1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV5033AJxLPG', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/drv5033.pdf', 'kicadSymbolki_keywords': 'Digital Omnipolar Switch Hall Effect Sensor', 'kicadSymbolki_description': '±6.9 / ±3.5 mT, 20-kHz, 2-38V, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Sensor_Magnetic : DRV5033AJxLPG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

