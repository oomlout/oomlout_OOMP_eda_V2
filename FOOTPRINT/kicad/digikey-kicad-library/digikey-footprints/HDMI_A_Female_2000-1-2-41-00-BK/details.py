
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "HDMI_A_Female_2000-1-2-41-00-BK"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSHDMIAFEMALE21241BK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDMI_A_Female_2000-1-2-41-00-BK', 'description': 'http://media.digikey.com/pdf/Data%20Sheets/CNC%20Tech%20PDFs/HDMI_A_Female_2000-1-2-41-00-BK_Dwg.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : HDMI_A_Female_2000-1-2-41-00-BK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

