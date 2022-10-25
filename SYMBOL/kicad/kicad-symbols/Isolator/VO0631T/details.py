
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "VO0631T"
    hexID = "SZKISOLATORVO631T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-063A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VO0631T', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/doc?84607', 'kicadSymbolki_keywords': 'High speed optically coupled gates', 'kicadSymbolki_description': 'Dual High Speed CMOS Compatible Optocoupler, dV/dt 5000/us, VCM 1000, max 7V VCC, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm?P1.27mm*'}])
    newPart['name'].append('Isolator : VO0631T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

