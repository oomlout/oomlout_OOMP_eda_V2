
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Samtec_ASP-134602-01"
    hexID = "SZKCNSAMTECASP134621"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Samtec_ASP-134602-01', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://suddendocs.samtec.com/prints/asp-134602-01-mkt.pdf', 'kicadSymbolki_keywords': 'FPGA Mezzanine Card FMC Terminal Connector Header', 'kicadSymbolki_description': 'Connector array, 10x40, 1.27mm pitch, male pins, gold finish, VITA 57.1 FMC, SMD', 'kicadSymbolki_fp_filters': '*FMC*ASP*134602?01*10x40*P1.27mm* *FMC*ASP*134486?01*10x40*P1.27mm*'}])
    newPart['name'].append('Samtec_ASP-134602-01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

