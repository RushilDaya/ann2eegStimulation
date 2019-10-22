import copy
import json

def _getRequiredConfigurations():
    with open("requiredConfigurations.json") as configs:
        requiredConfigurations = json.load(configs)
    return requiredConfigurations

def _allConfigurationsPresent(requiredSet,providedSet):
    # expects two sets as arguments
    if requiredSet == providedSet:
        return True

    missingConfigs = (requiredSet | providedSet ) - providedSet
    if len(missingConfigs)>0:
        print("the following required configs are missing:")
        print(missingConfigs)
        
    extraConfigs = (requiredSet | providedSet ) - requiredSet
    if len(extraConfigs)>0:
        print("the following provided configs are not required:")
        print(extraConfigs)
        
    return False

def _validConfiguration(provided, rules):
    
    if rules["type"] == "str":
        if type(provided) != type(' '):
            print("configuration definition not valid: expected string")
            return False
    
    elif rules["type"] == "int":
        if type(provided) !=type(1):
            print("configuration definition not valid: expected int")
            return False
        
        if 'upperBound' in rules.keys():
            if provided > rules['upperBound']:
                print('configuration definition not valid: exceeds upper bound')
                return False

        if 'lowerBound' in rules.keys():
            if provided < rules.keys():
                print("configuration definition not valid: below lower  bound")
                return False

    elif rules['type'] == 'intArray':
        if type(provided) !=type([]):
            print("configuration definition not valid: expected Array")
            return False

        if 'maxLength' in rules.keys():
            if len(provided) > rules['maxLength']:
                print("configuration definition not valid: array too long")
                return False

        if 'minLength' in rules.keys():
            if len(provided) < rules['minLength']:
                print("configuration definition not valid: array too short")
                return False
        
        tempDictionary = copy.deepcopy(rules)
        tempDictionary["type"] = "int"
        for entry in provided:
            if not _validConfiguration(entry, tempDictionary):
                return False


    return True

def formatConfigFileName(rawName):
    # minor formating on the file name to make it easier to enter
    # on the arglist
    configFileName = rawName.split('/') # ignore full paths
    configFileName = configFileName[-1]
    configFileName = configFileName.split('.')
    configFileName = configFileName[0]
    configFileName = 'configurations/'+configFileName+'.json'
    return configFileName

def configurationValidation(configurations):
    # need to make sure all the correct arguments are present
    # make sure the arguments are meaningful as well
    requiredConfigs = _getRequiredConfigurations()
    requiredConfigNames = set(list(requiredConfigs.keys()))
    argumentNames = set(list(configurations.keys()))

    # 1 - confirm exactly all arguments are present:
    if not _allConfigurationsPresent(requiredConfigNames,argumentNames):
        return False
    
    # 2 - confirm argument types:
    for confKey in requiredConfigNames:
        if not _validConfiguration(configurations[confKey],requiredConfigs[confKey]):
            return False

    return True
