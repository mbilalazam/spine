# 1_uresnet_ppn

docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/1_uresnet_ppn.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/1_output_uresnet_ppn.log 2> /home/bilal/polaris/2025_02_17/full_logs/1_error_uresnet_ppn.log


# 2_graph_spice
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/2_graph_spice.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/2_output_graph_spice.log 2> /home/bilal/polaris/2025_02_17/full_logs/2_error_graph_spice.log


# 3_grappa_shower
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/3_grappa_shower.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/3_output_grappa_shower.log 2> /home/bilal/polaris/2025_02_17/full_logs/3_error_grappa_shower.log 


# 4_grappa_track
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/4_grappa_track.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/4_output_grappa_track.log 2> /home/bilal/polaris/2025_02_17/full_logs/4_error_grappa_track.log


# 5_grappa_inter
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/5_grappa_inter.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/5_output_grappa_inter.log 2> /home/bilal/polaris/2025_02_17/full_logs/5_error_grappa_inter.log

# 6_full_chain_graph_spice
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/6_full_chain_graph_spice.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/6_output_full_chain_graph_spice.log 2> /home/bilal/polaris/2025_02_17/full_logs/6_error_full_chain_graph_spice.log

# 7_full_chain_grappa_shower
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/7_full_chain_grappa_shower.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/7_output_full_chain_grappa_shower.log 2> /home/bilal/polaris/2025_02_17/full_logs/7_error_full_chain_grappa_shower.log

# 8_full_chain_grappa_track
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/8_full_chain_grappa_track.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/8_output_full_chain_grappa_track.log 2> /home/bilal/polaris/2025_02_17/full_logs/8_error_full_chain_grappa_track.log

# 9_full_chain
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/9_full_chain.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/9_output_full_chain.log 2> /home/bilal/polaris/2025_02_17/full_logs/9_error_full_chain.log

# 11_2x2_full_chain_240819
docker run --rm -v /home/bilal:/mnt/data \
deeplearnphysics/larcv2:ub22.04-cuda12.1-pytorch2.4.0-larndsim \
python /mnt/data/spine_bilal/spine/bin/run.py -c /mnt/data/polaris/2025_02_17/11_2x2_full_chain_240819.cfg \
> /home/bilal/polaris/2025_02_17/full_logs/11_output_2x2_full_chain_240819.log 2> /home/bilal/polaris/2025_02_17/full_logs/11_error_2x2_full_chain_240819.log
