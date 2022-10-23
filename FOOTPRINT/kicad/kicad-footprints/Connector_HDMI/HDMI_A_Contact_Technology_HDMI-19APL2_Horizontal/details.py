
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_HDMI"
    oIndex = "HDMI_A_Contact_Technology_HDMI-19APL2_Horizontal"
    hexID = "FZKCNHDMIHDMIACONTACTTECHNOLOGYHDMI19APL2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDMI_A_Contact_Technology_HDMI-19APL2_Horizontal', 'description': 'HDMI Contact Technology Type A http://www.contactswitch.com/en/download.aspx?id=1449', 'tags': 'HDMI Contact Technology Type A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_HDMI.3dshapes/HDMI_A_Contact_Technology_HDMI-19APL2_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_HDMI : HDMI_A_Contact_Technology_HDMI-19APL2_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

