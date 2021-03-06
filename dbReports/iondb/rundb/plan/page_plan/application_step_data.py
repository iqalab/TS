# Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved
'''
Created on May 21, 2013

@author: ionadmin
'''
import logging

from iondb.rundb.plan.page_plan.abstract_step_data import AbstractStepData
from iondb.rundb.models import RunType, ApplProduct, ApplicationGroup
from iondb.rundb.plan.page_plan.step_names import StepNames


logger = logging.getLogger(__name__)


class ApplicationFieldNames():

    APPL_PRODUCT = 'applProduct'
    RUN_TYPE = 'runType'
    APPLICATION_GROUP = 'applicationGroup'
    APPLICATION_GROUP_NAME = "applicationGroupName"
    SAMPLE_GROUPING = 'sampleGrouping'
    RUN_TYPES = 'runTypes'
    APPLICATION_GROUPS = 'applicationGroups'
    SAMPLE_GROUPINGS = 'sampleGroupings'
    COLUMNS = 'columns'
    NAME = 'Name'
    RELATIONSHIP_TYPE = 'RelationshipType'
    VALUES = 'Values'
    PLAN_STATUS = "planStatus"
    UPDATE_KITS_DEFAULTS = 'updateKitsDefaults'
    CATEGORIES = "categories"
    
class ApplicationStepData(AbstractStepData):

    def __init__(self, sh_type):
        super(ApplicationStepData, self).__init__(sh_type)
        self.resourcePath = 'rundb/plan/page_plan/page_plan_application.html'

        # self._dependsOn = [StepNames.IONREPORTER]
        
        self.savedFields[ApplicationFieldNames.RUN_TYPE] = None
        self.savedFields[ApplicationFieldNames.APPLICATION_GROUP] = None
        self.savedFields[ApplicationFieldNames.SAMPLE_GROUPING] = None
        self.prepopulatedFields[ApplicationFieldNames.PLAN_STATUS] = ""
        
        self.savedObjects[ApplicationFieldNames.RUN_TYPE] = None
        self.savedObjects[ApplicationFieldNames.APPL_PRODUCT] = None
        self.savedObjects[ApplicationFieldNames.UPDATE_KITS_DEFAULTS] = True
        self.prepopulatedFields[ApplicationFieldNames.RUN_TYPES] = list(RunType.objects.all().order_by('nucleotideType', 'runType'))

        self.prepopulatedFields[ApplicationFieldNames.APPLICATION_GROUP_NAME] = None  
        self.prepopulatedFields[ApplicationFieldNames.CATEGORIES] = ''

#        isSupported = isOCP_enabled()
#        if isSupported:
#            self.prepopulatedFields[ApplicationFieldNames.APPLICATION_GROUPS] = ApplicationGroup.objects.filter(isActive=True).order_by('uid')
#        else:
#            self.prepopulatedFields[ApplicationFieldNames.APPLICATION_GROUPS] = ApplicationGroup.objects.filter(isActive=True).exclude(name = "DNA + RNA").order_by('uid')

        self.prepopulatedFields[ApplicationFieldNames.APPLICATION_GROUPS] = ApplicationGroup.objects.filter(isActive=True).order_by('uid')
                                                                                                                                                             
        # self.prepopulatedFields[ApplicationFieldNames.SAMPLE_GROUPINGS] = SampleGroupType_CV.objects.filter(isActive=True).order_by('uid')
        # self._dependsOn = [StepNames.EXPORT]

        self.sh_type = sh_type

    def getStepName(self):
        return StepNames.APPLICATION

    def updateSavedObjectsFromSavedFields(self):      
        #logger.debug("ENTER application_step_data.updateSavedObjectsFromSavedFields() self.savedFields=%s" %(self.savedFields))
        previous_run_type = self.savedObjects[ApplicationFieldNames.RUN_TYPE]
        
        if self.savedFields[ApplicationFieldNames.RUN_TYPE]:
            self.savedObjects[ApplicationFieldNames.RUN_TYPE] = RunType.objects.get(pk=self.savedFields[ApplicationFieldNames.RUN_TYPE])
            self.savedObjects[ApplicationFieldNames.APPL_PRODUCT] = ApplProduct.objects.get(isActive=True, isDefault=True, isVisible=True,
                                                                       applType__runType=self.savedObjects[ApplicationFieldNames.RUN_TYPE].runType)
        else:
            self.savedObjects[ApplicationFieldNames.RUN_TYPE] = None
            self.savedObjects[ApplicationFieldNames.APPL_PRODUCT] = None
        
        self.savedObjects[ApplicationFieldNames.UPDATE_KITS_DEFAULTS] = previous_run_type != self.savedObjects[ApplicationFieldNames.RUN_TYPE]
                        
    def updateFromStep(self, step_depended_on):
        pass
    #     if step_depended_on.getStepName() != StepNames.EXPORT:
    #         return
        # ir_sample_groupings = None
        # if step_depended_on.savedFields[ExportFieldNames.IR_OPTIONS] == ExportFieldNames.IR_VERSION_40:
        #     ir_qs = Plugin.objects.filter(name__icontains='IonReporter')
        #     irExists = ir_qs.count() > 0
        #     if irExists and ir_qs[0:1][0].userinputfields and ApplicationFieldNames.COLUMNS in ir_qs[0:1][0].userinputfields:
        #         configJson = ir_qs[0:1][0].userinputfields
        #         for column in configJson[ApplicationFieldNames.COLUMNS]:
        #             if column[ApplicationFieldNames.NAME] == ApplicationFieldNames.RELATIONSHIP_TYPE:
        #                 ir_sample_groupings = column[ApplicationFieldNames.VALUES]
        #                 break

        # if ir_sample_groupings:
        #     self.prepopulatedFields[ApplicationFieldNames.SAMPLE_GROUPINGS] = \
        #         SampleGroupType_CV.objects.filter(isActive=True, iRValue__in=ir_sample_groupings).order_by('uid')
        # else:
        #     self.prepopulatedFields[ApplicationFieldNames.SAMPLE_GROUPINGS] = SampleGroupType_CV.objects.filter(isActive=True).order_by('uid')

    def validateField(self, field_name, new_field_value):
        self.validationErrors.pop(field_name, None)
        
        if field_name == ApplicationFieldNames.RUN_TYPE:
            if not new_field_value:
                self.validationErrors[field_name] = 'Please select Target Technique'
