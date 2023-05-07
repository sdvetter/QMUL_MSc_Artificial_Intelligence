Simon Dreyer Vetter
To run the package:

1. Unzip the folder cr_week6_test in your catkin workspace in /src folder
2. Configure ROS environment by running source devel/setup.bash in root workspace directory
3. Build your workspace i.e. run catkin_make
4. Run launch file by executing roslaunch cr_week6_test 
   human_robot_interaction.launch
5. To view active nodes, run rqt_graph 
6. To view following four topics run rostopic echo \object_info_gen,
   \human_info_gen, \perceived_info or \robot_info_likelihoods