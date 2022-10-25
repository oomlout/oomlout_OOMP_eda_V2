
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Current"
    oIndex = "LT3092xDD"
    hexID = "SZKREFERENCECURRENTLT392XDD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3092xDD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.5mm_EP1.66x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3092fc.pdf', 'kicadSymbolki_keywords': 'current source', 'kicadSymbolki_description': '200mA 2-Terminal Programmable Current Source, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Reference_Current : LT3092xDD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

