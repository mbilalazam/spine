mkdir -p /home/azam/spine_bilal/batch_outputs

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/1_uresnet_ppn.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-train_uresnet_ppn.txt \
2> /home/azam/spine_bilal/batch_outputs/error-train_uresnet_ppn.txt


apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/2_graph_spice.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-graph_spice.txt \
2> /home/azam/spine_bilal/batch_outputs/error-graph_spice.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/3_grappa_shower.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-grappa_shower.txt \
2> /home/azam/spine_bilal/batch_outputs/error-grappa_shower.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/4_grappa_track.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-grappa_track.txt \
2> /home/azam/spine_bilal/batch_outputs/error-grappa_track.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/5_grappa_inter.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-grappa_inter.txt \
2> /home/azam/spine_bilal/batch_outputs/error-grappa_inter.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/6_full_chain_graph_spice.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-full_chain_graph_spice.txt \
2> /home/azam/spine_bilal/batch_outputs/error-full_chain_graph_spice.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/7_full_chain_grappa_shower.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-full_chain_grappa_shower.txt \
2> /home/azam/spine_bilal/batch_outputs/error-full_chain_grappa_shower.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/8_full_chain_grappa_track.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-full_chain_grappa_track.txt \
2> /home/azam/spine_bilal/batch_outputs/error-full_chain_grappa_track.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/9_full_chain.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-full_chain.txt \
2> /home/azam/spine_bilal/batch_outputs/error-full_chain.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/10_generic_full_chain_with_post.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-generic_full_chain_with_post.txt \
2> /home/azam/spine_bilal/batch_outputs/error-generic_full_chain_with_post.txt

apptainer exec --nv --bind /lus/eagle:/mnt/eagle /lus/eagle/clone/g2/projects/Nu_Novel/larcv2_ub22.04-cuda12.1-pytorch2.4.0-larndsim.sif \
python /home/azam/spine_bilal/spine/bin/run.py -c /home/azam/spine_bilal/configs/11_2x2_full_chain_240719.cfg \
| tee /home/azam/spine_bilal/batch_outputs/output-2x2_full_chain_240719.txt \
2> /home/azam/spine_bilal/batch_outputs/error-2x2_full_chain_240719.txt
