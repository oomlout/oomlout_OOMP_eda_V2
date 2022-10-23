
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "BNC_TEConnectivity_1478035_Horizontal"
    hexID = "FZKCNCOABNCTECONNECTIVITY147835HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BNC_TEConnectivity_1478035_Horizontal', 'description': 'BNC RF Interface, PCB mount 4 pin, Right Angle, Bayonet, 50Ohm, 4GHz, https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F1478035%7FB1%7Fpdf%7FEnglish%7FENG_CD_1478035_B1.pdf%7F1-1478035-0', 'tags': 'BNC RF interface bayonet 50ohm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/BNC_TEConnectivity_1478035_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : BNC_TEConnectivity_1478035_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

