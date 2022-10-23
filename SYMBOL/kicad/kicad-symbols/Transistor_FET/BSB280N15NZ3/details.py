
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSB280N15NZ3"
    hexID = "SZKTRANSISTORFETBSB28N15NZ3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB165N15NZ3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSB280N15NZ3', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MZ', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSB280N15NZ3-DS-v02_05-en.pdf?fileId=db3a30432e779412012e7b0b544c3852', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '30A Id, 150V Vds, 28mOhm Rds, N-Channel MOSFET, DirectFET MZ', 'kicadSymbolki_fp_filters': 'DirectFET*MZ*'}])
    newPart['name'].append('BSB280N15NZ3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

