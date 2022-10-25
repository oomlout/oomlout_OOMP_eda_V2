
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ISO7342FC"
    hexID = "SZKISOLATORISO7342FC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ISO7342C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISO7342FC', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=iso7342fc&fileType=pdf', 'kicadSymbolki_keywords': '4Ch Quad Digital Isolator 25Mbps', 'kicadSymbolki_description': 'Low Power Quad-Channel 2/2 Digital Isolator, 25Mbps 31ns, Fail-Safe Low, SO16', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('Isolator : ISO7342FC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

