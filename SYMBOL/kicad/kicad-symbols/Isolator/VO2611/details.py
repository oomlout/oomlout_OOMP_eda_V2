
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "VO2611"
    hexID = "SZKISOLATORVO2611"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-261A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VO2611', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/doc?84732', 'kicadSymbolki_keywords': 'High speed optically coupled gates enable', 'kicadSymbolki_description': 'Single High Speed CMOS Compatible Optocoupler with enable, dV/dt 15000/us, VCM 1000, max 7V VCC, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : VO2611')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

