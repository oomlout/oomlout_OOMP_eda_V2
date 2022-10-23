
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_B_Amphenol_MUSB-D511_Vertical_Rugged"
    hexID = "FZKCNUUBAMPHENOLMUD511VERTICALRUGGED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_B_Amphenol_MUSB-D511_Vertical_Rugged', 'description': 'A,phenol MUSB_D511, USB B female connector, straight, rugged, https://www.amphenolcanada.com/ProductSearch/drawings/AC/MUSBD511XX.pdf', 'tags': 'USB_B_MUSB_Straight female connector straight rugged MUSB D511', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_B_Amphenol_MUSB-D511_Vertical_Rugged.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_B_Amphenol_MUSB-D511_Vertical_Rugged')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

