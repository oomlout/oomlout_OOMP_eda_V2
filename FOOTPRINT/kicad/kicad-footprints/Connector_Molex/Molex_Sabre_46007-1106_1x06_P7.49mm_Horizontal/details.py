
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Sabre_46007-1106_1x06_P7.49mm_Horizontal"
    hexID = "FZKCNMXMXSABRE4671161X6P749HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Sabre_46007-1106_1x06_P7.49mm_Horizontal', 'description': 'Molex Sabre Power Connector, 46007-1106, 6 Pins per row (http://www.molex.com/pdm_docs/sd/460071105_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Sabre top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Sabre_46007-1106_1x06_P7.49mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Molex : Molex_Sabre_46007-1106_1x06_P7.49mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

