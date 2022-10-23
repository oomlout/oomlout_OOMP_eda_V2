
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_C_Receptacle_Amphenol_12401548E4-2A_CircularHoles"
    hexID = "FZKCNUUCRECEPTACLEAMPHENOL1241548E42ACIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_C_Receptacle_Amphenol_12401548E4-2A_CircularHoles', 'description': 'USB TYPE C, RA RCPT PCB, Hybrid, https://www.amphenolcanada.com/StockAvailabilityPrice.aspx?From=&PartNum=12401548E4%7e2A', 'tags': 'USB C Type-C Receptacle Hybrid', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_C_Receptacle_Amphenol_12401548E4-2A.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB_C_Receptacle_Amphenol_12401548E4-2A_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

