
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TLE8104E"
    hexID = "SZKPOWERMANAGEMENTTLE814E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'TLE8104E', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-20-30_ThermalVias', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-TLE8104E-DS-v01_04-en.pdf?fileId=db3a304318f3fe2901190401cfda7f25', 'kicadSymbolki_keywords': 'Low_Side_Switch Power', 'kicadSymbolki_description': 'Smart Quad Channel Powertrain Switch 4x3A (In=1A, Ilim=3A, Ron=320mOhm)', 'kicadSymbolki_fp_filters': '*PG?DSO*'}])
    newPart['name'].append('Power_Management : TLE8104E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

