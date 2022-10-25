
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_PicoBlade_53048-0510_1x05_P1.25mm_Horizontal"
    hexID = "FZKCNMXMXPICOBLADE5348511X5P125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_PicoBlade_53048-0510_1x05_P1.25mm_Horizontal', 'description': 'Molex PicoBlade Connector System, 53048-0510, 5 Pins per row (http://www.molex.com/pdm_docs/sd/530480210_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex PicoBlade top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_PicoBlade_53048-0510_1x05_P1.25mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_PicoBlade_53048-0510_1x05_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

