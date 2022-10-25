
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "VO615A-8"
    hexID = "SZKISOLATORVO615A8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VO615A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VO615A-8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/81753/vo615a.pdf', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 70V, CTR 130-260% @ 5mA, Viso 5000Vrms, DIP4', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* DIP*W10.16mm* SMDIP*W7.62mm* SMDIP*W9.53mm* SMDIP*W11.48mm*'}])
    newPart['name'].append('Isolator : VO615A-8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

