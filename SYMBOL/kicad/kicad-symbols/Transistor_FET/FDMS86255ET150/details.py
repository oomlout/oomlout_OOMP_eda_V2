
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMS86255ET150"
    hexID = "SZKTRANSISTORFETFDMS86255ET15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMS86255ET150', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMS86255ET150-D.pdf', 'kicadSymbolki_keywords': 'shielded-gate-powertrench MOSFET fairchild', 'kicadSymbolki_description': '10A Id, 150V Vds, N-Channel Shielded Gate PowerTrench MOSFET, 12.4mOhm Ron, 63nC Qgmax, -55 to 175 °C, 5x6mm SON8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : FDMS86255ET150')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

