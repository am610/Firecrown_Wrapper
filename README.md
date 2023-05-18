# Firecrown Wrapper
Track of Firecrown Wrapper developement which will be integrated to the LSST TD Pipeline

### Ayan Mitra 2023
--------------


### Firecrown Wrapper Manual for running with Cosmosis for SN Cosmology
-------------- 


Summary 
-------------- 
The Firecrown wrapper is a standalone unit which
can be run to link any given Supernova input data files to Cosmosis for
dark energy parameter estimation via firecrown likelihood module.

Why 
-------------- 
The LSST Rubin DESC data files have transitioned to
a new file format known as `sacc`[1]. This modification necessitated the
introduction of the Firecrown wrapper. The wrapper  aids in the conversion
of Supernova (SN) data files to the sacc format.  Once transformed,
these files can be processed by the Firecrown likelihood module, which
subsequently feeds them into Cosmosis for DE parameter estimation and
post processing for generating plots.


Firecrown Wrapper Flowchart 
--------------

 SN Hubble Diagram (HD) + Covariance Matrix [Input] --> Single `sacc`
 file --> Firecrown Likelihood --> Cosmosis --> DE Parameter estimation +
 Plots [Output]


Input requirements 
--------------
	 
   Mandatory  : Input file path to HD and covariance matrix, Name of HD file and covariance matrix file, cosmosis input
	 `ini` file.  
   
   Assumption : HD and covariance matrix files are
	 in the same folder.
  
  Additional optional attributes can be seen via the help command as : 
   
   `$SNANA_DEBUG/submit_batch_firecrown/NEW_AYAN_DEBUG-3/dist/Firecrown_wrapper_example-2 --help`

Notes 
--------------
	
  The wrapper can be used as : 
  
  (a) a standalone unit for submitting
	batch job in Perlmutter or, 
  
  (b) can also be used with SNANA/DESC
	TD pipeline software's function : `submit_batch_jobs.sh` for
	submitting batch job(s).


Syntax 
--------------

	(a) To simply run the code as a batch job in perlmutter the following example job script can be used as a template :
    
	  #!/bin/bash
	  #SBATCH -A m1727
	  #SBATCH -C cpu
	  #SBATCH --qos=debug
	  #SBATCH --time=00:10:00
	  #SBATCH --nodes=3
	  #SBATCH --error=perl_firecrown-%j.err
	  #SBATCH -o perl_firecrown.log
	  #SBATCH --mail-user=ayanmitra375@gmail.com
	  #SBATCH -J Firecrown


	  NUM_PROCESSES=16
	  export OMP_NUM_THREADS=4


	  #Example 1
	  # Syntax : srun -u -n ${NUM_PROCESSES}  --cpus-per-task ${OMP_NUM_THREADS} $SNANA_DEBUG/submit_batch_firecrown/NEW_AYAN_DEBUG-3/dist/Firecrown_wrapper_example-2 [Input/Folder/HD/covariance/matrix] [HD.txt] [cov.txt] [cosmosis.ini]
	  srun -u -n ${NUM_PROCESSES}  --cpus-per-task ${OMP_NUM_THREADS} $SNANA_DEBUG/submit_batch_firecrown/NEW_AYAN_DEBUG-3/dist/Firecrown_wrapper_example-2 $HOME/Analysis/7_CREATE_COV/LSST_BINNED_COV_BBC_SIMDATA_PHOTOZ_1/output hubble_diagram.txt covsys_000.txt.gz sn_only.ini --summary $PWD/FIRECROWN_OUTPUT/SUMMARY.YAML -O $PWD/FIRECROWN_OUTPUT/

	  # ## End of file
    


Save the above code in a file `test.sh` and then from perlmutter terminal submit the job as : `sbatch test.sh`
* Notes : qos = `debug` can be changed to `regular`. `nodes` and time can be modified accordingly (as of now Perlmutter's maximum time limit is 12 hours). The outputs will be stored in `$PWD/FIRECROWN_OUTPUT/`. cosmosis input file shown here is `sn_only.ini`, consult cosmosis manual for more information.







	 (b) To run with `submit_batch_jobs.sh` a separate Input yaml
	 file is needed suitable for `submit_batch_jobs.sh`. An example
	 of a test.yaml is below :


	  
    ```## YAML begins : CONFIG:
	    BATCH_INFO: sbatch
	    $SBATCH_TEMPLATES/SBATCH_Perlmutter.TEMPLATE
	    25 JOBNAME: srun -n 2
	    $SNANA_DEBUG/submit_batch_firecrown/NEW_AYAN_DEBUG-3/dist/Firecrown_wrapper_example-2
	    BATCH_WALLTIME: "12:00:00" FIRECROWN_INPUT_FILE:
	    /global/cfs/cdirs/lsst/groups/TD/SN/SNANA/SURVEYS/LSST/ROOT/starterKits/firecrown+submit_batch_jobs/Cosmosis_Input_Scripts/sn_planck.ini
	    ENV_REQUIRE: FIRECROWN_DIR FIRECROWN_EXAMPLES_DIR CSL_DIR
	    OUTDIR: output_firecrown_sn_cmb WFITAVG:
	    #- LSST_BINNED_COV_BBC_SIMDATA_SPECZ
	    - LSST_BINNED_COV_BBC_SIMDATA_PHOTOZ
	    COVOPT:  ALL NOSYS INPDIR: -
	    /pscratch/sd/d/desctd/PIPPIN_OUTPUT/PLASTICC_COMBINED_PUBLISHED/7_CREATE_COV/LSST_BINNED_COV_BBC_SIMDATA_PHOTOZ_1/output
	    -
	    /pscratch/sd/d/desctd/PIPPIN_OUTPUT/PLASTICC_COMBINED_PUBLISHED/7_CREATE_COV/LSST_BINNED_COV_BBC_SIMDATA_PHOTOZ_2/output
	  ##END_YAML
    

Launch the job : `submit_batch_jobs.sh test.yaml`


Outputs 
--------------

   Each successful output will produce the following three sub folders in the desired location :  
   
   (1) COSMOSIS-CHAINS
	    Contains the output chain files (name as written in input
	     `.ini` file) and `INPUT.INFO` file which logs all input
	     commands.
       
   (2) ERROR_LOGS
	     contains the error and log files of each stages. Also
	     contains files recording the time taken in each stages.    
       
   (3) PLOTS
	     contains the results of the analysis from the chain files
	     i.e. plots and parameter estimation summary files.  
       
   (4) Summary Yaml file : summarizes the outcomes of each stages : Fail or Successful. Also lists the main cosmological results (some fields are still under construction).   




##### ********************************************************************
********************************************************************


[1] https://sacc.readthedocs.io/en/latest/intro.html

[![gagan.jpg](https://i.postimg.cc/76vxpmSC/gagan.jpg)](https://postimg.cc/R3R5t1s9)


<i>"Pratima Visarjan", Gaganendranath Tagore, Watercolour on Paper, circa 1915.</i>
