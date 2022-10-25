
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "ADG733BRU"
    hexID = "SZKANALOGSWITCHADG733BRU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADG633YRU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADG733BRU', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG733_734.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Triple SPDT CMOS Analog Switch, 2.5Ohm Ron, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Analog_Switch : ADG733BRU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

