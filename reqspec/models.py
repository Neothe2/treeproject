from django.db import models

from mytree.models import Tree, TreeNode


class UseCaseDescription(models.Model):
    main_flow = models.OneToOneField('MainFlow', related_name='use_case_description', on_delete=models.SET_NULL, null=True, blank=True)
    pass


class MainFlow(Tree):
    # use_case_description = models.OneToOneField(
    #     UseCaseDescription,
    #     on_delete=models.CASCADE,
    #     related_name='main_flow',
    #     null=True,
    #     blank=True
    # )
    pass


class AlternateFlow(Tree):
    use_case_description = models.ForeignKey(UseCaseDescription, on_delete=models.CASCADE,
                                             related_name='alternate_flows', null=True, blank=True)


class ExceptionFlow(Tree):
    use_case_description = models.ForeignKey(UseCaseDescription, on_delete=models.CASCADE,
                                             related_name='exception_flows', null=True, blank=True)


class MainFlowStep(TreeNode):
    pass


class AlternateFlowStep(TreeNode):
    pass


class ExceptionFlowStep(TreeNode):
    pass
