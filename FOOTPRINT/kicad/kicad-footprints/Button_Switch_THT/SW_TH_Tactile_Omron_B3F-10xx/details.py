
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_TH_Tactile_Omron_B3F-10xx"
    hexID = "FZKBSWTHTACTILEOMRONB3F1XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_TH_Tactile_Omron_B3F-10xx', 'description': 'SW_TH_Tactile_Omron_B3F-10xx_https://www.omron.com/ecb/products/pdf/en-b3f.pdf', 'tags': 'Omron B3F-10xx', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_TH_Tactile_Omron_B3F-10xx.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_TH_Tactile_Omron_B3F-10xx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

