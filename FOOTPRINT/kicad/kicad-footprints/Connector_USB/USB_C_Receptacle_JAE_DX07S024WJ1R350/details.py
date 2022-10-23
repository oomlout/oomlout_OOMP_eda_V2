
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_C_Receptacle_JAE_DX07S024WJ1R350"
    hexID = "FZKCNUUCRECEPTACLEJAEDX7S24WJ1R35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_C_Receptacle_JAE_DX07S024WJ1R350', 'description': 'http://www.jae.com/z-en/pdf_download_exec.cfm?param=SJ117219.pdf', 'tags': 'USB C Type-C Receptacle SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_JAE_DX07S024WJ1R350.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Connector_USB : USB_C_Receptacle_JAE_DX07S024WJ1R350')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

