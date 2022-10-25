
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "HS-40003"
    hexID = "SZKCONHS43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'HS-40003', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Hahn_HS-400xx_THT', 'kicadSymbolDatasheet': 'http://www.tme.eu/de/Document/d4b3c52125889c3435af182c9515c76b/HS40003.pdf', 'kicadSymbolki_keywords': '3.3V 3W AC-DC module power supply', 'kicadSymbolki_description': '3.3V, 3W, AC-DC module power supply, Hahn', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Hahn*HS*400xx*'}])
    newPart['name'].append('Converter_ACDC : HS-40003')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

