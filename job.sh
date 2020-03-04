#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --qos=normal
#SBATCH -n 1
#SBATCH -c 1
#SBATCH -J circle
#SBATCH -A 1600011084
#SBATCH --partition=compute
#SBATCH -o slurm-%x.%6j.%12M.out

module load anaconda/3.5.1

python3 longos.py


echo "
*******************
job finished!
*******************
"
