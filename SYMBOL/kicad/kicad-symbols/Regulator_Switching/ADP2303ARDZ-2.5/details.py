
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADP2303ARDZ-2.5"
    hexID = "SZKREGULATORSWITCHINGADP233ARDZ25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADP2302ARDZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP2303ARDZ-2.5', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP2302_2303.pdf', 'kicadSymbolki_keywords': 'Step-Down Regulator', 'kicadSymbolki_description': 'Nonsynchronous Step-Down Regulator 3 Amp Vout 2.5v SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : ADP2303ARDZ-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

