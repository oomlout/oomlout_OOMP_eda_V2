
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "ITS5215"
    hexID = "SZKPOWERMANAGEMENTITS5215"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'ITS5215', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-12-9_ThermalVias', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-ITS5215L-DS-v01_01-en.pdf?fileId=db3a304412b407950112b428dba73e98', 'kicadSymbolki_keywords': 'High_Side_Switch Power', 'kicadSymbolki_description': 'Smart Dual Channel High Side Powertrain Switch (90mOhm)', 'kicadSymbolki_fp_filters': '*PG?DSO*'}])
    newPart['name'].append('Power_Management : ITS5215')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

