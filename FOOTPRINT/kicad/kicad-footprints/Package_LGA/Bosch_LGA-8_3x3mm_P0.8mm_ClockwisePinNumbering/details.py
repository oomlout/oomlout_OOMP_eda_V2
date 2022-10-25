
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering"
    hexID = "FZKLGABOSCHLGA83X3P8CLWISEPINNUMBERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering', 'description': 'Bosch  LGA, 8 Pin (https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME680-DS001-00.pdf#page=44), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Bosch LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

