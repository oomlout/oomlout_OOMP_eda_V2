
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "HS-40005"
    hexID = "SZKCONHS45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HS-40003', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'HS-40005', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Hahn_HS-400xx_THT', 'kicadSymbolDatasheet': 'http://www.tme.eu/de/Document/996b08915f81126361ce1f9c12d2f8b9/HS40005.pdf', 'kicadSymbolki_keywords': '5V 3W AC-DC module power supply', 'kicadSymbolki_description': '5V, 3W, AC-DC module power supply, Hahn', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Hahn*HS*400xx*'}])
    newPart['name'].append('Converter_ACDC : HS-40005')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

