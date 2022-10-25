
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "ERM19264"
    hexID = "FZKDIERM19264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ERM19264', 'description': 'STN/FSTN LCD 192x64 dot https://www.buydisplay.com/download/manual/ERM19264-1_Series_Datasheet.pdf', 'tags': 'ERM19264 Graphics Display 192x64', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/ERM19264.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Display : ERM19264')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

