
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BTS5012SDA"
    hexID = "SZKPOWERMANAGEMENTBTS512SDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BTS50080-1TEA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTS5012SDA', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BTS5012SDA-DS-v01_01-en.pdf?fileId=db3a30431d8a6b3c011db95c6eba237d', 'kicadSymbolki_keywords': 'infineon power switch', 'kicadSymbolki_description': 'Smart High-Side Power Switch, PROFET, Single, 24mOhm, 6.5A, 20V, TO252-5', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Power_Management : BTS5012SDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

