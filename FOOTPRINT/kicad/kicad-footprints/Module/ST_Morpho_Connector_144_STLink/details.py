
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "ST_Morpho_Connector_144_STLink"
    hexID = "FZKMOSTMORPHOCN144STLINK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_Morpho_Connector_144_STLink', 'description': 'ST Morpho Connector 144 With STLink', 'tags': 'ST Morpho Connector 144 STLink', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/ST_Morpho_Connector_144_STLink.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Module : ST_Morpho_Connector_144_STLink')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

