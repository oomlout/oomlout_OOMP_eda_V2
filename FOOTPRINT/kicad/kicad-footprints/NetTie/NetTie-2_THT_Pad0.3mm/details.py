
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "NetTie"
    oIndex = "NetTie-2_THT_Pad0.3mm"
    hexID = "FZKNTNT2THTPAD3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'NetTie-2_THT_Pad0.3mm', 'description': 'Net tie, 2 pin, 0.3mm round THT pads', 'tags': 'net tie', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('NetTie : NetTie-2_THT_Pad0.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

