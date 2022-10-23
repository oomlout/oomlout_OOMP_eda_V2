
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_HDMI"
    oIndex = "HDMI_A_Molex_208658-1001_Horizontal"
    hexID = "FZKCNHDMIHDMIAMX2865811HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDMI_A_Molex_208658-1001_Horizontal', 'description': 'HDMI Molex Type A https://www.molex.com/pdm_docs/sd/2086581001_sd.pdf', 'tags': 'HDMI Molex Type A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_HDMI.3dshapes/HDMI_A_Molex_208658-1001_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_HDMI : HDMI_A_Molex_208658-1001_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

