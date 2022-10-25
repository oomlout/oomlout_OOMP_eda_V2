
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "NHD-0420H1Z"
    hexID = "FZKDINHD42H1Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'NHD-0420H1Z', 'description': 'NHD-0420H1Z LCD http://www.newhavendisplay.com/specs/NHD-0420H1Z-FSW-GBW-33V3.pdf', 'tags': 'NHD-0420H1Z LCD', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/NHD-0420H1Z.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Display : NHD-0420H1Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

