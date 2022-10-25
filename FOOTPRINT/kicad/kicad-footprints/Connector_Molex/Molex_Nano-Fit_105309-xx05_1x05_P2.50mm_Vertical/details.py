
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Nano-Fit_105309-xx05_1x05_P2.50mm_Vertical"
    hexID = "FZKCNMXMXNANOFIT1539XX51X5P25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Nano-Fit_105309-xx05_1x05_P2.50mm_Vertical', 'description': 'Molex Nano-Fit Power Connectors, 105309-xx05, 5 Pins per row (http://www.molex.com/pdm_docs/sd/1053091203_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Nano-Fit side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Nano-Fit_105309-xx05_1x05_P2.50mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Nano-Fit_105309-xx05_1x05_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

