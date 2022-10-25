
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Panelmate_53780-0670_1x06-1MP_P1.25mm_Horizontal"
    hexID = "FZKCNMXMXPANELMATE5378671X61MPP125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Panelmate_53780-0670_1x06-1MP_P1.25mm_Horizontal', 'description': 'Molex Panelmate series connector, 53780-0670 (), generated with kicad-footprint-generator', 'tags': 'connector Molex Panelmate top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Panelmate_53780-0670_1x06-1MP_P1.25mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Panelmate_53780-0670_1x06-1MP_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

