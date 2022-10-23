
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_PicoBlade_53047-0810_1x08_P1.25mm_Vertical"
    hexID = "FZKCNMXMXPICOBLADE5347811X8P125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_PicoBlade_53047-0810_1x08_P1.25mm_Vertical', 'description': 'Molex PicoBlade Connector System, 53047-0810, 8 Pins per row (http://www.molex.com/pdm_docs/sd/530470610_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex PicoBlade side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_PicoBlade_53047-0810_1x08_P1.25mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_PicoBlade_53047-0810_1x08_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

