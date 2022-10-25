
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Picoflex_90814-0016_2x08_P1.27mm_Vertical"
    hexID = "FZKCNMXMXPICOFLEX9814162X8P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Picoflex_90814-0016_2x08_P1.27mm_Vertical', 'description': 'Molex Picoflex Ribbon-Cable Connectors, 90814-0016, 16 Pins (http://www.molex.com/pdm_docs/sd/908140004_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Picoflex side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Picoflex_90814-0016_2x08_P1.27mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Picoflex_90814-0016_2x08_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

