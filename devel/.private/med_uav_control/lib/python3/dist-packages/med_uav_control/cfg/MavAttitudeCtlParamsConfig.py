## *********************************************************
##
## File autogenerated for the urs_solution package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'roll_kp', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Roll ctl PID P gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'roll_ki', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Roll ctl PID I gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'roll_kd', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Roll ctl PID D gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'roll_r_kp', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Roll rate ctl PID P gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'roll_r_ki', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Roll rate ctl PID I gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'roll_r_kd', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Roll rate ctl PID D gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pitch_kp', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Pitch ctl PID P gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pitch_ki', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Pitch ctl PID I gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pitch_kd', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Pitch ctl PID D gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pitch_r_kp', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Pitch rate ctl PID P gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pitch_r_ki', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Pitch rate ctl PID I gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pitch_r_kd', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Pitch rate ctl PID D gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_kp', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Yaw ctl PID P gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_ki', 'type': 'double', 'default': 0.001, 'level': 0, 'description': 'Yaw ctl PID I gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_kd', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Yaw ctl PID D gain', 'min': 0.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_r_kp', 'type': 'double', 'default': 200.0, 'level': 0, 'description': 'Yaw rate ctl PID P gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_r_ki', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Yaw rate ctl PID I gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_r_kd', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Yaw rate ctl PID D gain', 'min': 0.0, 'max': 1000.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

