from setuptools import setup

setup(name='pb_planning',
      version='0.0.0',
      description='',
      url='http://github.com/kylehkhsu/pybullet-planning',
      author='Caelan Garrett',
      license='MIT',
      packages=['pb_planning'],
      zip_safe=False,
      install_requires=['motion_planners @ git+https://github.com/kylehkhsu/motion-planners'],
      package_data={'pb_planning_models': ['models/**/*']}
)