# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fcca0d58-487b-4d01-a63d-e515a31ca559",
# META       "default_lakehouse_name": "healthcare1_msft_bronze",
# META       "default_lakehouse_workspace_id": "ff9c80f8-5e5e-4354-8fa6-077467e7d42a"
# META     },
# META     "environment": {
# META       "environmentId": "37b9a6a8-93ee-84e0-4b56-c954f9104a34",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ##### WARNING
# The following notebook is intended to be read only. Please do not modify the contents of this notebook.


# CELL ********************

%run healthcare1_msft_config_notebook

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

%run healthcare1_msft_config_notebook {"enable_spark_setup" : true, "enable_packages_mount" : false}

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# PARAMETERS CELL ********************

inline_params = "{}"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

from microsoft.fabric.hls.hds.services.file_orchestration_service import FileOrchestrationService
import json

# convert inline params into dictionary
inline_params_dict = json.loads(inline_params)

service = FileOrchestrationService(spark, 
                workspace_name=workspace_name,
                solution_name=solution_name,
                admin_lakehouse_name=administration_database_name,
                inline_params=inline_params_dict,
                one_lake_endpoint=one_lake_endpoint)

service.run()

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

mssparkutils.fs.unmount(packages_mount_name)

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }
