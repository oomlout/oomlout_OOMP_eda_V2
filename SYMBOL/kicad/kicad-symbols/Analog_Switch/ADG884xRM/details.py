
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "ADG884xRM"
    hexID = "SZKANALOGSWITCHADG884XRM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADG884xRM', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG884.pdf', 'kicadSymbolki_keywords': 'analog switch', 'kicadSymbolki_description': '0.5Ω CMOS, Dual 2:1 MUX/SPDT Audio Switch, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_Switch : ADG884xRM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

