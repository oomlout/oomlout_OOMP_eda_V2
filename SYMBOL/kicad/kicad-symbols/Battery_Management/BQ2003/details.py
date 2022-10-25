
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ2003"
    hexID = "SZKBATMANAGEMENTBQ23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ2003', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq2003.pdf', 'kicadSymbolki_keywords': 'battery nickel cadmium metal hydride', 'kicadSymbolki_description': 'Standalone switchmode NiCd/NiMH battery charger, 2-4 cells, negative dV and dT/dt termination', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Battery_Management : BQ2003')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

