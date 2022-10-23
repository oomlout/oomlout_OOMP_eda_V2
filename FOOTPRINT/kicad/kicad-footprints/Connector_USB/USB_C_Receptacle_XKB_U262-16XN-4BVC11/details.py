
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_C_Receptacle_XKB_U262-16XN-4BVC11"
    hexID = "FZKCNUUCRECEPTACLEXKBU26216XN4BVC11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_C_Receptacle_XKB_U262-16XN-4BVC11', 'description': 'USB Type C, right-angle, SMT, https://datasheet.lcsc.com/szlcsc/1811141824_XKB-Enterprise-U262-161N-4BVC11_C319148.pdf', 'tags': 'USB C Type-C Receptacle SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_XKB_U262-16XN-4BVC11.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB_C_Receptacle_XKB_U262-16XN-4BVC11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

