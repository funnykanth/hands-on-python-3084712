import os
DEV = 'development'
STG = 'stage'
TEST = 'test'
CODESPACE = 'code space'
LOCAL = 'Local'

current_env = os.environ.get('ENV_NAME',DEV)

if current_env == DEV:
  print (DEV)
elif current_env == TEST:
  print(TEST)
elif current_env == STG:
  print (STG)
elif current_env in [CODESPACE, LOCAL]:
  print ('LOCAL DEV ENV')
else:
  print ('unknown')