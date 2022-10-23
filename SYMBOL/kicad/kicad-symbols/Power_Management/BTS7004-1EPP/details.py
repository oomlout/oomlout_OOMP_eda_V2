
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS7004-1EPP"
    hexID = "SZKPOWERMANAGEMENTBTS741EPP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS7004-1EPP', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-TSDSO-14-22', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BTS7004-1EPP-DS-v01_00-EN.pdf?fileId=5546d4626102d35a016147550a725555', 'kicadSymbolki_keywords': 'BTS7004', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, One Channel, 12V, 15A, Rds(on) 4.4mΩ, PG-TSDSO-14-22', 'kicadSymbolki_fp_filters': 'Infineon*TSDSO*22*'}])
    newPart['name'].append('BTS7004-1EPP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

