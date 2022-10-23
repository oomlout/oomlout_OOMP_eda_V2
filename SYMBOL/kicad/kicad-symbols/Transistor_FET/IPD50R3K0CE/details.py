
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IPD50R3K0CE"
    hexID = "SZKTRANSISTORFETIPD5R3KCE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IPD50R380CE', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPD50R3K0CE', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/IPx50R3K0CE_2_0.pdf?folderId=db3a3043163797a6011637d4bae7003b&fileId=db3a304339dcf4b10139e7e9ff592ce4', 'kicadSymbolki_keywords': 'CoolMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '1.7A Id, 500V Vds, CoolMOS N-Channel Power MOSFET, 3Ohm Ron, 4.3nC Qg (typ), TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('IPD50R3K0CE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

