
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_MicroClasp_55935-0630_1x06_P2.00mm_Horizontal"
    hexID = "FZKCNMXMXMCLASP55935631X6P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_MicroClasp_55935-0630_1x06_P2.00mm_Horizontal', 'description': 'Molex MicroClasp Wire-to-Board System, 55935-0630, 6 Pins (http://www.molex.com/pdm_docs/sd/559350530_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex MicroClasp horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_MicroClasp_55935-0630_1x06_P2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_MicroClasp_55935-0630_1x06_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

