
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_CLIK-Mate_502382-1070_1x10-1MP_P1.25mm_Vertical"
    hexID = "FZKCNMXMXCLIKMATE52382171X11MPP125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_CLIK-Mate_502382-1070_1x10-1MP_P1.25mm_Vertical', 'description': 'Molex CLIK-Mate series connector, 502382-1070 (http://www.molex.com/pdm_docs/sd/5023820270_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex CLIK-Mate side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_CLIK-Mate_502382-1070_1x10-1MP_P1.25mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_CLIK-Mate_502382-1070_1x10-1MP_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

