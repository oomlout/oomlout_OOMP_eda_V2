
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TLE8102SG"
    hexID = "SZKPOWERMANAGEMENTTLE812SG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'TLE8102SG', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-12-11_ThermalVias', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-TLE8102SG-DS-v01_05-en.pdf?fileId=db3a304319c6f18c0119c8384bf90042', 'kicadSymbolki_keywords': 'Low_Side_Switch Power', 'kicadSymbolki_description': 'Smart Dual Channel Powertrain Switch 2x8A (max 360mOhm)', 'kicadSymbolki_fp_filters': '*PG?DSO*'}])
    newPart['name'].append('Power_Management : TLE8102SG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

