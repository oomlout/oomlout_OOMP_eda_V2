
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "EE2-5NU"
    hexID = "SZKRELAYEE25NU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EE2-3NU', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'EE2-5NU', 'kicadSymbolFootprint': 'Relay_SMD:Relay_DPDT_Kemet_EE2_NU', 'kicadSymbolDatasheet': 'https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'kicadSymbolki_keywords': 'signal relay double pole double throw DPDT DC coil non latching', 'kicadSymbolki_description': 'General purpose signal relay, Kemet EE2 Series, DPDT (2 Form C), non-latching, SMD, 60W/125VA, 220VDC/250VAC, 2A, 5V DC coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Kemet*EE2*NU*'}])
    newPart['name'].append('Relay : EE2-5NU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

