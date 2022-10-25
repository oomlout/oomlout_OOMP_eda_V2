
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_Keyboard"
    oIndex = "SW_Matias_1.50u"
    hexID = "FZKBSWMATIAS15U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Matias_1.50u', 'description': 'Matias/ALPS keyswitch, 1.50u, http://matias.ca/switches/', 'tags': 'Matias ALPS keyswitch 1.50u', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_Keyboard.3dshapes/SW_Matias_1.50u.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_Keyboard : SW_Matias_1.50u')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

