
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "AS3935"
    hexID = "SZKSENAS3935"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS3935', 'kicadSymbolFootprint': 'Package_DFN_QFN:MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm', 'kicadSymbolDatasheet': 'https://www.embeddedadventures.com/datasheets/AS3935_Datasheet_EN_v2.pdf', 'kicadSymbolki_keywords': 'lightning sensor', 'kicadSymbolki_description': 'Programmable fully integrated Lightning Sensor IC', 'kicadSymbolki_fp_filters': '*MLPQ*16*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Sensor : AS3935')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

