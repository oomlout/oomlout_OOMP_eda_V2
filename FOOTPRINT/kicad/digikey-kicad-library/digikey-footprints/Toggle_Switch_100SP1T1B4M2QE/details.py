
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Toggle_Switch_100SP1T1B4M2QE"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSTOGGLESWITCH1SP1T1B4M2QE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Toggle_Switch_100SP1T1B4M2QE', 'description': 'http://spec_sheets.e-switch.com/specs/T111597.pdf', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : Toggle_Switch_100SP1T1B4M2QE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

