
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_HDMI"
    oIndex = "HDMI_A_Kycon_KDMIX-SL1-NS-WS-B15_VerticalRightAngle"
    hexID = "FZKCNHDMIHDMIAKYCONKDMIXSL1NSWSB15VERTICALRIGHTANGLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDMI_A_Kycon_KDMIX-SL1-NS-WS-B15_VerticalRightAngle', 'description': 'HDMI, Type A, Kycon KDMIX-SL1-NS-WS-B15, Vertical Right Angle, http://www.kycon.com/Pub_Eng_Draw/KDMIX-SL1-NS-WS-B15.pdf', 'tags': 'hdmi type a', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_HDMI.3dshapes/HDMI_A_Kycon_KDMIX-SL1-NS-WS-B15_VerticalRightAngle.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_HDMI : HDMI_A_Kycon_KDMIX-SL1-NS-WS-B15_VerticalRightAngle')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

