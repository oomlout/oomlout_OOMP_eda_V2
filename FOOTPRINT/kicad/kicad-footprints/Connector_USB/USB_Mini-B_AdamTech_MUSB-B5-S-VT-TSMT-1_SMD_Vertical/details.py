
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Mini-B_AdamTech_MUSB-B5-S-VT-TSMT-1_SMD_Vertical"
    hexID = "FZKCNUUMBADAMTECHMUB5SVTTSMT1SMVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Mini-B_AdamTech_MUSB-B5-S-VT-TSMT-1_SMD_Vertical', 'description': 'http://www.adam-tech.com/upload/MUSB-B5-S-VT-TSMT-1.pdf', 'tags': 'USB Mini-B', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Mini-B_AdamTech_MUSB-B5-S-VT-TSMT-1_SMD_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB_Mini-B_AdamTech_MUSB-B5-S-VT-TSMT-1_SMD_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

