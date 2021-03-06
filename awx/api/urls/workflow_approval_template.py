# Copyright (c) 2017 Ansible, Inc.
# All Rights Reserved.

from django.urls import re_path

from awx.api.views import WorkflowApprovalTemplateDetail, WorkflowApprovalTemplateJobsList


urls = [
    re_path(r'^(?P<pk>[0-9]+)/$', WorkflowApprovalTemplateDetail.as_view(), name='workflow_approval_template_detail'),
    re_path(r'^(?P<pk>[0-9]+)/approvals/$', WorkflowApprovalTemplateJobsList.as_view(), name='workflow_approval_template_jobs_list'),
]

__all__ = ['urls']
