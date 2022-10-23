
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS5200-1EJA"
    hexID = "SZKPOWERMANAGEMENTBTS521EJA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS40K2-1EJC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS5200-1EJA', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-8-43', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BTS5200-1EJA-DS-v01_00-EN.pdf?fileId=5546d46250cc1fdf0151636cd945402e', 'kicadSymbolki_keywords': 'infineon power switch', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 200mOhm, 1.5A, 28V, DSO-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*DSO*43*'}])
    newPart['name'].append('BTS5200-1EJA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

