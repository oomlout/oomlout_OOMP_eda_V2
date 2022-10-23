
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_C_Receptacle_HRO_TYPE-C-31-M-12"
    hexID = "FZKCNUUCRECEPTACLEHROTYPEC31M12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_C_Receptacle_HRO_TYPE-C-31-M-12', 'description': 'USB Type-C receptacle for USB 2.0 and PD, http://www.krhro.com/uploads/soft/180320/1-1P320120243.pdf', 'tags': 'usb usb-c 2.0 pd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_HRO_TYPE-C-31-M-12.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB_C_Receptacle_HRO_TYPE-C-31-M-12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

