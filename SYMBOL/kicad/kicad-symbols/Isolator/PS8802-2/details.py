
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "PS8802-2"
    hexID = "SZKISOLATORPS8822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PS8802-2', 'kicadSymbolFootprint': 'Package_SO:SSOP-8_3.95x5.21x3.27mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.cel.com/pdf/datasheets/ps8802.pdf', 'kicadSymbolki_keywords': 'Dual NPN DC Optocoupler Base Connected', 'kicadSymbolki_description': 'Dual DC Optocoupler Base Connected, Vcc 35V, CTR 15%, Viso 2500V, SSOP-8', 'kicadSymbolki_fp_filters': 'SSOP*3.95x5.21x3.27mm?P1.27mm*'}])
    newPart['name'].append('Isolator : PS8802-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

