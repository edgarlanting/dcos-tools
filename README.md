# dcos-tools
A selection of scripts to help troubleshoot DC/OS issues.

**dcos-fix-fbs.py**

This script fixes broken deployments of applications using file based secrets up until release 1.10.3 that have broken when
updating the apps.
By running a group update PUT against the API it basically redeploys all current broken apps on the cluster to get them
back in a healthy state.
