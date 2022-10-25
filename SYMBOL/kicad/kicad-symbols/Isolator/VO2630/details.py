
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "VO2630"
    hexID = "SZKISOLATORVO263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-263A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VO2630', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/doc?84732', 'kicadSymbolki_keywords': 'High speed optically coupled gates', 'kicadSymbolki_description': 'Dual High Speed CMOS Compatible Optocoupler, dV/dt 1000/us, VCM 10, max 7V VCC, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : VO2630')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

