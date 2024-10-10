# Step 1: SSH into Polaris
ssh -KY azam@polaris.alcf.anl.gov

# Password: (8-digit code from MobilePass application)

# Step 2: Submit an Interactive Job to a Compute Node
qsub -I -l select=1 -l walltime=01:00:00 -A Nu_Novel -l filesystems=eagle -q debug
# The debug queue is specifically for smaller jobs (1–2 nodes) with a maximum run time of 1 hour.


# Step 3: Change the directory
cd spine_bilal/

# Step 4: Load Necessary Modules
module use /soft/spack/gcc/0.6.1/install/modulefiles/Core
module load apptainer

# Step 5: Start Jupyter Notebook
# apptainer exec --nv /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif jupyter-notebook --no-browser --port=8899 --ip=0.0.0.0
# if and external path needs to bind
apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif jupyter-notebook --no-browser --port=8899 --ip=0.0.0.0


# Step 6: Set Up SSH Tunnel from Local Machine
ssh -L 8899:localhost:8899 azam@polaris.alcf.anl.gov -t ssh x3005c0s1b0n0 -L 8899:localhost:8899

ssh -L 8899:localhost:8899 azam@polaris.alcf.anl.gov -t ssh x3201c0s37b0n0 -L 8899:localhost:8899


# Step 7: File paths
file_keys: /mnt/eagle/clone/g2/projects/Nu_Novel/Tutorials/spine_workshop_2024/data_samples/Small_LArCV_files/generic_small.root
weight_path: /mnt/eagle/clone/g2/projects/Nu_Novel/Tutorials/spine_workshop_2024/data_samples/weights/generic_snapshot-4999.ckpt

###################################

# Check quota on POLARIS
qstat -u $USER
qdel xxxx

###################################

scp -r azam@polaris.alcf.anl.gov:'/home/azam/spine_bilal/play.h5' .

scp -r lets_play.ipynb azam@polaris.alcf.anl.gov:/home/azam/spine_bilal/lets_play
scp -r play.h5 azam@polaris.alcf.anl.gov:/home/azam/spine_bilal/lets_play

###################################

## Specific queues and job submission guidelines
1. Submit to the debug Queue for Interactive Jobs:
The debug queue is specifically for smaller jobs (1–2 nodes) with a maximum run time of 1 hour, which seems to fit your needs for interactive testing. You can submit your job to the debug queue using the following command:

# qsub -I -l select=1 -l walltime=01:00:00 -A Nu_Novel -l filesystems=eagle -q debug

This command:
Requests 1 node (select=1).
Requests 1 hour of wall time (walltime=01:00:00).
Specifies your project account (-A Nu_Novel).
Specifies the eagle filesystem (-l filesystems=eagle).
Submits the job to the debug queue (-q debug).


2. Using the prod Queue for Larger Jobs:
If you are running a larger job, the prod queue can route your job to one of the execution queues (small, medium, large, etc.). Here is how you can submit a larger job via the prod queue:

#qsub -I -l select=10:ncpus=1 -l walltime=01:00:00 -A Nu_Novel -l filesystems=eagle -q prod

qsub -I -l select=10 -l walltime=03:00:00 -A Nu_Novel -l filesystems=eagle -q prod # Working

This command:
Requests 10 nodes (select=10:ncpus=1) for a larger job.
Requests 1 hour of wall time.
Specifies the project account and filesystem


3. Submitting to the preemptable Queue (if flexible):
If you do not mind your job being interrupted by higher-priority jobs, you can use the preemptable queue, which allows your job to be preempted if demand jobs come in:

# qsub -I -l select=1 -l walltime=01:00:00 -A Nu_Novel -l filesystems=eagle -q preemptable

This would allow the job to run in the preemptable queue, but it can be interrupted.







