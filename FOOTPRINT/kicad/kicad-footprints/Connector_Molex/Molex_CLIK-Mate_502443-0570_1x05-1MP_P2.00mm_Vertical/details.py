
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_CLIK-Mate_502443-0570_1x05-1MP_P2.00mm_Vertical"
    hexID = "FZKCNMXMXCLIKMATE52443571X51MPP2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_CLIK-Mate_502443-0570_1x05-1MP_P2.00mm_Vertical', 'description': 'Molex CLIK-Mate series connector, 502443-0570 (http://www.molex.com/pdm_docs/sd/5024430270_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex CLIK-Mate side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_CLIK-Mate_502443-0570_1x05-1MP_P2.00mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_CLIK-Mate_502443-0570_1x05-1MP_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

