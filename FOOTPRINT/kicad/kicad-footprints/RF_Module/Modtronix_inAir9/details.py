
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "Modtronix_inAir9"
    hexID = "FZKRFMOMODTRONIXINAIR9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Modtronix_inAir9', 'description': 'Modtronix Wireless SX1276 LoRa Module (http://modtronix.com/img/prod/imod/inair9/inair_dimensions.gif)', 'tags': 'Modtronix LoRa inAir inAir9 SX1276 RF 915MHz 868MHz Wireless', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/Modtronix_inAir9.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : Modtronix_inAir9')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

