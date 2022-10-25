
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Micro-AB_Molex_47590-0001"
    hexID = "FZKCNUUMABMX47591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro-AB_Molex_47590-0001', 'description': 'Micro USB AB receptable, right-angle inverted (https://www.molex.com/pdm_docs/sd/475900001_sd.pdf)', 'tags': 'Micro AB USB SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Micro-AB_Molex_47590-0001.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_Micro-AB_Molex_47590-0001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

