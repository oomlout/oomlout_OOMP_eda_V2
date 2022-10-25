
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "USB_Micro_A_3.1_Female_GSB443T33HR"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUMA31FEMALEGSB443T33HR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro_A_3.1_Female_GSB443T33HR', 'description': 'http://media.digikey.com/pdf/Data%20Sheets/Amphenol%20PDFs/USB_Micro_A_3.1_Female_GSB443T33HR_Dwg.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : USB_Micro_A_3.1_Female_GSB443T33HR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

