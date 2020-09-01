

# Costs 

Overview of Costs Associated with AWS

Amazon Web Services (AWS) allows researchers to use AWS resources for NRAO data processing. This section presents costs associated with using these resources. Resource types include: Instances, EBS Volumes, EBS Snapshots, S3, and Glacier.

The primary resource utilized is Instances.

Other resources are methods of storing input and output data: EBS, EFS, Snapshots, S3, and Glacier.

The way to contain costs is to first determine the needs of the code that is to be run. Then AWS resources can be matched to those needs as efficiently as possible given the circumstances.

# CASA Hardware Requirements

## Running CASA

Selecting a suitable instance type and size requires some knowledge about the CASA tasks to be run. The [Hardware Requirements](https://casa.nrao.edu/casadocs-devel/stable/usingcasa/hardware-requirements) page includes sizing guidelines for typical computing hardware that can be translated to AWS instance types.

## Choosing an Instance

An instance is the best place to start (allocating resources). A list of on-demand instance costs and capabilities are listed here: <https://aws.amazon.com/ec2/pricing/>, though be aware it takes a minute to load and nothing will display under \"on-demand\" while the data loads. Note that spot instances can be utilized to run jobs at a much reduced cost; this is covered in the [Instances](https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-on-amazon-web-services/instances) section of this document. The goal is to select an Instance type that is large enough to do the job, but leaves as few resouces idle as possible.

## File I/O

Default EBS is generally used. However, options exist to specify different types of EBS, e.g., storage with higher iops, etc., that cost more. EBS storage pricing details can be found here: <https://aws.amazon.com/ebs/pricing/>. For reference, there is a detailed discussion of EBS volume types here: <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>.

## Instance Store

Some instance types are pre-configured with attached SSD storage called \"instance store\". If you start such an instance, part of its intrinsic cost is this storage. More details about instance store are here: <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-instance-store-volumes.html#adding-instance-storage-instance>.

# Selecting an Instance Type for CASA

## What to try First

There are over 40 instance types with varying amounts of RAM and CPUs. There are, when you look closely, many storage options, but a few recurrent themes emerge. The simple storage system (S3) is primarily for storing large volumes of data from a few hours to a few months. S3 can be used to stage input and output data. You can share these data with other users. EBS storage is the most often used \"attached\" storage with performance comparable to a very good hard drive attached to your desktop system. However, it\'s bandwidth goes up with the core count, contrary to ordinary storage. The number of cores and GBs of RAM depend entirely on instance type. If you were to want 4 GB RAM per core (as recommended in CASA [Hardware Requirements](https://casa.nrao.edu/casadocs-devel/stable/usingcasa/hardware-requirements)) and 10 cores, you can find the closest instance on the list of instance types, <https://aws.amazon.com/ec2/instance-types/>. m4.4xlarge is close with 16 \"vCPU\" and 64 GB. Despite apearances, it does not have enough cores. AWS lists \"vCPUs\" (a.k.a. hyperthread) instead of cores. A vCPU is an internal CPU scheduling trick that is useful for certain classes of programs, but is nearly always detrimental in scientific computing, e.g., CASA. To summarize, 2 Amazon vCPUs equal 1 core. From here on cores are used, where 1 core = 2 vCPUs.

Continuing with the example of looking for an instance that meets the contraints of 10 cores and 4 GB RAM per core, it makes sense to look at core count first. The listing of instances with their core count, memory, and cost are here: <https://aws.amazon.com/ec2/pricing/>. There are no instances with 10 cores. The closest have 8 and 16 cores. So we\'ll look at \>=16 core instances. Also, we\'ll throw out any instances that do not have: RAM \>= (\#cores \* 4 GB RAM). What is left (without looking at immensely large and therefore expensive instances) are these:

-   m4.10xlarge with 20 cores and 160 GB of RAM. Cost: \$2.394/hour
-   x1.32xlarge with 64 cores and 1962 GB of RAM. Cost: \$13.338/hour
-   r3.8xlarge with 16 cores and 244 GB of RAM. Cost: \$2.66/hour
-   d2.8xlarge with 18 cores and 244 GB of RAM. Cost: \$5.52/hour

Selecting 10 cores produced a results list that contains the most expensive instances. If it\'s feasible to use a number of cores that is an exponent of 2, a more efficient arrangement may result.  Looking at what instances with 2\^3 = 8 cores also meet the criterion of 4GB RAM per core, for example:

-   m4.4xlarge 8 cores, 64 GB RAM. Cost: \$0.958/hour
-   c3.8xlarge 8 cores, 60 GB RAM. Cost: \$1.68/hour (instance store)

The c3.8xlarge, although very similar to the m4.4xlarge, costs 75% more per hour. That\'s because c3.8xlarge comes pre-configured with local (instance store) storage. This is charged even when it is not used. It is something to watch out for. Instance store can be useful, but it is tricky to make use of. The use of instance store is outside the scope of this document. When considering 8 core instances, m4.4xlarge appears to be the most attractive option in this case.

-   m4.4xlarge 8 cores 4 GB/core \$0.958/hour
-   r3.8xlarge 16 cores \~15 GB/core \$2.66/hour
-   r3.4xlarge 8 cores \~7.6 GB/core \$1.33/hour

r3.4xlarge is not far behind in price. And it has more RAM as well as 320 GB of instance store storage. So zeroing in on the best instance takes some time. However, it is not time well spent to find the most efficient instance until many instances are to be run or an instance is run for a long period of time.

 

# What Instance(s) to Consider for Big or Long Jobs

So, to begin, it is probably best to choose EC2 as your primary storage, S3 for cold storage, and an instance with \>=4GB RAM per core. A more detailed discussion of these (and other) hardware considerations is outlined in the  [Hardware Requirements](https://casa.nrao.edu/casadocs-devel/stable/usingcasa/hardware-requirements) page.  What is covered here is what is sufficient to get started. Keep in mind that, since AWS has hyperthreading turned on, their \"2 cores\" means \"1 physical core\" (2 hyperthreads). For example, an AWS \"8 core\" instance type is actually only 4 physical cores. CASA does not make good use of virtual cores so if you want a system with 4 actual cores, select an AWS \"8 core\" system with \>= 16 GB of RAM. That should be sufficent to get started. As you use AWS more, you\'ll want to invest more time in optimizing the instance type based on the details of your processing case. If you are running only a few instances, such optimizations are not worth much effort, but if you plan to run hundreds of jobs, this can have a very significant impact on total run time and cost. The 4GB per physical core rule should be sufficient to get started, but more demanding imaging tasks will likely require 8GB or 16Gbyte per core.

# AWS Storage for CASA

## Root Volume

Starting an Instance with an NRAO AMI and accepting the storage defaults creates a suitable root volume for CASA.  If desired, exhaustive detail on root volumes is availabe at the AWS website: <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html>.

## Additional EBS Volumes

Additional EBS volumes can be added to an instance at any time during it\'s life cycle. See the following link for more information: <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html>.

 

