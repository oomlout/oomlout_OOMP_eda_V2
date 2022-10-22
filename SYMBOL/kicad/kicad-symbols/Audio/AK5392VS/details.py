
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "AK5392VS"
    hexID = "SZKAUDIOAK5392VS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AK5392VS', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x18.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/AKM%20Semiconductor%20Inc.%20PDFs/AK5392.pdf', 'kicadSymbolki_keywords': 'audio adc 2ch 24bit', 'kicadSymbolki_description': 'Enhanced Dual Bit Sigma-Delta 24Bit ADC, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x18.7mm*P1.27mm*'}])
    newPart['name'].append('AK5392VS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

