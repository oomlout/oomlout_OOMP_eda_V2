
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "NRVA4005T3G"
    hexID = "SZKDIODENRVA45T3G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MRA4003T3G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'NRVA4005T3G', 'kicadSymbolFootprint': 'Diode_SMD:D_SMA', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MRA4003T3-D.PDF', 'kicadSymbolki_keywords': 'AEC-Q101', 'kicadSymbolki_description': '600V, 1A, General Purpose Rectifier Diode, SMA(DO-214AC)', 'kicadSymbolki_fp_filters': 'D*SMA*'}])
    newPart['name'].append('Diode : NRVA4005T3G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

