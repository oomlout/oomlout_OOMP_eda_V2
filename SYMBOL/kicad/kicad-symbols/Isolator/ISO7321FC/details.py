
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ISO7321FC"
    hexID = "SZKISOLATORISO7321FC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ISO7321C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISO7321FC', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=iso7321fc&fileType=pdf', 'kicadSymbolki_keywords': '2Ch Dual Digital Isolator 25Mbps', 'kicadSymbolki_description': 'Low Power Dual-Channel 1/1 Digital Isolator, 25Mbps 33ns, Fail-Safe Low, SO8', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('Isolator : ISO7321FC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

