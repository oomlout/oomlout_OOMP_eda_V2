
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "MV267"
    hexID = "SZKOCSMV267"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MV267', 'kicadSymbolFootprint': 'Oscillator:Oscillator_OCXO_Morion_MV267', 'kicadSymbolDatasheet': 'http://www.morion.com.ru/catalog_pdf/MV267.pdf', 'kicadSymbolki_keywords': 'OCXO', 'kicadSymbolki_description': '5/10 MHz Low Phase-Noise Precision OCXO, Morion MV267', 'kicadSymbolki_fp_filters': 'Oscillator*OCXO*Morion*MV267*'}])
    newPart['name'].append('Oscillator : MV267')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

