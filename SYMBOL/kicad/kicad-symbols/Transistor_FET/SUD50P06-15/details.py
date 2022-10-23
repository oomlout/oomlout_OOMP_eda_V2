
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SUD50P06-15"
    hexID = "SZKTRANSISTORFETSUD5P615"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SUD19P06-60', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SUD50P06-15', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/68940/sud50p06.pdf', 'kicadSymbolki_keywords': 'TrenchFET P-Channel Power MOSFET', 'kicadSymbolki_description': '50A Id, 60V Vds, TrenchFET P-Channel Power MOSFET, 15mOhm Ron, 165nC Qg, -55 to 150 °C, TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('SUD50P06-15')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

