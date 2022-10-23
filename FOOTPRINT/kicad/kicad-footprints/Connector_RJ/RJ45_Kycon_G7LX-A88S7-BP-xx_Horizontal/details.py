
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Kycon_G7LX-A88S7-BP-xx_Horizontal"
    hexID = "FZKCNRJRJ45KYCONG7LXA88S7BPXXHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Kycon_G7LX-A88S7-BP-xx_Horizontal', 'description': '10/100Base-T RJ45 ethernet magnetic transformer connector horizontal with green/yellow LEDs http://www.kycon.com/Pub_Eng_Draw/G7LX-A88S7-BP-GY.pdf', 'tags': 'RJ45 ethernet magnetic', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Kycon_G7LX-A88S7-BP-xx_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Kycon_G7LX-A88S7-BP-xx_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

