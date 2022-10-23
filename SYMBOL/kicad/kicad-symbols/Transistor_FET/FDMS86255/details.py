
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMS86255"
    hexID = "SZKTRANSISTORFETFDMS86255"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMS86255', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMS86255-D.pdf', 'kicadSymbolki_keywords': 'shielded-gate-powertrench-MOSFET MOSFET fairchild', 'kicadSymbolki_description': '10A Id, 150V Vds, N-Channel Shielded Gate PowerTrench MOSFET, 12.4mOhm Ron, 63nC Qgmax, -55 to 150 °C, 5x6mm SON8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('FDMS86255')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

