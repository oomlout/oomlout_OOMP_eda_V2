
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Antenna"
    oIndex = "Texas_SWRA416_868MHz_915MHz"
    hexID = "FZKRFTEXASSWRA416868MHZ915MHZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_SWRA416_868MHz_915MHz', 'description': 'http://www.ti.com/lit/an/swra416/swra416.pdf', 'tags': 'PCB antenna', 'attributeType': 'smd', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Antenna : Texas_SWRA416_868MHz_915MHz')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

