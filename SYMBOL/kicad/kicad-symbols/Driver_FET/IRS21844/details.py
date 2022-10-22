
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS21844"
    hexID = "SZKDRIVERFETIRS21844"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR21844', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS21844', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs2184.pdf?fileId=5546d462533600a401535676d8da27db', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Driver, 600V, 1.4/1.8A, PDIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('IRS21844')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

