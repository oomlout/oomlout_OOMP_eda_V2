
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_MicroClasp_55932-1430_1x14_P2.00mm_Vertical"
    hexID = "FZKCNMXMXMCLASP559321431X14P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_MicroClasp_55932-1430_1x14_P2.00mm_Vertical', 'description': 'Molex MicroClasp Wire-to-Board System, 55932-1430, 14 Pins (http://www.molex.com/pdm_docs/sd/559320530_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex MicroClasp side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_MicroClasp_55932-1430_1x14_P2.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_MicroClasp_55932-1430_1x14_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

