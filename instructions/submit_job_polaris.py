# Step 1: SSH into Polaris
ssh -KY azam@polaris.alcf.anl.gov

# Password: (8-digit code from MobilePass application)

# Step 2: Submit an Interactive Job to a Compute Node
qsub -I -l select=1 -l walltime=01:00:00 -A Nu_Novel -l filesystems=eagle -q debug
# qsub -I -l select=10 -l walltime=03:00:00 -A Nu_Novel -l filesystems=eagle -q prod

# Step 3: Change the directory
cd spine_bilal/

# Step 4: Load Necessary Modules
module use /soft/spack/gcc/0.6.1/install/modulefiles/Core
module load apptainer

# Step 5: (See Appendix 1 before this step) Run the training using the specified configuration file in Apptainer (change path accordingly)
# GRAPPA_SHOWER.CFG (training)
apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/spine_workshop_2024/basics/training/grappa_shower.cfg

# URESNET.CFG (training)
apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/spine_workshop_2024/basics/training/uresnet.cfg

# PRODUCTION
apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/spine_prod/config/2x2/2x2_full_chain_240719.cfg


######################

# To open ROOT in Apptainer
apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif /bin/bash

# See file size
du -ah /home/azam/spine_bilal/small_2x2_output.h5
######################

# Appendix 1
## MAKE FOLLOWING CHANGES IN CONFIGURATION FILES ##
1. In uresnet.cfg, set
		file_keys: /your/path/to/generic_small.root
	in my case, it is: 
		file_keys: /mnt/eagle/clone/g2/projects/Nu_Novel/Tutorials/spine_workshop_2024/data_samples/Small_LArCV_files/generic_small.root
																					
2. Set batch_size to 6 for this "generic_small.root" file. It is 128 by default.


## You can make these changes to uresnet.cfg file using the following command line prompt as well. For example:
sed -i 's/batch_size: 6/batch_size: 128/' /home/azam/spine_bilal/spine_workshop_2024/basics/training/uresnet.cfg
# And confirm that it has been changed using:
grep "batch_size" /home/azam/spine_bilal/spine_workshop_2024/basics/training/uresnet.cfg

#AND
sed -i 's/iterations: 5000/iterations: 9000/' /home/azam/spine_bilal/spine_workshop_2024/basics/training/uresnet.cfg
grep "iterations" /home/azam/spine_bilal/spine_workshop_2024/basics/training/uresnet.cfg


sed -i 's/iterations: 8000/iterations: 25000/' /home/azam/spine_bilal/spine_workshop_2024/basics/training/grappa_shower.cfg
sed -i 's/batch_size: 128/batch_size: 6/' /home/azam/spine_bilal/spine_workshop_2024/basics/training/grappa_shower.cfg
grep "iterations" /home/azam/spine_bilal/spine_workshop_2024/basics/training/grappa_shower.cfg 
grep "batch_size" /home/azam/spine_bilal/spine_workshop_2024/basics/training/grappa_shower.cfg
