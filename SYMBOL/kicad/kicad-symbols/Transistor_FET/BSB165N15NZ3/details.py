
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSB165N15NZ3"
    hexID = "SZKTRANSISTORFETBSB165N15NZ3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSB165N15NZ3', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MZ', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSB165N15NZ3-DS-v02_02-en.pdf?fileId=db3a30432e779412012e7b04a1353843', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '45A Id, 150V Vds, 16.5mOhm Rds, N-Channel MOSFET, DirectFET MZ', 'kicadSymbolki_fp_filters': 'DirectFET*MZ*'}])
    newPart['name'].append('Transistor_FET : BSB165N15NZ3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

