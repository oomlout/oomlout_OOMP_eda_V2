
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_HDMI"
    oIndex = "HDMI_Micro-D_Molex_46765-0x01"
    hexID = "FZKCNHDMIHDMIMDMX46765X1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDMI_Micro-D_Molex_46765-0x01', 'description': 'HDMI, Micro, Type D, SMD, 0.4mm pitch, 19 ckt, right angle (http://www.molex.com/pdm_docs/sd/467651301_sd.pdf)', 'tags': 'hdmi micro type d right angle smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_HDMI.3dshapes/HDMI_Micro-D_Molex_46765-0x01.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_HDMI : HDMI_Micro-D_Molex_46765-0x01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

