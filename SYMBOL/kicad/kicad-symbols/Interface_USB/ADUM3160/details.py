
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "ADUM3160"
    hexID = "SZKINTERFACEUADUM316"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADUM4160', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADUM3160', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM3160.pdf', 'kicadSymbolki_keywords': 'usb isolation', 'kicadSymbolki_description': 'Full/Low Speed, iCoupler USB Digital Isolator, 2.5kV protection', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Interface_USB : ADUM3160')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

