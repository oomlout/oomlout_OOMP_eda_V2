
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMP3013SFV"
    hexID = "SZKTRANSISTORFETDMP313SFV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMP3013SFV', 'kicadSymbolFootprint': 'Package_SON:Diodes_PowerDI3333-8', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/DMP3013SFV.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-12A Id, -30V Vds, P-Channel Power MOSFET, 9.5mOhm Ron, 33.7nC Qg (typ), PowerDI3333-8', 'kicadSymbolki_fp_filters': 'Diodes*PowerDI3333*'}])
    newPart['name'].append('Transistor_FET : DMP3013SFV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

