
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM1201BR"
    hexID = "SZKISOLATORADUM121BR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADuM1201AR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM1201BR', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/ADuM1200_1201.pdf', 'kicadSymbolki_keywords': '2Ch Dual Digital Isolator 10Mbps', 'kicadSymbolki_description': 'Dual-Channel Digital Isolator, 10Mbps 50ns, bidirectional communication, 3V/5V level translation, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Isolator : ADuM1201BR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

